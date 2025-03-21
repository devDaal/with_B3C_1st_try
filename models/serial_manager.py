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

    def list_ports(self):
        self.ports = serial.tools.list_ports.comports()
        self.port_list = [port.device for port in self.ports]
        self.trigger_event("update_ports")
        
    def read_data(self):
        if self.serial_port and self.serial_port.is_open:
            try:
                self.data = self.serial_port.readline().decode().strip()
                if self.data:
                    print(f"Datos recibidos: {self.data}")
                    self.data_manager(self.data)#Aquí va trigger_event
                    #aquí se pueden enviar los datos al controlador que le sean útiles
                    #a través de trigger_event
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
    
    def connect(self, port_to_open, baudrate = 9600):
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
    
    def toggle_connection(self, port_to_open):
        if self.is_connected:
            self.disconnect()
            self.trigger_event("update_connection_status")
        else:
            selected_port = port_to_open
            if selected_port:
                success = self.connect(selected_port)
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
        
    def data_manager(self, data):
        #La respuesta de la máquina es inmediata? Es casi inmediato
        #Si pongo time.sleep, afecta a la aplicación? Parece que no
        print("Enviando testsoft")
        self.serial_port.write("TESTSOFT\n".encode("utf-8"))
        time.sleep(0.5)
        message = self.serial_port.readline().decode().strip()
        if message == "LED encendido":
           print("Enviando bns")
           self.serial_port.write("bns\n".encode("utf-8"))
           time.sleep(0.5)
        elif message == "":
           print("No hay nada")
           time.sleep(0.5)
        elif message == "LED apagado":
            print("off")
        """
           if self.serial_port.readline().decode().strip() == "Título 1":
                self.serial_port.write("5")
                time.sleep(0.5)
                if self.serial_port.readline().decode().strip() == "Título 2":
                     self.serial_port.write("1")
                     time.sleep(0.5)
                     if self.serial_port.readline().decode().strip() == "Título 3":
                          self.serial_port.write(data)
                          time.sleep(0.5)
                          if self.serial_port.readline().decode().strip() == "Respuesta esperada":
                            self.trigger_event("evento para ese comando")
        else:
            self.trigger_event("evento para manejar datos no válidos")"""