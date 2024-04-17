from Helper import *
from Helper.Common.utils import *

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    while True:
        time.sleep(interval)
        heartbeatJson = {
            "op": 1,
            "d": 'null'
        }
        send_json_request(ws, heartbeatJson)

def handle_events(ws):
    print("Logging messages!")
    while True:
        try:
            event = receive_json_response(ws)
            if event is not None and isinstance(event, dict):
                username = event.get('d', {}).get('author', {}).get('username')
                content = event.get('d', {}).get('content')
                server = event.get('d', {}).get('guild_id')  
                if username and content:
                    if server:  
                        print(f"[Server: {server}]: {username}: {content}")
                    else: 
                        print(f"[DM]: {username}: {content}")
                op_code = event.get('op')
                if op_code == 11:
                    print('Heartbeat received')
            else:
                print("Received invalid event:", event)
        except:
            pass


def message_logger():
    new_title("Discord Message Logger discord.gg/nexustools")
    token = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Token: ")
    try:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')

        event = receive_json_response(ws)
        heartbeat_interval = event['d']['heartbeat_interval']

        threading.Thread(target=heartbeat, args=(heartbeat_interval / 1000, ws)).start()
        threading.Thread(target=handle_events, args=(ws,)).start()

        payload = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": "windows",
                    "$browser": "chrome",
                    "$device": 'pc'
                }
            }
        }
        send_json_request(ws, payload)

    except Exception as e:
        print(f"Error: {e}")
