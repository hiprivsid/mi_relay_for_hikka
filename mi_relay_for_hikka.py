__version__ = (1, 0, 0)
# requires: miio
# meta developer: @hiprivsidsmods

from .. import loader, utils

import logging
import datetime
import time

from telethon import types
from telethon.tl.types import Message



@loader.tds
class MRH(loader.Module):
 
    strings = {
        "name": "Mi_relay_for_hikka",
        "relayfalse": "Relay disabled",
        "relaytrue": "Relay enabled"
    }


    from miio.device import Device
    


    def __init__(self):
        # loader.ModuleConfig will throw!
        self.config = loader.LibraryConfig(
            loader.ConfigValue(
                "DEVICE_IP",
                None,
                "Device IP address",
                validator=loader.validators.String(),
            ),
            loader.ConfigValue(
		"DEVICE_TOKEN",
                None,
		"Device token",
                validator=loader.validators.String(),
	    )
        )





@loader.command()
async def relayon(self, message):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                plug = Device(DEVICE_IP, DEVICE_TOKEN)
                plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':True}])
                await utils.answer(message, 'relaytrue')

@loader.command()          
async def relayoff(self, message):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
		plug = Device(DEVICE_IP, DEVICE_TOKEN)
                plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':False}])
                await utils.answer(message, 'relayfalse')


