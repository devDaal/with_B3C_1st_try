baudrate = 9600
timeout = 1
restart_connection = "ctrl + ECB"

general_steps = ("Leitz","\x05\x03\x02","testsoft","bns",)
home_steps = (5,1,)
axes = {'x': 1, 
        'y': 2, 
        'z': 3, 
        'all': 9}