import requests

# 代理配置
PROXY_HOST = "38.180.95.9"  # 代理服务器地址
PROXY_PORT = "20171"  # 代理服务器端口
PROXY_USER = ""  # 代理用户名（如果需要）
PROXY_PASS = ""  # 代理密码（如果需要）

# 配置代理
proxies = {
    "http": "http://38.180.95.9:20171",  # 替换为有效的公共代理
    "https": "http://38.180.95.9:20171", # 替换为有效的公共代理
}

# 测试代理是否生效
url = "https://sg110.nodes.rpcpool.com"  # Solana RPC URL 或其他公共 URL

# 设置代理
response = requests.get(url, proxies=proxies)

# 输出代理请求的结果
print("Status Code:", response.status_code)
print("Response:", response.text[:200])  # 打印前200个字符

# 测试是否通过代理访问
if response.status_code == 200:
    print("代理配置成功!")
else:
    print("代理配置失败!")
