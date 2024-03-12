import requests
import json

main_request = "https://api.dexscreener.com/latest/dex/pairs/"
chaid_id = "/" + ""
token_adress = "/" + ""

def dex_screen():
    response = requests.get("https://api.dexscreener.io/latest/dex/pairs/bsc/0x7213a321F1855CF1779f42c0CD85d3D95291D34C")
    print(response.text)
    data_dict = json.loads(response.text)
    print(data_dict)


if __name__ == "__main__":
    dex_screen()
    
