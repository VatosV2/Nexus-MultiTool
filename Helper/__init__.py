__title__ = 'Nexus'
__author__ = 'Vatos'
__copyright__ = 'discord.gg/nexustools'
__version__ = '2.0.0'

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
import httpx
import tls_client
import secrets
import ctypes
import websocket
import sys
import aiohttp
import asyncio
import pytz
import shutil
import tempfile
import undetected_chromedriver as uc

from faker import Faker
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from datetime import datetime
from tls_client import Session
from pathlib import Path
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from os.path import isfile, join

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

from .Funcs2.Token_Mail_verifier import TokenMailverifier
from .Funcs2.Token_pass_changer import pass_changer
from .Funcs2.Token_onliner import online_tokens
from .Funcs2.Status_Rotator import status_changer
from .Funcs2.Token_Nuker import Token_nuker
from .Funcs2.Token_editor import token_editor
from .Funcs2.Discord_Nuker import Discord_nuker
from .Funcs2.Nitro_gift_checker import check_codes
from .Funcs2.get_own_token import get_own_token
from .Funcs2.Pc_cleaner import Cleaner
from .Funcs2.TokenLogin import token_login

banner = f'''{Fore.LIGHTMAGENTA_EX}
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    '''

def donate_infos():
    print(f"{Fore.RESET}Btc: {Fore.GREEN}bc1q2e86tshk0cs05sty5ajlc6n6j8esutj2umcjtz")
    print(f"{Fore.RESET}Ltc: {Fore.GREEN}Lf5vGeL8BwNE84QGyAh1TJWuDxhyKS7QTD")
    print(f"{Fore.RESET}Eth: {Fore.GREEN}0xa66343933221706294c29935FC8da88b025D501B")
    input("Press Enter To continue...")

def discord():
    os.system("start https://discord.gg/nexustools")
    print("Opend Link!")
    time.sleep(1)