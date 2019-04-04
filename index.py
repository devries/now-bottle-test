#!/usr/bin/env python
import bottle
import os

app = bottle.app()

@bottle.route('/')
def root_index():
    region = os.environ.get('NOW_REGION', 'unknown')
    return bottle.template('index', region = region)

if __name__=='__main__':
    bottle.debug(True)
    bottle.run(app=app, host='localhost', port=5000)
