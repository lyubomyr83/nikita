import currency_exchange
from translate import Translator

# список всех валют
all_currencies = currency_exchange.currencies()
# установим язык для переводдов
translator= Translator(to_lang="ru")


translated_currencies = {}  # пустой словарь

for currency in all_currencies:
    code_name = currency.split(' - ')
    translation = translator.translate(code_name[1])
    translated_currencies[translation] = code_name[0]

print(translated_currencies)
# print(currency_exchange.exchange("EUR", "RUB", 100))