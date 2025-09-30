from enum import Enum

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

    map = KeyMaps.Normal

    def GetKey(self, charInput) :
        return self.map.value


