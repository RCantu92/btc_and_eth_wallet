# RivCo Wallet: Wallet for BTC-Testnet & ETH-Testnet:

![](https://coindoo.com/wp-content/uploads/2019/09/secure_cryptocurrency_wallet.png)

## Description

What is it? What does it do?:

RivCo is now providing a cryptocurrency wallet service. What RivCo's wallet does is it generates accounts from private keys, with which users are then able to transact with upon command. 

(As it stands, there have been three private keys for both BTC-testnet and ETH-testnet that have been derived. To derive more than three in the future, the "--numderive=" flag could be filled in with a number greater than 3.)

Below is an image of a valie BTC-testnet transaction.

![](./screenshots/btc-testnet-tx-confirmation.png)

The code to run the transaction above is as follows:

> send_tx(BTCTEST, btc_accounts["account_01"], btc_accounts["account_02"], 0.00003)

(The code in that above instance could be altered to have transactions occur with different accounts. for example "account_02" and "account_03".)

Below is an image of a valid ETH-testnet transaction.

![](./screenshots/eth-testnet-tx-confirmation.png)

The code to run the transaction above is as follows:

> send_tx(ETH, eth_accounts["account_01"], eth_accounts["account_02"], 200000000000000s)

(The code in that above instance could be altered to have transactions occur with different accounts. for example "account_02" and "account_03".)

What is it built with?:

What happens behind the scenes to help RivCo's wallet function is as follows: First, with python, the subprocess library is used to run hd-wallet-derive to derive private keys for both BTC and ETH testnets. Once the private keys have been generated, they are used to create accounts for the BTC and ETH testnets using the bit and web3 libraries for python.

How do you use it?:

You simply run the .py file from the command line using python.