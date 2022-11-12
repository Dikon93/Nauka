import re
# "." uznaje dowolny znak
if re.match("ko.", "kot"):
    print("dopasowano")
else:
    print("niedopasowano")
