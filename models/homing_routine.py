from .base import ObservableModel

class Homing_Routine(ObservableModel):
    
    def __init__(self):
        super().__init__()
        """self.counter += 1
        print("Homing", self.counter)"""

        print(self._initialized,"homing")
        #variables
        
    def send_index_to_serial_manager(self,axis):
        
        #Aquí hay que cambiar esto por tomar el valor de la selección de protocolo 
        #y ver a dónde enviarlo. Aquí hay que recibir la selección del protocolo del usuario
        #decidir de dónde vamos a importar los comandos, regresar la información al controlador
        # y enviarla a serial_manager. 
        # ¿El serial manager debe tener la funcionalidad de los 4 protocolos? o debe de ser un nuevo modelo?
        # ¿Cómo comunico a los modelos? ¿Cómo envío los comandos y la rutina de cada protocolo a serial_manager?
        self.axis_options = ('x','y','z',)
        if axis in self.axis_options:
            self.axis_option = self.axis_options.index(axis,0,3) + 1
        if axis == 'all':
            self.axis_option = 9
        self.trigger_event("axis_option")
            