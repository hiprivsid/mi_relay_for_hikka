__version__ = (1, 0, 0)


from .. import loader, utils

import logging
import datetime
import time

from telethon import types

logger = logging.getLogger(__name__)

from miio.device import Device
plug = Device(DEVICE_IP, DEVICE_TOKEN)

@loader.tds
class MRH(loader.Module):
"""Mi Relay """

strings = {
     "name": "Mi relay for hikka"
    }

def __init__(self):
self.config = loader.ModuleConfig(
loader.ConfigValue(
'DEVICE_IP',
None,
"Ip of device"
)
)
def __init__(self):
self.config = loader.ModuleConfig(
loader.ConfigValue(
'DEVICE_TOKEN',
None,
"Token of device"
)
)



async def relayon(self, call: InlineCall):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                print(plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':True}]))
                await utils.answer(message, f'Реле включенно')
          
async def relayoff(self, call: InlineCall):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                print(plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':False}]))
                await utils.answer(message, f'Реле выключенно')

async def client_ready(self, client, db):

    )
