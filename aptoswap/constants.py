# todo
MODULES_ACCOUNT = "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b"
RESOURCES_ACCOUNT = "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b"

COIN_INFO = "0x1::coin::CoinInfo"
COIN_STORE = "0x1::coin::CoinStore"

NETWORKS_MODULES = {
    "Scripts": f"{MODULES_ACCOUNT}::pool",
    "ResourceType": f"{MODULES_ACCOUNT}::pool"
}

FEE_PCT = 3
FEE_SCALE = 1000
