from xml.etree import ElementTree as ET
import urllib.parse
import os
import base64

log_path ="./burp_logs"

def parse_log(log_path):
    '''
    This function accepts burp log file path.
    and returns a dict. of request and responsea
    result = {'GET /page.php...':'200 OK HTTP / 1.1....','':'',.....}
    '''
    result = {}
    if not os.path.exists(log_path):
        print("[+] Error!!!", log_path, "doesn't exist..")
        exit()

    try:
        tree = ET.parse(log_path)
    except ET.ParseError:
        print('[+] Oops..! Please make sure binary data is not present in Log, like raw image dump, flash (.swf files) dump, etc.')
        exit()

    root = tree.getroot()
    for reqs in root.findall('item'):
        raw_req = reqs.find('request').text
        if raw_req is not None:
            raw_req = urllib.parse.unquote(raw_req)  # Removed .decode('utf8')
        raw_resp = reqs.find('response').text
        result[raw_req] = raw_resp
    return result

result=parse_log(log_path)
for items in result:
    # Convert the string to bytes before encoding
    encoded = base64.b64decode(items.encode('utf-8'))
    print(encoded.decode('utf-8'))  # Decode to print as a string
