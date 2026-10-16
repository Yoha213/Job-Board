import csv
import json

with open("data/currencies.csv", "r", encoding="utf-8") as csvf:
    data = list(csv.DictReader(csvf))

for currency in data:

    currency.pop("Entity")
    currency.pop("NumericCode")
    currency.pop("MinorUnit")
    currency.pop("WithdrawalDate")
    currency.update({"code":currency.get("AlphabeticCode")})
    currency.pop("AlphabeticCode")
    currency.update({"currency":currency.get("Currency")})
    currency.pop("Currency")

for currency in data.copy():

    if not currency.get("code").strip() or not currency.get("currency").strip():

        data.remove(currency)

currencies = []
currencies.append(data[0])
for c1 in data:

    if not any(c2.get("code").lower() == c1.get("code").lower() or c2.get("currency").lower() == c1.get("currency").lower() for c2 in currencies):
        currencies.append(c1)

with open("data/currencies.json", "w", encoding="utf-8") as jsonf:
    json.dump(currencies, jsonf, indent=4)