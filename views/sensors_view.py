from tkinter import Frame, Label, Button

class Sensorsview(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.place_title()
        self.place_exit_btn()
        self.place_information_widget()
        self.place_check_btn()
        
    def place_title(self):
        title = Label(self, text="Sensors",font=("Robot",12,"normal"))
        title.grid()
        
    def place_exit_btn(self):
        
        self.buttons_container = Frame(self)
        self.buttons_container.grid(column=0, row=5, padx=(10,0), pady=(10,0))
        
        self.exit_btn = Button(self.buttons_container, text='EXIT',
                               font=("Robot",12,"bold"), bg='red', fg='white')
        self.exit_btn.grid(sticky='sw', padx=5)
        
    def place_check_btn(self):
        
        self.check_btn = Button(self.buttons_container, text='CHECK',
                               font=("Robot",12,"bold"), bg='green', fg='white')
        self.check_btn.grid(column=1, row=0, padx=(10,0))
        
    def place_information_widget(self):
        
        container = Frame(self)
        container.grid(column=0, row=1)
        
        self.limit_pos_x_led = Label(container, text=' ', bg='gray',width=2)
        self.limit_pos_x_led.grid(column=1, row=1,pady=(2,0))
        
        self.limit_pos_x_lbl = Label(container, text='Limit (+) X')
        self.limit_pos_x_lbl.grid(column=0,row=1,sticky='e')
        
        self.limit_pos_y_led = Label(container, text=' ', bg='gray',width=2)
        self.limit_pos_y_led.grid(column=1, row=2,pady=(2,0))
        
        self.limit_pos_y_lbl = Label(container, text='Limit (+) in Y')
        self.limit_pos_y_lbl.grid(column=0,row=2)
        
        self.limit_pos_z_led = Label(container, text=' ', bg='gray',width=2)
        self.limit_pos_z_led.grid(column=1, row=3,pady=(2,0))
        
        self.limit_pos_z_lbl = Label(container, text='Limit (+) in Z')
        self.limit_pos_z_lbl.grid(column=0,row=3)
        
        self.air_led = Label(container, text=' ', bg='gray',width=2)
        self.air_led.grid(column=1, row=4,pady=(2,0))
        
        self.air_lbl = Label(container, text='Air')
        self.air_lbl.grid(column=0,row=4,sticky='e')
        
        #------------------------Negative Limits------------------------
        
        self.limit_neg_x_led = Label(container, text=' ', bg='gray',width=2)
        self.limit_neg_x_led.grid(column=2, row=1,padx=(30,0),pady=(2,0))
        
        self.limit_neg_x_lbl = Label(container, text='Limit (-) X')
        self.limit_neg_x_lbl.grid(column=3,row=1,sticky='w')
        
        self.limit_neg_y_led = Label(container, text=' ', bg='gray',width=2)
        self.limit_neg_y_led.grid(column=2, row=2,padx=(30,0),pady=(2,0))
        
        self.limit_neg_y_lbl = Label(container, text='Limit (-) in Y')
        self.limit_neg_y_lbl.grid(column=3,row=2)
        
        self.limit_neg_z_led = Label(container, text=' ', bg='gray',width=2)
        self.limit_neg_z_led.grid(column=2, row=3,padx=(30,0),pady=(2,0))
        
        self.limit_neg_z_lbl = Label(container, text='Limit (-) in Z')
        self.limit_neg_z_lbl.grid(column=3,row=3)