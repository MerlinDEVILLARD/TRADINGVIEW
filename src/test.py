import pandas as pd
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def create_data(name: str):
    cg = CoinGeckoAPI()

    prices = cg.get_price(ids=[name], vs_currencies='eur')
    print(f"{name.capitalize()}: {prices}")

    history = cg.get_coin_market_chart_by_id(id=name, vs_currency='eur', days=90)

    df = pd.DataFrame(history['prices'], columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

    return df

def plot_all_cryptos():
    cryptos = ["bitcoin", "solana", "ethereum"]
    fig = plt.figure(figsize=(15, 12))
    gs = GridSpec(3, 2, figure=fig)
    colors = ['#FF9500', '#2E9AFE', '#41D98D', '#627EEA', '#E6007A', '#C2A633']

    for i, crypto in enumerate(cryptos):
        try:
            row = i // 2
            col = i % 2

            ax = fig.add_subplot(gs[row, col])

            df = create_data(crypto)
            ax.plot(df['date'], df['price'], linewidth=2, color=colors[i])

            ax.set_title(f'Prix de {crypto.capitalize()} (90 jours)', fontweight='bold')
            ax.set_xlabel('Date')
            ax.set_ylabel('Prix (EUR)')
            ax.grid(alpha=0.3)

            ax.get_yaxis().set_major_formatter(
                plt.FuncFormatter(lambda x, loc: "{:,}".format(x).replace(',', ' ')))

        except Exception as e:
            print(f"Erreur avec {crypto}: {e}")

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.35)

    fig.suptitle('Comparaison des prix des cryptomonnaies sur 90 jours', 
                 fontsize=16, fontweight='bold', y=0.98)

    plt.show()

if __name__ == "__main__":
    plot_all_cryptos()