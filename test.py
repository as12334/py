from solana.rpc.api import Client

# 连接到 Solana RPC 服务
rpc_url = "https://api.mainnet-beta.solana.com"
client = Client(rpc_url)

def get_latest_block():
    # 获取最新区块的 slot
    response = client.get_epoch_info()
    if response['result']:
        latest_slot = response['result']['absoluteSlot']  # 获取当前最新的 slot
        print(f"当前最新的 Slot: {latest_slot}")

        # 获取区块信息
        block_info = client.get_block(latest_slot)
        print(f"区块信息: {block_info}")
    else:
        print("获取最新区块信息失败")

get_latest_block()
