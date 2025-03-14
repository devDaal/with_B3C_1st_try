from .hello_test import Hello_Test
from .serial_manager import SerialManager
from .homing_routine import Homing_Routine

class Model:
    
    def __init__(self):
        self.hello = Hello_Test()
        self.serial_manager = SerialManager()
        self.homing_routine = Homing_Routine()
        
        print(self.hello is self.serial_manager)
        print(self.hello is self.homing_routine)
        print(self.serial_manager is self.homing_routine)