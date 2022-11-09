__version__ = (1, 0, 0)


from .. import loader, utils

import logging
import datetime
import time

from telethon import types
from telethon.tl.types import Message

logger = logging.getLogger(__name__)

@loader.tds
class MRH(loader.Module):
    """Mi Relay
    
Developer: @hiprivsid
"""


strings = {
     "name": "Mi_relay _for_hikka",
     "relayfalse": "Relay disabled",
     "relaytrue": "Relay enabled"
    }


from miio.device import Device
plug = Device(DEVICE_IP, DEVICE_TOKEN)



		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"DEVICE_IP",
				None,
				"Token of device"
			),
			loader.ConfigValue(
				"DEVICE_TOKEN",
				None,
				"Token of device"
			)
		)






@loader.command()
async def relayon(self, message):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':True}])
                await utils.answer(message, 'relaytrue')

@loader.command()          
async def relayoff(self, message):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':False}])
                await utils.answer(message, 'relayfalse')


