import tornado
import asyncio
import time
import json

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
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
