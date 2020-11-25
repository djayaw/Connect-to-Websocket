import requests
import json
import asyncio
import websockets

from tkinter import *
from PIL import ImageTk, Image

#Login Data
payload ={
    'email': 'desktopapplication@hunterboe.com',
    'password': 'Demo1!',
    'remember': True,
}

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        load = Image.open("911inform.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


with requests.Session() as s:
    url = 'https://qa.911inform.com/'
    r = s.post(url+'login', data = payload)
    content = json.loads(r.content)
    token = content["token"]
    while True:
        async def hello():
            uri = ("wss://qa.911inform.com/?access_token="+token)
            async with websockets.connect(uri) as websocket:
                test = await websocket.recv()
                cnt = json.loads(test)
                check = cnt["method"]
                check2 = cnt["params"]
                print(check2)
                Building = check2["buildingName"]
                Type = check2["type"]
                print(Building)
                print(Type)
                if (check == "notifications.created"):
                    print("NEW NOTIFICATION BTW")
                    root = Tk()
                    app = Window(root)
                    label_1 = Label(root,
                                    text = Building,
                                    font="Times 32",
                                    width =20,
                                    height=0,
                                    anchor = NE)
                    label_2 = Label(root,
                                    text = Type,
                                    font="Times 32",
                                    width =20,
                                    height=0,
                                    anchor = NE)
                    label_1.pack()
                    label_2.pack()
                    root.attributes('-fullscreen', True)
                    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
                    root.mainloop()
                print("<<<<<<<<<<<<<<<--------------------->>>>>>>>>>>>>>>>>>")
        asyncio.get_event_loop().run_until_complete(hello())
