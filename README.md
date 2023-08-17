# aptos-aptoswap-swap

Скрипт для свапов в сети Aptos с использованием DEX AptoSwap

В пулах мало ликвидности, могут быть ошибки и большие потери на свапах. **Лучше этот dex не юзать**, 
максимум 1-2 свапа для +1 контракта на кошелек

#### Установка зависимостей: ```pip install -r requirements.txt```

- `wallet.txt` для ввода приватников
- `config.py`  дефолтные настройки, также можно настроить время ожидания между кошельками, включить рандомизацию кошельков
- `tokens_mapping` в `config.py` используется для мапинга токенов (если вам надо какой-то еще, то просто добавьте
  удобное для вас название и адрес нового токена)

