from .base import ObservableModel
import importlib
from Commands.protocols import Protocols

class Protocol_Selector(ObservableModel):
    
    def __init__(self):
        super().__init__()
        
    def send_routine_to_serial_manager(self,protocol,axis):
        
        self.routine = {}
        module_name = Protocols[protocol]
        protocol_module = importlib.import_module(module_name)
        general_steps = protocol_module.general_steps
        home_steps = protocol_module.home_steps
        home_to_axis = protocol_module.axes[axis]
        
        self.routine['general_steps'] = general_steps
        self.routine['home_steps'] = home_steps
        self.routine['home_to_axis'] = home_to_axis
        
        print(self.routine)
        self.trigger_event("send_routine")
        
    def send_port_config(self, protocol):
        self.port_config = {}
        protocol_module = importlib.import_module(Protocols[protocol])
        self.port_config['baudrate'] = protocol_module.baudrate
        self.port_config['timeout'] = protocol_module.timeout
        return self.port_config
        #self.trigger_event("send_port_config")