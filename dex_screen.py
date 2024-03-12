import requests
import json

# chain is a string that is the ticket of the chain built on, example: 'bsc'
# address is the token_address you want to see, example: '0x7213a321F1855CF1779f42c0CD85d3D95291D34C'
def dex_screen(chain, address):
    main_request = "https://api.dexscreener.com/latest/dex/pairs/"
    chain_id = "/" + chain
    token_address = "/" + address
    response = requests.get("https://api.dexscreener.io/latest/dex/pairs/" + chain_id + token_address)
    print(response.text)
    data_dict = json.loads(response.text)
    print(data_dict)


if __name__ == "__main__":
    dex_screen('bsc', '0x7213a321F1855CF1779f42c0CD85d3D95291D34C')
    # dex_screen("sol", "")