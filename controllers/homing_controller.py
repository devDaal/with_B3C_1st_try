from views.main import View
from models.main import Model

class Homing_Controller:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["homing_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.home_page)
        self.frame.start_btn.config(command = self.start_routine)      
        
    def start_routine(self):
        #Agregar que se lea si actualmente existe conexión serial para poder continuar con el proceso
        if self.model.serial_manager.is_connected:   
            if '0' not in self.frame.selected.get():
                if self.frame.show_askyesnocancel():
                    self.model.homing_routine.send_index_to_serial_manager(self.frame.selected.get())
                else:
                    print("Ño quiero")
            else:
                self.frame.show_no_selection_message()
        else:
            self.frame.show_no_serial_connection()
        
        
    def home_page(self):
        self.view.switch("left_page")