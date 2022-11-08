__version__ = (1, 0, 0)


from .. import loader
from ..inline.types import InlineCall

import random
import requests
import logging
from miio.device import Device
plug = Device(DEVICE_IP, DEVICE_TOKEN)

await self.allmodules.commands["config"](
	await utils.answer(message, f"{self.get_prefix()}config mirelay")
)

    async def client_ready(self, client, db):
        logger.info("сру в логи")

@loader.tds
class MRH(loader.Module):

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


