import requests
import time

rpc_url = "https://api.mainnet-beta.solana.com"
# 配置代理
proxies = {
    "http": "http://38.180.95.9:20171",  # 替换为有效的公共代理
    "https": "http://38.180.95.9:20171", # 替换为有效的公共代理
}


def get_latest_block():
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getEpochInfo",
        "params": []
    }
    response = requests.post(rpc_url, json=payload)
    print(response)
    return response.json()['result']['absoluteSlot']


def get_signatures_for_block(slot):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBlock",
        "params": [slot, {"encoding": "json", "maxSupportedTransactionVersion": 0}]
    }
    response = requests.post(rpc_url, json=payload)

    if response.status_code == 200:
        return response.json().get('result', [])
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return []


def monitor_new_tokens():
    last_slot = get_latest_block()
    print(f"Starting block monitoring at slot: {last_slot}")

    while True:
        # Get the latest block
        current_slot = get_latest_block()
        if current_slot > last_slot:
            print(f"New block detected at slot {current_slot}")
            transactions = get_signatures_for_block(current_slot)
            for txn in transactions:
                print(f"Transaction: {txn}")
                # 这里可以添加逻辑来判断是否为代币发行交易
                # 比如，查看交易是否涉及 mint 或代币创建的指令
            last_slot = current_slot

        time.sleep(5)  # 每5秒检查一次新区块


# 启动监控
monitor_new_tokens()
