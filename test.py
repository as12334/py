import json
import websocket
import requests
from solana.rpc.api import Client
from solana.rpc.types import TokenAccountOpts

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

# 设置 HTTP 代理
session = requests.Session()
session.proxies.update(proxies)

# 创建 Solana 客户端并使用代理
client = Client("https://sg110.nodes.rpcpool.com")


# 获取最新的区块信息
def get_latest_block():
    try:
        # 获取最新的区块信息
        response = client.get_epoch_info()

        # 获取当前 epoch 的信息，最新的区块哈希可以从中获得
        latest_blockhash = response['result']['blockhash']

        print(f"Latest Block Hash: {latest_blockhash}")
    except Exception as e:
        print(f"Error fetching block: {e}")


# 分析交易中的代币操作
def analyze_transaction(tx):
    instructions = tx['transaction']['message']['instructions']
    for instruction in instructions:
        if instruction['program'] == 'token':  # 监控 Token 相关操作
            print("Token-related Instruction:", instruction)


# 监听 WebSocket 并监控新交易
def on_message(ws, message):
    try:
        data = json.loads(message)
        for item in data:
            # 假设创建代币的操作是 InitializeMint，可以根据实际情况修改
            if "InitializeMint" in item['data']:
                print("New Token Created:", item)
    except Exception as e:
        print(f"Error processing WebSocket message: {e}")


# WebSocket 连接配置
def on_open(ws):
    print("WebSocket opened")


# WebSocket URL
ws_url = "wss://api.mainnet-beta.solana.com/"

# 设置 WebSocket 代理（通过 SOCKS 代理）
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, PROXY_HOST, int(PROXY_PORT))
socket.socket = socks.socksocket

# 创建 WebSocket 应用并连接
ws = websocket.WebSocketApp(ws_url, on_message=on_message, on_open=on_open)


# 启动 WebSocket 监听
def start_websocket():
    ws.run_forever()


# 主程序
if __name__ == "__main__":
    # 获取最新区块
    get_latest_block()

    # 启动 WebSocket 监听
    start_websocket()
