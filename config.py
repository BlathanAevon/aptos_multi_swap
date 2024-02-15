node_url = "https://rpc.ankr.com/http/aptos/v1"


 
APTOSWAP_MAPPING = {
    "APT": "0x1::aptos_coin::AptosCoin",
    "USDT": "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
    "USDC": "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
}

DEFAULT_MAPPING = {
    "APT": "0x1::aptos_coin::AptosCoin",
    "USDT": "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT"
}


# Если хотите, чтобы в логах был баланс до свапа ставьте True, если нет, то False
show_balance_before_swap = True
# Если хотите, чтобы в логах был баланс после свапа ставьте True, если нет, то False
show_balance_after_swap = True
# Если хотите рандомизировать кошельки, то ставьте True, если нет, то False
randomize_wallets = True
# Если хотите делать паузы между кошельками, то ставьте True, если нет, то False
is_sleep = True
# Если хотите рандомизировать модули
randomize_modules = True
# Количество секунд паузы между кошельками
sleep_from = 20
sleep_to = 50
loops = 20

# Кол-во от/до для свапа из Aptos в USDT
amount_APT_from = 0.005
amount_APT_to = 0.0051
# Кол-во от/до для свапа из USDT в APT
amount_USDT_from = 0.06
amount_USDT_to = 0.07


