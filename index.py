#!/usr/bin/env python
import bottle

app = bottle.app()

@bottle.route('/')
def root_index():
    return "Hello World!"

if __name__=='__main__':
    bottle.debug(True)
    bottle.run(app=app, host='localhost', port=8080)
