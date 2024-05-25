# from xml.etree import ElementTree as ET
# import urllib.parse
# import os
# import base64
# import csv

# log_path = "./good_requests.log"
# output_csv_log='http_log.csv'
# class_flag= "1"

# class LogParse:
#     def __init__(self):
#         pass

#     def parse_log(self, log_path):
#         '''
#         This function accepts burp log file path
#         and returns a dict of requests and responses
#         result = {'GET /page.php...':'200 OK HTTP / 1.1....','':'',.....}
#         '''
#         result = {}
#         if not os.path.exists(log_path):
#             print("[+] Error!!!", log_path, "doesn't exist..")
#             exit()

#         try:
#             tree = ET.parse(log_path)
#         except ET.ParseError:
#             print(
#                 '[+] Oops..! Please make sure binary data is not present in the log, like raw image dump, flash (.swf files) dump, etc.')
#             exit()

#         root = tree.getroot()
#         for reqs in root.findall('item'):
#             raw_req = reqs.find('request').text
#             if raw_req is not None:
#             raw_req = urllib.parse.unquote(raw_req).decode('utf8')
#             raw_resp = reqs.find('response').text
#             result[raw_req] = raw_resp
#         return result

#     def parseRawHTTPReq(self, rawreq):
#         try:
#             raw = rawreq.decode('utf8')
#         except Exception as e:
#             raw = rawreq
#         global headers, method, body, path
#         headers = {}
#         sp = raw.split('\r\n\r\n', 1)
#         if len(sp) > 1:
#             head = sp[0]
#             body = sp[1]
#         else:
#             head = sp[0]
#             body = ""
#         lines = head.split('\r\n')
#         request_line = lines[0]
#         method, path, _ = request_line.split(' ', 2)
#         for line in lines[1:]:
#             if ': ' in line:
#                 key, value = line.split(': ', 1)
#                 headers[key] = value
#         return headers, method, body, path

# #jaii ganesha
# badwords=['sleep', 'drop', 'uid', 'select', 'waitfor', 'delay', 'system', 'union', 'order by', 'group by']
# def ExtractFeatures(method, path_enc, body_enc, headers):
#     badwords_count=0
#     path = urllib.parse.unquote_plus(path_enc)
#     body = urllib.parse.unquote(body_enc)
#     single_q = path.count("'") + body.count("'")
#     double_q = path.count("\"") + body.count("\"")
#     dashes = path.count("--") + body.count("--")
#     braces = path.count("(") + body.count("(")
#     spaces = path.count(" ") + body.count(" ")
#     for word in badwords:
#         badwords += path.count(word) + body.count(word)

#     for header in headers:
#         badwords_count += headers[header].count(word) + headers[header].count(word)
#         return [method, path_enc.encode('utf-8').strip(), body_enc.encode('utf-8').strip(), single_q, double_q, dashes,
#                 braces, spaces, badwords_count,class_flag]
       

# # Open the log file
# with open(output_csv_log, "w", newline='') as f:
#     c = csv.writer(f)
#     c.writerow(["method","path", "body","single_q", "double_q", "dashes", "braces","spaces", "badwords", "class"])
#     f.close();
#     lp= LogParse();
#     result = lp.parse_log(log_path)
#     f=open(output_csv_log, "w")
#     c=csv.writer(f);
#     for raw_req in result:
        
#         data = []
#     try:
#         raaw = base64.b64decode(raw_req.encode('utf-8'))
#         headers, method, body, path = lp.parseRawHTTPReq(raaw)
#         result=ExtractFeatures(method,path,body, headers )
#         c.writerow(result)
#     except Exception as e:
#         print(f"Error processing request: {e}")
    
from xml.etree import ElementTree as ET
import urllib.parse
import os
import base64
import csv

log_path = "./burp_logs"
output_csv_log = 'httplog.csv'
class_flag = "1"

class LogParse:
    def __init__(self):
        pass

    def parse_log(self, log_path):
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

    def parseRawHTTPReq(self, rawreq):
        try:
            raw = rawreq.decode('utf8')
        except Exception as e:
            raw = rawreq
        global headers, method, body, path
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

badwords = ['sleep', 'drop', 'uid', 'select', 'waitfor', 'delay', 'system', 'union', 'order by', 'group by']

def ExtractFeatures(method, path_enc, body_enc, headers):
    badwords_count = 0
    path = urllib.parse.unquote_plus(path_enc)
    body = urllib.parse.unquote(body_enc)
    single_q = path.count("'") + body.count("'")
    double_q = path.count('"') + body.count('"')
    dashes = path.count("--") + body.count("--")
    braces = path.count("(") + body.count("(")
    spaces = path.count(" ") + body.count(" ")
    for word in badwords:
        badwords_count += path.count(word) + body.count(word)

    for header in headers:
        badwords_count += headers[header].count(word) + headers[header].count(word)

    return [method, path_enc.encode('utf-8').strip(), body_enc.encode('utf-8').strip(), single_q, double_q, dashes,
            braces, spaces, badwords_count, class_flag]

# Open the log file
with open(output_csv_log, "w", newline='') as f:
    c = csv.writer(f)
    c.writerow(["method", "path", "body", "single_q", "double_q", "dashes", "braces", "spaces", "badwords", "class"])
    lp = LogParse()
    result = lp.parse_log(log_path)
    for raw_req in result:
        try:
            raaw = base64.b64decode(raw_req.encode('utf-8'))
            headers, method, body, path = lp.parseRawHTTPReq(raaw)
            row = ExtractFeatures(method, path, body, headers)
            c.writerow(row)
        except Exception as e:
            print(f"Error processing request: {e}")
