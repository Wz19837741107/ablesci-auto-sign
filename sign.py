import requests

# 你的 Cookie
COOKIE = "Hm_lvt_21ea3daf4a17e94a98a483d3d810f41a=1779342311; HMACCOUNT=C2AB941822F3254A; ablesci-serial=4faf414ad5933008af3884991880f96f; security_session_verify=cf3b56272f4d47f9666ae010b4187b39; advanced-frontend=enn7qhdluo0q7h6mn3efstr78v; _identity-frontend=016dddc6ad22fc3f576cd64a26c69e84f45931ebc3c48f9c6035b801c094db5ba%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_identity-frontend%22%3Bi%3A1%3Bs%3A52%3A%22%5B1082758%2C%22Wk5t4t8eDcnVymQANC_s3tRxdP-j0SBP%22%2C2592000%5D%22%3B%7D; _csrf=ca946a1aa835cc9f4a1e5601e3a840e38330dedbfa25f772699e3ca624787a1aa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Qp7Gk9t8CKvsjek4SNgJ3HgZRnYrNcrZ%22%3B%7D; Hm_lpvt_21ea3daf4a17e94a98a483d3d810f41a=1779344589"

# 签到接口
url = "https://www.ablesci.com/user/sign"

headers = {
    "Cookie": COOKIE,
    "User-Agent": "Mozilla/5.0"
}

# 发送请求
response = requests.get(url, headers=headers)

# 输出结果
print(response.text)
