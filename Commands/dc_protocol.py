#DC protocol Commands
baudrate = 9600
timeout = 1
general_steps = ("DC","\x05\x03\x02","\x74\x65\x73\x74\x73\x6f\x66\x74","\x62\x6e\x73",)
home_steps = (5,1,)
axes = {'x': 1, 
        'y': 2, 
        'z': 3, 
        'all': 9}

connection_steps = ("\x0e\x0d\x0a\x0d\x0a\x0d\x0a\x03\x0d\x0a\x0d\x0a\x0d\x0a\x02\x02\x0d\x0a", 
                    "\x43\x4d\x4d\x54\x59\x50\x0d\x0a")
tcp_general_steps = ("DC",)
tcp_home_steps = (5,1,) 
tcp_axes = {'x': 1, 
             'y': 2, 
             'z': 3, 
             'all': 9}