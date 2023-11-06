import redis
import tornado
import asyncio
import time
import json
import base64
import logging
import requests

def post_note(note):
    _url = "http://178.16.143.99:8069/create_note"
    
    try:
        _n = json.loads(note)
        requests.post(_url, json=_n)
    except Exception as e:
        print("Meet ",  e)
        return

    print("Post ", note)
    return

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    while True:
        time.sleep(1)
        note = r.lpop("notes")
        if not note:
            continue
        post_note(note)


if __name__ == "__main__":
    main()
