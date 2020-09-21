import requests
import json
import asyncio
import websockets

#Login Data
payload ={
    'email': 'sample email',
    'password': 'sample password',
    'remember': True,
}

with requests.Session() as s:
    url = 'sample url'
    r = s.post(url+'login', data = payload)
    content = json.loads(r.content)
    token = content["token"]
    while True:
        async def running():
            uri = ("wss://"+url+"?access_token="+token)
            async with websockets.connect(uri) as websocket:
                test = await websocket.recv()
                cnt = json.loads(test)
                print(cnt)

        asyncio.get_event_loop().run_until_complete(running())

