# Hack.chat bot
A hack.chat bot is a bot made for hack.chat that goes to different servers the commands on this bot will be shown when you do %help (special thanks to MrZhang365 for teaching me how to make bots)
This project just uses a few simple websocket-client protocols using a html library using requests !  ( btw if your wondering yes we did use jokeapi stay mad >:) )    [![CodeFactor](https://www.codefactor.io/repository/github/ttrmaniac/senpai-bot/badge)](https://www.codefactor.io/repository/github/ttrmaniac/senpai-bot)
oh and yes this can be used as a template as long as you give me credits



## Installation

Use the package manager [pip](https://pypi.org/project/websocket-client/) and [this](https://pypi.org/project/websocket/) oh and also last one [here](https://pypi.org/project/requests/) to download

```bash
pip install requests
```
```bash
pip install websocket-client
```
```bash
pip install websocket
```

## Usage

```python
from importlib.metadata import requires
import websocket
import ssl
import requests
from json import loads,dumps
nick = 'SenpaiBot'   #change this!!!
ws = websocket.create_connection("wss://hack.chat/chat-ws",sslopt={"cert_reqs": ssl.CERT_NONE}) #1: connect
ws.send(dumps({'cmd':'join','channel':'bot','nick':nick,'pass':'<your password>'}))#2: join
print('The bot is now running...')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
