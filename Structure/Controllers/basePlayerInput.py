from enum import Enum
from idlelib.delegator import Delegator
from logging import DEBUG
from typing import Callable
from eventpy.eventdispatcher import EventDispatcher


class KeyMaps(Enum):
    Normal = {
        'y': "Approved",
        'n': "next turn",
        'h': "help",
        'c': "change input"
    }
    Alt = {
        'y': "Approved",
        'n': "next turn",
        'h': "help",
        'c': "change input"
    }

class BasePlayerInput :

    map : KeyMaps
    inputEvents = { ("Approved", EventDispatcher()) , ("next turn", EventDispatcher()) , ("help", EventDispatcher()) , ("change input", EventDispatcher())}

    def __init__(self, args : {()} = None, kmap = KeyMaps.Normal):
        self.map = kmap
        if args is not None :
            if args in self.inputEvents :
                for arg,event in args,self.inputEvents :
                    if  event.Key == arg.Key :
                        EventDispatcher(event).insertListener(arg, event.Key, False)

    def GetKey(self, charInput) :
        return self.map.value


    def WaitForPlayerResponse(self, isPlayerAllowedToOrder : bool):
        if DEBUG: print("player order")
        currInput = input()
        if isPlayerAllowedToOrder:
            if currInput.lower() in map.__dict__.keys():
                EventDispatcher( self.inputEvents.__dict__[map.__dict__[currInput]]).dispatch()
                return None
        return currInput