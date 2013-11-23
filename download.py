#!/usr/bin/env python3
from hashlib import sha512
import os
import json
import datetime
import time

from requests import session

def cache(key, age = datetime.timedelta(hours = 1)):
    def wrap1(func):
        def wrap2(*args, **kwargs):
            if not os.path.exists('data'):
                os.mkdir('data')

            fn = os.path.join('data',key)

            if (not os.path.exists(fn)) or datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(fn)) > age:
                f = open(fn, 'w')
                value = func(*args, **kwargs)
                f.write(value)
            else:
                f = open(fn, 'r')
                value = f.read()
                f.close()

            return value
        return wrap2
    return wrap1

class Jsx:
    url = 'https://amciv.lumenogic.com/amciv/jsx.json'
    def __init__(self, login = 'guest', password = 'american'):
        s = session()
        s.headers['Accept'] = '*/*'
        s.headers['Accept-Encoding'] = 'gzip,deflate,sdch'
        s.headers['Accept-Language'] = 'en-US,en;q=0.8,fr;q=0.6,sv;q=0.4,zh;q=0.2,zh-CN;q=0.2,zh-TW;q=0.2'
        s.headers['Connection'] = 'keep-alive'
        s.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        s.headers['Host'] = 'amciv.lumenogic.com'
        s.headers['Origin'] = 'https://amciv.lumenogic.com'
        s.headers['Referer'] = 'https://amciv.lumenogic.com/amciv/app.html'
        s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'

        r = s.get('https://amciv.lumenogic.com/amciv/app.html')

        r = s.post(self.url, data = {
            'jsx':json.dumps([["registrar","login",{"login": login,"authKey": sha512(password).hexdigest()}]])
        })
        s.cookies.set('lumAuth',json.loads(r.text)[0])
        self.session = s
    def lookup(self, question_number):
        r = self.session.post(self.url, data = {
            'jsx':json.dumps([
 #              [["GQ","getById",{"id": 1}],"format",{"fmt": {"account": {"cash": True}}}],
                [
                    ["GQ","getById",{"id": question_number}],
                    "format",
                    {"fmt": {
                        "cond": {
                            "account": {"cash": True},
                            "otcm": {
                                "account": {"cash": True},
                                "hldg": {"cash": True,"order": {"user": {"idOnly": True}}},
                                "orderbook": {"user": {"idOnly": True}},
                                "trade": {"summary": True},"tradesSince": 1}
                            },
                        "otcm": {
                            "account": {"cash": True},
                            "hldg": {"cash": True,"order": {"user": {"idOnly": True}}},
                            "orderbook": {"user": {"idOnly": True}},
                            "trade": {"summary": True},"tradesSince": 1}
                        }
                    }
                ],
 #              [["forum","get",{"topic": "Q.%d" % question_number}],"format",{"fmt": {"post": {"login": True},"since": 1}}]
              ])
            }
        )
        return r.text

# jsx = Jsx('guest','american')
# r = jsx.lookup(205)
