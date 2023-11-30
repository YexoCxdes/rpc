from pypresence import Presence
import psutil
import time
from datetime import datetime

time1 = datetime.now().strftime("%H:%M")

client_id = 1143916261865164870
RPC = Presence(client_id)  # Initialize the client class
data = None
img = None
RPC.connect() # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    for proc in psutil.process_iter():
        match proc.name().lower():
            case "clipchamp.exe":
                img = 'https://th.bing.com/th/id/OIP.j8hlWr1Mb4PBWy0qRkEnsQAAAA?w=120&h=120&c=7&r=0&o=5&pid=1.7'
                data = 'Editing a video'
                print('Clipchamp Detected.')
                break
            case "code.exe":
                img = 'https://cdn-1.webcatalog.io/catalog/vs-code/vs-code-icon-filled-256.png?v=1675612398960'
                data = 'Coding'
                print('Visual Studio Code Detected.')
                break
            case "spotify.exe":
                img = 'https://th.bing.com/th?id=OIP.Z5U069MFYVWvJPvCI8PAtwHaHa&w=250&h=250&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2'
                data = 'Listening to music'
                print('Spotify Detected.')
                break
            case _:
                data = None
                img = None
    cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    RPC.update(details="RAM: "+str(mem_per)+"%", state="CPU: "+str(cpu_per)+"%", buttons=[{"label": "Website", "url": "https://e-z.bio/Yexo"}, {"label": "Server", "url": "https://discord.gg/gYsG6fSHCv"}], large_image='https://r2.e-z.host/3f3990ac-a41f-4698-8ac7-e559321f513e/pv19d67o.png', large_text=f'My time = {time1}', small_image=img, small_text=data)  # Set the presence
    print(f'Updated ( CPU = {cpu_per}% RAM = {mem_per}% )')
    time.sleep(15) # Can only update rich presence every 15 seconds