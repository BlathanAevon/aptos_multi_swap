import random
import time
from loguru import logger
from aptoswap.client import AptoSwap
from pancakeswap.client import PancakeSwapClient
from liquidswap.client import LiquidSwapClient
from config import (
    node_url,
    APTOSWAP_MAPPING,
    DEFAULT_MAPPING,
    show_balance_before_swap,
    show_balance_after_swap,
)
from config import is_sleep, sleep_from, sleep_to, randomize_wallets, randomize_modules


# TOKENS: USDT, APT
def pancakeswap_swap(wallet, from_token, to_token, from_amount, to_amount):
    pancakeswap_client = PancakeSwapClient(node_url, DEFAULT_MAPPING, wallet)
    pancakeswap_client.client_config.max_gas_amount = 5_000

    amount = round(random.uniform(from_amount, to_amount), 2)

    try:
        if show_balance_before_swap:
            logger.info(
                f"Баланс {from_token}: {pancakeswap_client.get_token_balance(from_token)}; "
                f"Баланс {to_token}: {pancakeswap_client.get_token_balance(to_token)}"
            )

        coins_in = pancakeswap_client.calculate_rates(from_token, to_token, amount)
        coins_out = pancakeswap_client.calculate_rates(to_token, from_token, coins_in)

        logger.warning(
            f"Попытка свапнуть {coins_out} {from_token} в {coins_in} {to_token}"
        )
        pancakeswap_client.swap(from_token, to_token, amount, coins_in)

        if show_balance_after_swap:
            logger.info(
                f"Баланс {from_token}: {pancakeswap_client.get_token_balance(from_token)}; "
                f"Баланс {to_token}: {pancakeswap_client.get_token_balance(to_token)}"
            )

        if is_sleep:
            wait_time_in_sec = random.randint(sleep_from, sleep_to)
            logger.warning(f"Ждем {wait_time_in_sec} секунд")
            time.sleep(wait_time_in_sec)
    except Exception:
        logger.error(f"Непредвиденная ошибка")


# TOKENS: USDT, APT
def liquidswap_swap(wallet, from_token, to_token, from_amount, to_amount):
    liquidswap_client = LiquidSwapClient(node_url, DEFAULT_MAPPING, wallet)
    liquidswap_client.client_config.max_gas_amount = 5_000

    amount = round(random.uniform(from_amount, to_amount), 2)

    try:
        if show_balance_before_swap:
            logger.info(
                f"Баланс {from_token}: {liquidswap_client.get_token_balance(from_token)}; "
                f"Баланс {to_token}: {liquidswap_client.get_token_balance(to_token)}"
            )

        coins_in = liquidswap_client.calculate_rates(from_token, to_token, amount)
        coins_out = liquidswap_client.calculate_rates(to_token, from_token, coins_in)

        logger.warning(
            f"Попытка свапнуть {coins_out} {from_token} в {coins_in} {to_token}"
        )
        liquidswap_client.swap(from_token, to_token, amount, coins_in)

        if show_balance_after_swap:
            logger.info(
                f"Баланс {from_token}: {liquidswap_client.get_token_balance(from_token)}; "
                f"Баланс {to_token}: {liquidswap_client.get_token_balance(to_token)}"
            )

        if is_sleep:
            wait_time_in_sec = random.randint(sleep_from, sleep_to)
            logger.warning(f"Ждем {wait_time_in_sec} секунд")
            time.sleep(wait_time_in_sec)
    except Exception:
        logger.error(f"Непредвиденная ошибка")


if __name__ == "__main__":
    # Можно убрать какой-то из модулей по-желанию
    modules = [liquidswap_swap, pancakeswap_swap, aptoswap_swap]
    # Кол-во прогонов всех кошельков по модулям где кол-во транз = 1 прогон * 3 модуля т.е 50 прогонов = 150 транз на каждом кошельке
    loops = 50

    with open("wallets.txt", "r", encoding="utf-8-sig") as file:
        wallets = [line.strip() for line in file]

    if randomize_wallets:
        random.shuffle(wallets)

    if randomize_modules:
        random.shuffle(modules)

    for _ in range(loops):
        for wallet in wallets:
            for module in modules:
                module(wallet, "APT", "USDT", 0.01, 0.011)
                module(wallet, "USDT", "APT", 0.06, 0.065)
