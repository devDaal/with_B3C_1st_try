from .base import ObservableModel

class Homing_Routine(ObservableModel):
    
    def __init__(self):
        super().__init__()
        
    def send_index_to_protocol_selector(self,axis):
        self.axis_option = axis
        self.trigger_event("axis_option")
            