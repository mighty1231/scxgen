import sys
v = sys.version_info
assert v.major == 3 and v.minor >= 6, "Run with python which is 32bit and version >= 3.6"
assert sys.maxsize == 2**31 - 1, "Run with python which is 32bit and version >= 3.6"

from .mapfile import MapFile
from .sections.trigsection import Trigger, Condition, Action, TRIGSection
from .sections.mbrfsection import MBTrigger, MBAction, MBRFSection
from .sections.condact import *
from .sections.uprpsection import UnitProperty, UPRPSection
from .sections.strsection import STRSection
from .sections.mrgnsection import MRGNSection
from .trgconst import *
from .trgstrconst import *
from .convtep import ConvertTrigEditPlusTrigger
from .hooks import *
from .utils import *
from .coder import Coder
