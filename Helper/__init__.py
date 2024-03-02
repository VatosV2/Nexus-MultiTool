__title__ = 'Nexus'
__author__ = 'Vatos'
__copyright__ = 'discord.gg/nexustools'
__version__ = '1.0.0'

import os
import time
import threading
import requests
import concurrent.futures
import json
import urllib.request
import socket
import base64 
import codecs
import random
import string

from faker import Faker
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from datetime import datetime

from .Funcs.token_checker import Token_checker
from .Funcs.token_formater import formater
from .Funcs.token_sorter import sort_tokens
from .Funcs.remove_doubles import remove_duplicates
from .Funcs.token_guild_check import check_tokens_guild
from .Funcs.token_guild_leaver import token_leave_server
from .Funcs.token_spammer import token_spammer
from .Funcs.proxy_scraper import Proxy_scraper
from .Funcs.proxy_checker import check_proxys
from .Funcs.obf import obfuscate
from .Funcs.webhook_tool import Webhook_tool
from .Funcs.faker import main_faker
from .Funcs.start import StartupTool
from .Funcs.clear_output import clear_output

banner = f'''{Fore.LIGHTMAGENTA_EX}
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    '''

def discord():
    os.system("start https://discord.gg/nexustools")
    print("Opend Link!")
    time.sleep(1)