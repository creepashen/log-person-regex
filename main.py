import re

text = "[INFO] user=Ahmed id=A12 action=login time=10:30 [ERROR] user=Sara id=B77 action=fail_login code=404 [WARN] user=Khalid id=C3 action=login [INFO] user=Noor id=D40 action=logout time=12:10"

matches = re.findall(r"user=(\w+).*?id=([A-Z0-9]+).*?action=([A-Za-z_]+)", text)

result = matches

print(result)