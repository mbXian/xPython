import requests

# 通过url直接加上请求参数，与通过params传参效果是一样的
response = requests.get(url='http://www.baidu.com/s?wd=requests模块')
# 通过params传参
response2 = requests.get(url='http://www.baidu.com/s', params={"wd": "requests模块"})
print('状态码=' + response.status_code)		# 打印状态码
print('内容：' + response.text)		# 获取响应内容