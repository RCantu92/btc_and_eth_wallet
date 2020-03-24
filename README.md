# Local Wallet Generator for BTC-Testnet & ETH-Testnet:

What this project does is that it generates accounts from private keys, with which users are then able to transact with upon command.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

### Installing

Getting a local copy of hd-wallet-derive on your machine.

```
Go to https://github.com/dan-da/hd-wallet-derive and clone the repository. 
```

## Running the tests

You simply run the .py file from the command line using python.

### Break down into end to end tests

Below is an image of a valie BTC-testnet transaction.

![](./screenshots/btc-testnet-tx-confirmation.png)

The code to run the transaction above is as follows:

```
send_tx(BTCTEST, btc_accounts["account_01"], btc_accounts["account_02"], 0.00003)
```

(The code in that above instance could be altered to have transactions occur with different accounts. for example "account_02" and "account_03".)

Below is an image of a valid ETH-testnet transaction.

![](./screenshots/eth-testnet-tx-confirmation.png)

The code to run the transaction above is as follows:

```
send_tx(ETH, eth_accounts["account_01"], eth_accounts["account_02"], 200000000000000s)
```

(The code in that above instance could be altered to have transactions occur with different accounts. for example "account_02" and "account_03".)

## Built With

* [python](https://www.python.org/) - Programming language.
* [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive) - CLI tool that derives bip32 addresses and private keys.
* [Bit](https://ofek.dev/bit/) - Python Bitcoin library.
* [web3.py](https://github.com/ethereum/web3.py) - Python Ethereum library.

## Authors

* **Roberto Cantu**  - [GitHub](https://github.com/RCantu92)