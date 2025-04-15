import socket
import threading

from .base import ObservableModel

class TCPManager(ObservableModel):
    
    def __init__(self):
        super().__init__()
        self.is_running = False
        self.client = None
        self.is_connected = False
        
    def validate_ip_entry(self, ip_address):
        if '.' in ip_address:
            parts = ip_address.split('.')
            if len(parts) == 4:
                for part in parts:
                    if not part.isdigit() or not (0 <= int(part) <= 255):
                        return False
                return True
        return False
    
    def validate_server_port_number(self, port_number):
        if port_number.isdigit():
            port_number = int(port_number)
            if 0 < port_number < 65536:
                return True
        return False
    
    def normalize_ip_entry(self, ip_address):
        parts = ip_address.split('.')
        normalized_parts = [str(int(part)) for part in parts]
        return '.'.join(normalized_parts)
    
    def connect(self, ip_address, port_number, connection_steps):
        ADDR = ip_address
        PORT = int(port_number)
        SERVER = (ADDR, PORT)
        print(SERVER)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect(SERVER)
            for step in connection_steps:
                self.client.sendall(step.encode())
                response = self.client.recv(1024).decode()
                print(f"Respuesta del servidor: {response}")
            if 'CMMTYP' in response:
                #self.start_listening()
                self.is_connected = True
                self.client.close()
                #Mandar el mensaje de conexión exitosa
            else:
                print("Se logró")
                self.client.close()
                self.is_connected = False
                #Mensaje de que no se pudo lograr la conexión
        except socket.error as e:
            print(f"Error al conectar: {e}")
    
    def disconnect(self):
        if self.client:
            try:
                self.client.close()
                self.is_connected = False
                print("Desconectado del servidor")
            except socket.error as e:
                print(f"Error al desconectar: {e}")
    
    def start_listening(self):
        def listen():
            self.is_running = True
            while self.is_running:
                try:
                    data = self.client.recv(1024)  # Tamaño del buffer
                    if data:
                        print(f"Datos recibidos: {data.decode()}")
                        self.trigger_event("data_received", data.decode())
                    else:
                        print("El servidor cerró la conexión.")
                        self.is_running = False
                        self.disconnect()
                        self.trigger_event("server_disconnected")
                except socket.error as e:
                    print(f"Error en la conexión: {e}")
                    self.is_running = False
                    self.disconnect()
                    self.trigger_event("connection_error", str(e))
                    break

        threading.Thread(target=listen, daemon=True).start()