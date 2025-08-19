from enum import Enum

class eSite(Enum):
    B1F=0,
    B2F=1,
    B3F=2,
    B4F=3,
    C3F=4,
    D1F=5,
    D2F=6,
    VC2F=7,

class eManuType(Enum):
    양산=0,
    개발=1,
    
class eEquipmentModel(Enum):
    K465I=0,
    C4=1,
    EPIK = 2,