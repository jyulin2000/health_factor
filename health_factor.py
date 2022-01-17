# Main resource was https://docs.aave.com/developers/deployed-contracts/deployed-contracts
import web3
import json

endpoint = 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'
w3 = web3.Web3(web3.Web3.HTTPProvider(endpoint))

def get_contract(address, abi_file):
    with open(abi_file) as f:
        abi = json.loads(f.read())

    contract = w3.eth.contract(address, abi=abi)
    return contract

lending_pool_address = '0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9'
lending_pool_abi = 'lending_pool_abi'
lending_pool = get_contract(lending_pool_address, lending_pool_abi)

wintermute1 = '0x0000006daea1723962647b7e189d311d757Fb793'

user_address = wintermute1
block = 13532886

def get_health_factor(address, block=0):
    f = lending_pool.functions.getUserAccountData(address)
    if block == 0:
        return f.call()[-1]
    else:
        return f.call(block_identifier=block)[-1]

user_address = '0xb3aba44B58F3a1E82b91D7264492Ea8E778C3BA6'
block = 14025797
print("Health of address {} at block {}: {}".format(user_address, block, get_health_factor(user_address, block)))


