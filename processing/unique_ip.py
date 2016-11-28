import re


# def extract_ips(content):
#     pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#     # pattern = r"""
#     #     ^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
#     #     (25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
#     # """
#     regex = re.compile(pattern)
#     ips = re.findall(regex, content)
#     tbl = {}
#     for ip in ips:
#         tbl[ip] = tbl.get(ip, 0) + 1
#     return tbl
#
#
# with open('log.txt', 'r') as f:
#     content = f.read()
#     cnt = extract_ips(content)
#     for k, v in cnt.iteritems():
#         print k, v

def extract_ips(log_file):
    with open(log_file, 'r') as f:
        logs = f.read()
        ip_regex = r"\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3}"
        ip_pattern = re.compile(ip_regex)

        ips = re.findall(ip_pattern, logs)
        s = set()
        for ip in ips:
            s.add(ip)

        return [ip for ip in s]
