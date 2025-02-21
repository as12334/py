import httpx
from solana.rpc.api import Client

# 连接到 Solana RPC 端点
rpc_url = "https://api.mainnet-beta.solana.com"
client = Client(rpc_url)

# 获取最新区块哈希
latest_blockhash = client.get_recent_blockhash()

# 获取最新区块的详细信息
block_info = client.get_block(latest_blockhash["result"]["value"]["blockhash"])

# 打印区块信息
print(block_info)
