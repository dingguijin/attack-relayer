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

_id = 0
class MainHandler(tornado.web.RequestHandler):


    def get(self):
        print("Ignore Get", self.request)
        global _id
        _id += 1
        _r = {"id":_id,"jsonrpc":"2.0","result":"0x1"}
        self.write(json.dumps(_r))

    def post(self):
        print(self.request.body)
        try:
            x = json.loads(self.request.body)
            if x:
                _nice = x.get("__nice") or {}
                _n = _nice.get("n")
                if _n:
                    _rev = reverse_string(_n)
                    print(_rev)
                    x["time"] = time.time()
                    _nice["n"] = _rev
                    self.application.redis.rpush('notes', json.dumps(x))
        except Exception as e:
            print("Meet ", e)

        with open("note-%s-note" % time.time(), "wb") as _f:
            _f.write(self.request.body)
        global _id
        _id += 1
        _r = {"id":_id,"jsonrpc":"2.0","result":"0x1"}
        self.write(json.dumps(_r))

def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])

async def main():
    app = make_app()
    app.redis = redis.Redis(host='localhost', port=6379, db=0)
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
