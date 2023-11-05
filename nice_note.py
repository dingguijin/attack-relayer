import tornado
import asyncio
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Nice")

    def post(self):
        print(self.request.body)
        with open("note-%s-note" % time.time()) as _f:
            _f.write(self.request.body)
        self.write(json.dumps({"success":True}))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
