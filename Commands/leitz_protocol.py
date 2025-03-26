baudrate = 9600
timeout = 1
restart_connection = "ctrl + CBE"
general_step_2 = 'testsoft'
home_x = 1
home_y = 2
home_z = 3
home_all = 9

general_steps = ("ctrl + CBE","testsoft","bns",)
home_steps = (5,1,)
axes = {'x': 1, 
        'y': 2, 
        'z': 3, 
        'all': 9}

"""
IDEA: Utilizar tuplas para las rutinas de comandos de lo que se repite, es decir, 
en todos los ejes se sigue el mismo proceso, por lo que en el serial manager se 
puede hacer algo como:

def home_routine(self,axis,protocol):

    module_name = Protocols[protocol]
    protocol_module = importlib.import_module(module_name)
    
    general_steps = protocol_module.general_steps
    home_steps = protocol_module.home_steps
    home_to_axis = protocol_module.axes[axis]

    for x in general_steps:
        serial_port.write(f"{x}\n".encode("utf-8"))
        time.sleep(0.5)
        
    for x in home_steps:
        serial_port.write(f"{x}\n".encode("utf-8"))
        time.sleep(0.5)
        
    serial_port.write(f"{home_to_axis}\n".encode("utf-8"))
    time.sleep(0.5)
"""