import serial
import serial.tools.list_ports
import threading
import time
from .base import ObservableModel

class SerialManager(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.serial_port = None
        self.is_connected = False
        self.port_name = None
        self.ports = None
        self.secure_disconnection = None
        self.is_decode_error = None
        self.is_running = False

    def list_ports(self):
        self.ports = serial.tools.list_ports.comports()
        self.port_list = [port.device for port in self.ports]
        self.trigger_event("update_ports")
        
    def read_data(self):
        if self.serial_port and self.serial_port.is_open:
            try:
                self.data = self.serial_port.readall().decode().strip()
                if self.data:
                    print(f"Datos recibidos: {self.data}")
                    #Aquí va trigger_event ??
                    #aquí se pueden enviar los datos al controlador que le sean útiles
                    #a través de trigger_event ??
                return self.data
            except serial.SerialException:
                self.secure_disconnection = False
                self.is_connected = False
                self.is_decode_error = False
            except UnicodeDecodeError:
                self.secure_disconnection = False
                self.is_connected = False
                self.is_decode_error = True
        return None
    
    def connect(self, port_to_open, baudrate, timeout):
        try:
            self.serial_port = serial.Serial(port_to_open, baudrate, timeout=1)
            self.is_connected = True
            self.port_name = port_to_open
            return True
        except serial.SerialException as e:
            print(f"Error al conectar: {e}")
            self.is_connected = False
            return False
    
    def disconnect(self):
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.is_connected = False
            self.port_name = None
            self.secure_disconnection = True
    
    def toggle_connection(self, port_to_open, port_config):
        baudrate = port_config['baudrate']
        timeout = port_config['timeout']
        if self.is_connected:
            self.disconnect()
            self.trigger_event("update_connection_status")
        else:
            selected_port = port_to_open
            if selected_port:
                #Aquí se debe pedir la configuración del puerto, guardarse como variables y pasarlas
                #a connect
                success = self.connect(selected_port,baudrate,timeout)
                if success:
                    self.trigger_event("update_connection_status")
                    self.start_monitoring()
    
    def start_monitoring(self):
        def monitor():
            while self.is_connected:
                time.sleep(1)
                data = self.read_data()
                if data is None and not self.is_connected:
                    if not self.secure_disconnection:
                        self.handle_disconnection()
                    break        
        threading.Thread(target=monitor, daemon=True).start()
        
    def handle_disconnection(self):
        """Handles unexpected disconnection."""
        self.trigger_event("unexpected_disconnection")
            
    def home_routine(self,routine):

        self.is_running = True
        
        general_steps = routine['general_steps']
        home_steps = routine['home_steps']
        home_to_axis = routine['home_to_axis']
        
        for x in general_steps:
            self.serial_port.write(f"{x}\r".encode("utf-8"))
            print(x)
            time.sleep(3)
            
        for x in home_steps:
            self.serial_port.write(f"{x}\r".encode("utf-8"))
            print(x)
            time.sleep(3)
            
        self.serial_port.write(f"{home_to_axis}\r".encode("utf-8"))
        print(home_to_axis)
        time.sleep(3)
        
        self.is_running = False
        
    def reset_connection(self):
        if self.serial_port and self.serial_port.is_open:    
            print("Enviando: ctrl + ECB")
            self.serial_port.write("\x05\x03\x02".encode("utf-8"))
            
    def test_soft(self):
        if self.serial_port and self.serial_port.is_open:
            print("Enviando: testsoft")
            self.serial_port.write("\x74\x65\x73\x74\x73\x6f\x66\x74\x0d".encode("utf-8"))