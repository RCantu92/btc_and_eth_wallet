# RivCo Wallet: Wallet for BTC-Testnet & ETH-Testnet:

![](https://coindoo.com/wp-content/uploads/2019/09/secure_cryptocurrency_wallet.png)

## Description

What is it? What does it do?:

RivCo is now providing a cryptocurrency wallet service. What RivCo's wallet does is it generates private keys upon command. After generating private keys, the keys are then used to derive accounts with addresses, with which users are then able to transact with.

Below is an image of a valie BTC-testnet transaction.

![](./screenshots/btc-testnet-tx-confirmation.png)

The code to run the transaction above is as follows:

> send_tx(BTCTEST, btc_accounts["account_01"], btc_accounts["account_02"], 0.00003)

Below is an image of a valid ETH-testnet transaction.

![](./screenshots/eth-testnet-tx-confirmation.png)

What is it built with?:

What happens behind the scenes to help RivCo's wallet function is as follows: First, with python, the subprocess library is used to run hd-wallet-derive to derive private keys for both BTC and ETH testnets. Once the private keys have been generated, they are used to create accounts for the BTC and ETH testnets using the bit and web3 libraries for python.

How do you use it?:

You simply run the .py file from the command line using python.