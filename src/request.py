import requests
import json

from dataclasses import dataclass

@dataclass
class CoinData:
    name:str
    currentPrice:float
    dayChange:float
    capitalisation:float
    dayVolume:float
    dayVolumeChange:float

def get_data(url:str)->CoinData:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            parsedData = CoinData(
                name=f"{data['name']} ({data['symbol']})",
                currentPrice=round(data['quotes']['USD']['price'], 6),
                dayChange=round(data['quotes']['USD']['percent_change_24h'], 6),
                capitalisation=round(data['quotes']['USD']['market_cap'], 6),
                dayVolume=round(data['quotes']['USD']['volume_24h'], 6),
                dayVolumeChange=round(data['quotes']['USD']['volume_24h_change_24h'], 6),
            )
            return parsedData
        else:
            print(f"Request error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête: {e}")
        return None
    except json.JSONDecodeError:
        print("Erreur lors de la conversion des données JSON")
        return None
    except KeyError as e:
        print(f"Clé manquante dans les données: {e}")
        return None