# Main resource was https://docs.aave.com/developers/deployed-contracts/deployed-contracts
import web3
import json
import sys

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

def get_health_factor(address, block=0):
    f = lending_pool.functions.getUserAccountData(address)
    if block == 0:
        return f.call()[-1]
    else:
        return f.call(block_identifier=block)[-1]

if __name__ == '__main__':
    address = sys.argv[1]
    block = int(sys.argv[2])
    health_factor = get_health_factor(address, block)
    print("Health factor: {}".format(health_factor))

