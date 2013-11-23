'''
Request URL:https://amciv.lumenogic.com/amciv/jsx.json
Request Method:POST
Status Code:200 OK

jsx:[[["GQ","getById",{"id": 1}],"format",{"fmt": {"account": {"cash": true}}}],[["GQ","getById",{"id": 205}],"format",{"fmt": {"cond": {"account": {"cash": true},"otcm": {"account": {"cash": true},"hldg": {"cash": true,"order": {"user": {"idOnly": true}}},"orderbook": {"user": {"idOnly": true}},"trade": {"summary": true},"tradesSince": 1}},"otcm": {"account": {"cash": true},"hldg": {"cash": true,"order": {"user": {"idOnly": true}}},"orderbook": {"user": {"idOnly": true}},"trade": {"summary": true},"tradesSince": 1}}}],[["forum","get",{"topic": "Q.205"}],"format",{"fmt": {"post": {"login": true},"since": 1}}]]
'''

from requests import session

s = session()
s.headers['Accept'] = '*/*'
s.headers['Accept-Encoding'] = 'gzip,deflate,sdch'
s.headers['Accept-Language'] = 'en-US,en;q=0.8,fr;q=0.6,sv;q=0.4,zh;q=0.2,zh-CN;q=0.2,zh-TW;q=0.2'
s.headers['Connection'] = 'keep-alive'
s.headers['Content-Length'] = '1191'
s.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
s.headers['Host'] = 'amciv.lumenogic.com'
s.headers['Origin'] = 'https://amciv.lumenogic.com'
s.headers['Referer'] = 'https://amciv.lumenogic.com/amciv/app.html'
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'
