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
        self.frame.reset_btn.config(command = self.reset_)
        self.frame.test_btn.config(command = self.test_)      
        
    def start_routine(self):
        if self.model.serial_manager.is_connected:   
            if '0' not in self.frame.selected.get():
                if self.frame.show_askyesnocancel():
                    self.model.homing_routine.send_index_to_protocol_selector(self.frame.selected.get())
                else:
                    print("Ño quiero")
            else:
                self.frame.show_no_selection_message()
        else:
            self.frame.show_no_serial_connection()
        
    def reset_(self):
        self.model.serial_manager.reset_connection()
    
    def test_(self):
        self.model.serial_manager.test_soft()
        
    def home_page(self):
        self.view.switch("left_page")