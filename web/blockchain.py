from web3 import Web3
import config
import json

web3 = Web3(Web3.HTTPProvider(config.url))

def connect_blockchain():
    web3 = Web3(Web3.HTTPProvider(config.url))
    chain_id = web3.eth.chainId
    return (web3, chain_id)

def load_contract():
    with open('abi.json') as f:
        abi = json.load(f)
    contract = web3.eth.contract(address=config.contract_address, abi=abi)
    return(contract)

def connection_status():
    print("Web3 Connection:",web3.isConnected())

def create_account():
    account=web3.eth.account.create()
    key=account.encrypt(config.key)
    return(account.address,key)

def account_balance(address):
    bal=web3.eth.getBalance(address)
    balance=web3.fromWei(balance,'ether')
    return(balance)

def decrpyt(key):
    private_key=web3.eth.account.decrypt(key,config.key)
    return(private_key)

def load_account(key):
    private_key=web3.eth.account.decrypt(key,config.key)
    account=web3.eth.account.privateKeyToAccount(private_key)
    return(account)

def send_ether(address):
    account=web3.eth.account.privateKeyToAccount(config.main_account_key)
    trxn={
        'nonce':web3.eth.getTransactionCount(account.address),
        'gas':700000,
        'gasPrice':web3.toWei('10','gwei'),
        'to':address,
        'value':500000000000000000,
    }
    singed_trn = web3.eth.account.sign_transaction(trxn, private_key=account.privateKey)
    return(web3.eth.sendRawTransaction(singed_trn.rawTransaction))

def is_mined(txn_hash):
    web3.eth.waitForTransactionReceipt(txn_hash)

