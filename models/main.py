from .hello_test import Hello_Test
from .serial_manager import SerialManager
from .homing_routine import Homing_Routine
from .protocol_selector import Protocol_Selector

class Model:
    
    def __init__(self):
        self.hello = Hello_Test()
        self.serial_manager = SerialManager()
        self.homing_routine = Homing_Routine()
        self.protocol_selector = Protocol_Selector()