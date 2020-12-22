from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
cr = c.get_rates('USD')

print(cr)
