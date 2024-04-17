from Helper import *
from Helper.Common.utils import *


types = ['Playing', 'Streaming', 'Watching', 'Listening']
status = ['online', 'dnd', 'idle']


GAME = "Nexus Tools"
type_ = types[0] 
status = status[0] 
random_ = True  
stream_text = "discord.gg/nexustools"  


c = 0


def online(token, game, type, status):
    global c
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    l = len(tokens)
    if random_:
        type = random.choice(['Playing', 'Streaming', 'Watching', 'Listening', ''])
        status = ['online', 'dnd', 'idle']
        status = random.choice(status)

        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            game = random.choice(["Minecraft", "Badlion", "Roblox", "The Elder Scrolls: Online", "DCS World Steam Edit", ])
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            game = random.choice(["Spotify", "Deezer", "Apple Music", "YouTube", "SoundCloud", "Pandora", "Tidal", "Amazon Music", "Google Play Music", "Apple Podcasts", "iTunes", "Beatport"])
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            game = random.choice(["YouTube", "Twitch"])
            gamejson = {
                "name": game,
                "type": 3
            }
        else:
            gamejson = {
                "name": game,
                "type": 0
            }

        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.GREEN}[i] {token} is online {c}/{l}")
                ws.send(json.dumps(ack))

            except Exception as e:
                print("[!] Error: " + str(e))
                break
    else:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
        if type == "Playing":
            gamejson = {
                "name": game,
                "type": 0
            }
        elif type == 'Streaming':
            gamejson = {
                "name": game,
                "type": 1,
                "url": stream_text
            }
        elif type == "Listening":
            gamejson = {
                "name": game,
                "type": 2
            }
        elif type == "Watching":
            gamejson = {
                "name": game,
                "type": 3
            }
        else:
            gamejson = {
                "name": game,
                "type": 0
            }

        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
        }
        ws.send(json.dumps(auth))
        ack = {
            "op": 1,
            "d": None
        }
        while True:
            time.sleep(heartbeat_interval / 1000)
            try:
                c += 1
                print(f"{Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ONLINE{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}  {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}({Fore.LIGHTBLACK_EX}{c}/{l}{Style.BRIGHT}{Fore.LIGHTBLACK_EX}){Fore.RESET}")
                ws.send(json.dumps(ack))

            except Exception as e:
                print(f"{Fore.BLUE}token={Fore.WHITE}{token[:20]}...{Fore.RESET} {Fore.RESET}{Fore.LIGHTBLACK_EX}{Style.BRIGHT}[{Fore.GREEN}ERROR{Style.BRIGHT}{Fore.LIGHTBLACK_EX}]{Fore.RESET}" + str(e))
                break



def online_tokens():
    new_title("Token Onliner discord.gg/nexustools")
    threads = []
    tokens = get_tokens()
    tokens = [token.strip() for token in tokens]
    print(f"{lc} Starting...")
    for token in tokens:
        thread = threading.Thread(target=online, args=(token, GAME, type_, status))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"{ld} {Fore.GREEN}Tokens are online{Fore.RESET}")
    input("")
