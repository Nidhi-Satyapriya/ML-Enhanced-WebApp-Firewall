from xml.etree import ElementTree as ET
import urllib.parse
import os
import base64
import csv

log_path = "./burp_log2"

def parse_log(log_path):
    '''
    This function accepts burp log file path
    and returns a dict of requests and responses
    result = {'GET /page.php...':'200 OK HTTP / 1.1....','':'',.....}
    '''
    result = {}
    if not os.path.exists(log_path):
        print("[+] Error!!!", log_path, "doesn't exist..")
        exit()

    try:
        tree = ET.parse(log_path)
    except ET.ParseError:
        print('[+] Oops..! Please make sure binary data is not present in the log, like raw image dump, flash (.swf files) dump, etc.')
        exit()

    root = tree.getroot()
    for reqs in root.findall('item'):
        raw_req = reqs.find('request').text
        if raw_req is not None:
            raw_req = urllib.parse.unquote(raw_req)
        raw_resp = reqs.find('response').text
        result[raw_req] = raw_resp
    return result

def parseRawHTTPReq(rawreq):
    try:
        raw = rawreq.decode('utf8')
    except Exception as e:
        raw = rawreq
    headers = {}
    sp = raw.split('\r\n\r\n', 1)
    if len(sp) > 1:
        head = sp[0]
        body = sp[1]
    else:
        head = sp[0]
        body = ""
    lines = head.split('\r\n')
    request_line = lines[0]
    method, path, _ = request_line.split(' ', 2)
    for line in lines[1:]:
        if ': ' in line:
            key, value = line.split(': ', 1)
            headers[key] = value
    return headers, method, body, path

# Open the log file
with open('httplog.csv', "w", newline='') as f:
    c = csv.writer(f)
    c.writerow(["method", "body", "path", "headers"])

result = parse_log(log_path)
for raw_req in result:
    data = []
    try:
        raaw = base64.b64decode(raw_req.encode('utf-8'))
        headers, method, body, path = parseRawHTTPReq(raaw)
        data.append(method)
        data.append(body)
        data.append(path)
        data.append(headers)
        with open('httplog.csv', "a", newline='') as f:
            c = csv.writer(f)
            c.writerow(data)
    except Exception as e:
        print(f"[+] Error processing request: {e}")
        continue
