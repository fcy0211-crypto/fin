import requests
from bs4 import BeautifulSoup

URL = "https://bii.by/currency"

def get_rates():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except:
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # ищем все строки с валютами
    rows = soup.select("table tbody tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue

        currency = cols[0].get_text(strip=True)

        # фильтр — только реальные валюты
        if currency not in ["USD", "EUR", "RUB"]:
            continue

        buy = cols[1].get_text(strip=True)
        sell = cols[2].get_text(strip=True)

        # ТОЛЬКО курсы (никакой рекламы, текста и т.д.)
        print(f"{currency} {buy} {sell}")

if __name__ == "__main__":
    get_rates()