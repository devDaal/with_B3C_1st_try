import subprocess
import psutil
import time
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
        self.frame.update_ports_btn.config(command = lambda: self.update_values())
        self.frame.connect_btn.config(command = self.send_selections_to_serial_manager)
        self.frame.radio_DC.config(command = self.disconnection_needed)
        self.frame.radio_LEITZ.config(command = self.disconnection_needed)
        self.frame.radio_SHEFFIELD.config(command = self.disconnection_needed)
        self.frame.radio_REFLEX.config(command = self.disconnection_needed)
        self.frame.ph10_btn.config(command = self.open_ph10_module)
        self.frame.tcp_connect_btn.config(command = self.send_config_to_tcp_manager)
        
    def update_values(self):
        self.model.serial_manager.list_ports()
    
    def update_ports_view(self):
        self.frame.combo_port["values"] = self.model.serial_manager.port_list
        print(self.frame.combo_port["values"])
        #buscar la forma de que no se quede el valor anterior en el combo box
        if self.model.serial_manager.port_list:
            self.frame.combo_port.current(0)
        else:
            self.frame.combo_port.set("")
        self.frame.combo_port.update()
            
    def send_selections_to_serial_manager(self):
        if self.frame.selected_protocol.get() != '0': 
            self.protocol = self.frame.selected_protocol.get()
            self.model.serial_manager.toggle_connection(self.frame.combo_port.get(),
                                        self.model.protocol_selector.send_port_config(self.protocol))
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
            
    def disconnection_needed(self):
        if self.model.serial_manager.is_connected:
            if self.protocol != self.frame.selected_protocol.get():    
                self.frame.selected_protocol.set(self.protocol)
                self.frame.show_disconnection_needed()

    def send_config_to_tcp_manager(self):
        if self.frame.selected_protocol.get() != '0': 
            self.protocol = self.frame.selected_protocol.get()
        else:
            self.frame.show_selection_needed()
        self.ip_address = self.frame.server_ip_adrres.get()
        self.port_number = self.frame.server_port_number.get()
        steps = self.model.protocol_selector.send_tcp_connection_config(self.protocol)
        is_validated_ip = self.model.tcp_manager.validate_ip_entry(self.ip_address)
        is_validated_port = self.model.tcp_manager.validate_server_port_number(self.port_number)
        if is_validated_ip:
            if is_validated_port:
                print("Conectanding...")
                self.ip_address = self.model.tcp_manager.normalize_ip_entry(self.ip_address)
                self.model.tcp_manager.connect(self.ip_address, self.port_number, steps['connection_steps'])
            else:
                self.frame.show_invalid_port_input()
        else:
            self.frame.show_invalid_ip_input()
                
    def open_ph10_module(self):
        script_path = r"C:\Users\ITS_Servicio\Desktop\Desarrollo Software Diego\Proyecto Cabezalv1\Pruebas.v2\Interfaz\Version Diego.py"
        
        for process in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if process.info['cmdline'] and script_path in process.info['cmdline']:
                    return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        subprocess.Popen(["python", script_path], shell=True)
        time.sleep(0.05)
    
    def start_page(self):
        self.view.switch("startpage")