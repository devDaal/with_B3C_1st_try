from views.main import View
from models.main import Model

class SettingsController:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["settings_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.start_page)
        self.frame.combo_port.config(postcommand = lambda: self.update_values())
        self.frame.connect_btn.config(command = self.send_port_to_model)
        
    def update_values(self):
        self.model.serial_manager.list_ports()
    
    def update_ports_view(self):
        self.frame.combo_port["values"] = self.model.serial_manager.port_list
        if self.model.serial_manager.ports:
            self.frame.combo_port.current(0)
        else:
            self.frame.combo_port.set("")
            
    def send_port_to_model(self):
        if self.frame.selected_control.get() != '0':    
            self.model.serial_manager.toggle_connection(self.frame.combo_port.get())
        else:
            self.frame.show_selection_needed()
        
    def update_view_connection_status(self):
        if self.model.serial_manager.is_connected:
            self.frame.show_succesfull_connection()
            self.frame.connect_btn.config(text='DISCONNECT', bg='red')
        else:
            self.frame.show_succesfull_disconnection()
            self.frame.connect_btn.config(text='CONNECT', bg='green')
            
    def unexpected_disconnection(self):
        """Inside settings Page Controller's scope"""
        self.frame.connect_btn.config(text='CONNECT', bg='green')
        if self.model.serial_manager.is_decode_error:
            self.frame.show_decode_error()
        else:
            self.frame.show_unexpected_disconection_error()

    def start_page(self):
        self.view.switch("startpage")