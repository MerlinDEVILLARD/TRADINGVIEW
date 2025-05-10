from request import get_data

if __name__ == "__main__":
    get_data('https://api.coinpaprika.com/v1/tickers/sol-solana')
    get_data('https://api.coinpaprika.com/v1/tickers/eth-ethereum')
    get_data('https://api.coinpaprika.com/v1/tickers/link-chainlink')
    # get_data('')
    # get_data('')
    # get_data('')
    
    # if solana_data:
    #     save_option = input("Voulez-vous sauvegarder les données brutes dans un fichier JSON? (o/n): ")
    #     if save_option.lower() == 'o':
    #         with open('solana_data.json', 'w') as f:
    #             json.dump(solana_data, f, indent=4)
    #             print("Données sauvegardées dans solana_data.json")