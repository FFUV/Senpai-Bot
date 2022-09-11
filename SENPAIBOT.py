from importlib.metadata import requires
import websocket
import ssl
import requests
from json import loads,dumps
nick = 'SenpaiBot'   #change this to your bot name!!!
ws = websocket.create_connection("wss://hack.chat/chat-ws",sslopt={"cert_reqs": ssl.CERT_NONE}) #1: connect
ws.send(dumps({'cmd':'join','channel':'bot','nick':nick,'pass':'<your password>'}))#2: join #change bot to the channel you want it to join  and change its pass to a good password
print('The bot is now running...') # if you want you can change this to something funni like print('Bomb has been planted')
class global_vars:
    def __init__(self):
        pass
# 
def get_json(url):
    x= requests.get(url)
    return x.json()
vars = global_vars()
while True:
    result = loads(ws.recv())   #3: receive data
    print(str(result))
    cmd = result['cmd']  # bro it doesnt let u run on the web for some reason
    if cmd == 'chat':#if someone sent a message...
        if result['nick'] == nick:continue
        msg = result['text']
        if msg == 'hello':
            ws.send(dumps({'cmd':'chat','text':'Hello! I am a bot! Now go get a life instead of talking to randos on Hack.chat'})) #change this to your custom hello message
        if msg[0] == '%':
            cmdlist = msg.split(' ')
            cmdname = cmdlist[0][1:]
            sendmsg = ''
            if cmdname == 'lookup':
                if len(cmdlist) >= 2:
                    if cmdlist[1] in vars.userinfo:
                        sendmsg = f'{cmdlist[1]}\'s information:\ntrip: {vars.userinfo[cmdlist[1]]["trip"]}\nhash: {vars.userinfo[cmdlist[1]]["hash"]}'
                    else:
                        ws.send(dumps({'cmd':'chat','text':'I have never seen this man...'}))
                else:
                    ws.send(dumps({'cmd':'chat','text':'? ? ?'}))
            elif cmdname == 'joke': 
                json_data = get_json('https://v2.jokeapi.dev/joke/Any?blacklistFlags=political,sexist') # put your own joke filters here
                if json_data['error']:
                    sendmsg = 'Oops! There is a problem with the API we are sending us stuff!!!'
                else:
                    sendmsg = json_data['setup'] + '\n' + json_data['delivery']
            elif cmdname == 'help':
                sendmsg = '%help %lookup %joke fun fact your life is a joke'
            if sendmsg != '':
                ws.send(dumps({'cmd':'chat','text':sendmsg}))
    elif cmd == 'onlineSet':
        vars.users = result['nicks']
        for i in result['users']:
            vars.userinfo = {}
            for i in result['users']:
                trip = ''
                if 'trip' not in i:
                    trip = '(null)'
                else:
                    trip = i['trip']
                vars.userinfo.update({i['nick']:{'hash':i['hash'],'trip':trip}})
        print('Users online: '+str(vars.users)+'\nPower by UwU senpai arigato!')
    elif cmd == 'onlineAdd':
        vars.users.append(result['nick'])
        if result['nick'] not in vars.userinfo:
            trip = ''
            if 'trip' not in i:
                trip = '(null)'
            else:
                trip = i['trip']
            vars.userinfo.update({result['nick']:{'hash':result['hash'],'trip':trip}})
        ws.send(dumps({'cmd':'whisper','nick':result['nick'],'text':'Hey guy, I am a bot, you can send \"%help\" to get my help information'}))
    elif cmd == 'onlineRemove':
        if result['nick'] in vars.users:vars.users.remove(result['nick'])
        if result['nick'] in vars.userinfo:
            del vars.userinfo[result['nick']]
