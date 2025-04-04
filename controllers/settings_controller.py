import subprocess
import os

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
        self.frame.connect_btn.config(command = self.send_selections_to_serial_manager)
        self.frame.radio_DC.config(command = self.disconnection_needed)
        self.frame.radio_LEITZ.config(command = self.disconnection_needed)
        self.frame.radio_SHEFFIELD.config(command = self.disconnection_needed)
        self.frame.radio_REFLEX.config(command = self.disconnection_needed)
        self.frame.ph10_btn.config(command = self.open_ph10_module)
        
    def update_values(self):
        self.model.serial_manager.list_ports()
    
    def update_ports_view(self):
        self.frame.combo_port["values"] = self.model.serial_manager.port_list
        if self.model.serial_manager.ports:
            self.frame.combo_port.current(0)
        else:
            self.frame.combo_port.set("")
            
    def send_selections_to_serial_manager(self):
        if self.frame.selected_protocol.get() != '0':    
            self.model.serial_manager.toggle_connection(self.frame.combo_port.get())
            self.protocol = self.frame.selected_protocol.get()
            #Queda pendiente ver cómo recibir el eje, para después mandar eje y protocolo juntos
            #Qué parte del código tiene acceso simultáneo a ambas cosas? 
            #Crear una función que pida ambas, se alamacenan y luego enviarlas
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
                
    def open_ph10_module(self):
        script_path = r"C:\Users\ITS_Servicio\Desktop\Desarrollo Software Diego\Proyecto Cabezalv1\Pruebas.v2\Interfaz\Version Diego.py"
        subprocess.Popen(["python", script_path], shell=True)
    
    def start_page(self):
        self.view.switch("startpage")