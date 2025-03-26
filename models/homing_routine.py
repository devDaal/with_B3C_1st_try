from .base import ObservableModel

class Homing_Routine(ObservableModel):
    
    def __init__(self):
        super().__init__()
        """self.counter += 1
        print("Homing", self.counter)"""

        print(self._initialized,"homing")
        #variables
        
    def send_index_to_serial_manager(self,axis):
        
        self.axis_options = ('x','y','z',)
        if axis in self.axis_options:
            self.axis_option = self.axis_options.index(axis,0,3) + 1
        if axis == 'all':
            self.axis_option = 9
        self.trigger_event("axis_option")
            