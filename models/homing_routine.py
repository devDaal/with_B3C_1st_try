from .base import ObservableModel

class Homing_Routine(ObservableModel):
    
    def __init__(self):
        super().__init__()
        """self.counter += 1
        print("Homing", self.counter)"""

        #variables
        
    def home_routine(self,axis):
        print("Enviar testsoft")
        print("Enviar bns")
        print("Enviar 5")
        print("Enviar 1")
        listilla = ('x','y','z',)
        if axis in listilla:
            print(listilla.index(axis,0,3) + 1)
        if axis == 'all':
            print(9)