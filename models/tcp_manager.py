from .base import ObservableModel

class TCPManager(ObservableModel):
    
    def __init__(self):
        super().__init__()
        
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