MODULES_ACCOUNT = "0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12"
RESOURCES_ACCOUNT = "0x05a97986a9d031c4567e15b797be516910cfcb4156312482efc6a19c0a30c948"
COINS_ACCOUNT = "0x43417434fd869edee76cca2a4d2301e528a1551b1d719b75c350c3c97d15b8b9"

CURVE_UNCORRELATED = f"{MODULES_ACCOUNT}::curves::Uncorrelated"
CURVE_STABLE = f"{MODULES_ACCOUNT}::curves::Stable"
COIN_INFO = "0x1::coin::CoinInfo"
COIN_STORE = "0x1::coin::CoinStore"

NETWORKS_MODULES = {
    "Scripts": f"{MODULES_ACCOUNT}::scripts_v2",
    "Faucet": f"{COINS_ACCOUNT}::faucet",
    "LiquidityPool": f"{MODULES_ACCOUNT}::liquidity_pool",
    "CoinInfo": f"{COIN_INFO}",
    "CoinStore": f"{COIN_STORE}",
}

FEE_PCT = 3
FEE_SCALE = 1000
CURVES = f"{MODULES_ACCOUNT}::curves::Uncorrelated"
