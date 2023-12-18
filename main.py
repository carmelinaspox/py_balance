from web3 import Web3

# Enter your Ethereum wallet address
wallet_address = '0xYourWalletAddress'

# Create a provider (in this case the Infura provider is used)
infura_url = 'https://ropsten.infura.io/v3/YourInfuraApiKey'
w3 = Web3(Web3.HTTPProvider(infura_url))

# Get your wallet balance
def get_balance():
     try:
         balance_wei = w3.eth.getBalance(wallet_address)
         balance_eth = w3.fromWei(balance_wei, 'ether')
         print(f'Balance of {wallet_address}: {balance_eth} ETH')
     except Exception as e:
         print('Error:', str(e))

# Call the function to get the balance
get_balance()
