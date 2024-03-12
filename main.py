import random
import time
from loguru import logger
from pancakeswap.client import PancakeSwapClient
from liquidswap.client import LiquidSwapClient
from config import (
    node_url,
    DEFAULT_MAPPING,
    show_balance_before_swap,
    show_balance_after_swap,
    amount_APT_from ,
    amount_APT_to ,
    amount_USDT_from ,
    amount_USDT_to,
    loops)
from config import is_sleep, sleep_from, sleep_to, randomize_wallets, randomize_modules

def pancakeswap_swap(wallet: str, from_token: str, to_token: str, from_amount: float, to_amount: float) -> None:
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


def liquidswap_swap(wallet: str, from_token: str, to_token: str, from_amount: float, to_amount: float) -> None:
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

    modules = [liquidswap_swap, pancakeswap_swap]
    
    with open("wallets.txt", "r", encoding="utf-8-sig") as file:
        wallets = [line.strip() for line in file]

    for _ in range(loops):
        
        logger.warning("Мешаю кошельки...")
        if randomize_wallets:
            random.shuffle(wallets)
            
        for wallet in wallets:
            
            logger.warning("Мешаю модули...")
            if randomize_modules:
                random.shuffle(modules)
                
            for module in modules:
                module(wallet, "APT", "USDT", amount_APT_from, amount_APT_to)
                module(wallet, "USDT", "APT", amount_USDT_from, amount_USDT_to)
