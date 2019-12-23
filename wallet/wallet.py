from constants import *
import subprocess
import json
from web3 import Web3
from bit import PrivateKeyTestnet
import bit
from eth_account import Account

# Establish connection with Ethereum node
conn = Web3.HTTPProvider("http://127.0.0.1:8545")
w3 = Web3(conn)

def derive_wallets(coin):
    '''
    Function to derive wallets from hd-wallet-derive
    for either BTC-Testnet or ETH.
    The mnemonic words are imported from an
    external file, constants.py.
    '''
    if (coin == BTCTEST):
        '''
        Use the subprocess library to derive a wallet for
        BTC Testnet and return the output as a JSON object.
        '''
        output_01 = subprocess.run(['./derive','-g', f'--mnemonic={mnemonic}', f'--coin={BTCTEST}', '--numderive=3', '--format=json'], text=True, capture_output=True)
        return(json.loads(output_01.stdout))
    elif (coin == ETH):
        '''
        Use the subprocess library to derive a wallet for
        ETH and return the output as a JSON object.
        '''
        output_02 = subprocess.run(['./derive','-g', f'--mnemonic={mnemonic}', f'--coin={ETH}', '--numderive=3', '--format=json'], text=True, capture_output=True)
        return(json.loads(output_02.stdout))


'''
Creating a Coins dictionary to store
the wallets as a key-value pair with
the cryptocurrency name as a string.
'''
Coins = {
    "btc-test" : derive_wallets(BTCTEST),
    "eth" : derive_wallets(ETH)
}

'''
Creating crypto privkeys dictionaries
to store both BTC-Test and ETH private keys.
'''
btc_privkeys = {
    "privkey_01": Coins['btc-test'][0]['privkey'],
    "privkey_02": Coins['btc-test'][1]['privkey'],
    "privkey_03": Coins['btc-test'][2]['privkey']
}

eth_privkeys = {
    "privkey_01": Coins['eth'][0]['privkey'],
    "privkey_02": Coins['eth'][1]['privkey'],
    "privkey_03": Coins['eth'][2]['privkey']
}

def priv_key_to_account(coin, priv_key):
    '''
    Function to create accounts from private keys
    for either BTC-Testnet or ETH.
    '''
    if (coin == BTCTEST):
        '''
        This will convert the BTC Test privkey string
        to an account object that bit can use to transact.
        '''
        btctest_account = PrivateKeyTestnet(priv_key)
        return(btctest_account)
    elif (coin == ETH):
        '''
        This will convert the ETH privkey string to
        an account object that web3.py can use to transact.
        '''
        eth_account = Account.privateKeyToAccount(priv_key)
        return(eth_account)

'''
Creating crypto account dictionaries
to store both BTC-Test and ETH accounts.
'''
btc_accounts = {
    "account_01": priv_key_to_account(BTCTEST, btc_privkeys["privkey_01"]),
    "account_02": priv_key_to_account(BTCTEST, btc_privkeys["privkey_02"]),
    "account_03": priv_key_to_account(BTCTEST, btc_privkeys["privkey_03"])
}

eth_accounts = {
    "account_01": priv_key_to_account(ETH, eth_privkeys["privkey_01"]),
    "account_02": priv_key_to_account(ETH, eth_privkeys["privkey_02"]),
    "account_03": priv_key_to_account(ETH, eth_privkeys["privkey_03"])
}

def create_tx(coin, account, to, amount):
    '''
    Function to create transacations between
    accounts for either BTC-Testnet or ETH.
    '''
    if (coin == BTCTEST):
        '''
        This will create the transaction between
        accounts on the BTC-Testnet.
        '''
        btc_tx = PrivateKeyTestnet.prepare_transaction(account.address, [(to.address, amount, BTC)])
        return(btc_tx)
    elif (coin == ETH):
        '''
        This will create the transaction
        between accounts on ETH.
        '''
        gas_estimate = w3.eth.estimateGas(
            {
                "from": account.address,
                "to": to,
                "value": amount
            }
        )
        return({
            "to": to,
            "from": account.address,
            "value": amount,
            "gas": gas_estimate,
            "gas_price": w3.eth.gasPrice,
            "nonce":w3.eth.getTransactionCount(account.address),
            "chain_id": web3.eth.chainId
        })

def send_tx(coin, account, to, amount):
    '''
    This function will send transactions between
    accounts on either BTC-Testnet or ETH. It will
    call the create_tx() function.
    '''
    if (coin == BTCTEST):
        '''
        This will send the transaction between
        accounts on the BTC-Testnet.
        '''
        tx_data = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(tx_data)
        result = bit.network.NetworkAPI.broadcast_tx_testnet(signed_tx)
        return(result)
    elif (coin == ETH):
        '''
        This will send the transaction
        between accounts on ETH.
        '''
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)
        result = w3.eth.sendRawTransaction(signed.rawTransaction)
        return(result.hex())

# Following code to execute the
# transaction on BTC Testnet

print(send_tx(BTCTEST, btc_accounts["account_01"], btc_accounts["account_02"], 0.00003))