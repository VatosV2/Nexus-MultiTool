__title__ = 'Nexus'
__author__ = 'Vatos'
__copyright__ = 'discord.gg/nexustools'
__version__ = '4.0.0'

import re
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
import subprocess
import http

import undetected_chromedriver as uc
import tkinter as tk

from tkinter import filedialog
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
from bs4 import BeautifulSoup
from pytube import YouTube
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve

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
from .Funcs.clear import clear_output, clear_input

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

from .Funcs3.token_huminazor import procces_hm
from .Funcs3.token_watermarker import token_wartermarker
from .Funcs3.remove_discord_injection import RemoveInjection
from .Funcs3.token_payment_checker import check_payments
from .Funcs3.token_leave_groups import leave_groups
from .Funcs3.picture_scraper import scrape_Avatars
from .Funcs3.token_guild_count_checker import guild_count
from .Funcs3.token_message_everywhere import meessage_everywhere_spam
from .Funcs3.gen_test_token import gen_token
from .Funcs3.token_info import fetch_user_details
from .Funcs3.converter import youtube_converter
from .Funcs3.social_menu import social_menu
from .Funcs3.ip_lookup import ip_lookup

from .Funcs4.id_to_tokend import id__token
from .Funcs4.ip_grabber import make_ip_grabber
from .Funcs4.message_logger import message_logger
from .Funcs4.serial_checker import check_serials
from .Funcs4.serial_changer import serial_changer

banner = f'''{Fore.LIGHTMAGENTA_EX}
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗  
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝     
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗       
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║      
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║   
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexustools
    '''

def donate_infos():
    print(f"{Fore.RESET}Btc: {Fore.GREEN}bc1q2e86tshk0cs05sty5ajlc6n6j8esutj2umcjtz")
    print(f"{Fore.RESET}Ltc: {Fore.GREEN}Lf5vGeL8BwNE84QGyAh1TJWuDxhyKS7QTD")
    print(f"{Fore.RESET}Eth: {Fore.GREEN}0xa66343933221706294c29935FC8da88b025D501B")
    input("Press Enter To continue...")

os.system("title discord.gg/nexustools")
response = requests.get('https://raw.githubusercontent.com/VatosV2/Nexus-MultiTool/main/Helper/__init__.py')
version_match = re.search(r"__version__\s*=\s*[\'\"](.*?)[\'\"]", response.text)
if version_match and __version__ == version_match.group(1):
    pass
else:
    input(f"{Fore.RED} New Version Detected! https://github.com/VatosV2/Nexus-MultiTool")
