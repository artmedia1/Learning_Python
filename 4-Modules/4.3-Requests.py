import requests

# HTTP Status Codes
# 200 - OK
# 403 - Forbidden
# 404 - Not Found

r = requests.get("https://www.google.com")
print(r.status_code)

print(r.headers)

print(r.headers["Date"])