from tkinter import Frame, Label, Button, StringVar, Radiobutton, messagebox

class Homingview(Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.place_title()
        self.place_selection_widget()
        self.place_exit_btn()
        self.place_information_widget()
        self.place_start_btn()
        
    def place_title(self):
        title = Label(self, text="HOMING",font=("Robot",12,"normal"))
        title.grid()
        
    def place_exit_btn(self):
        self.exit_btn = Button(self, text='EXIT',
                               font=("Robot",12,"bold"), bg='red', fg='white')
        self.exit_btn.grid(row=5)
        
    def place_start_btn(self):
        self.start_btn = Button(self, text='START',
                               font=("Robot",12,"bold"), bg='green', fg='white')
        self.start_btn.grid(column=1,row=5,padx=(30,0))
        
    def place_selection_widget(self):
        self.selected = StringVar()
        self.selected.set("0") #This is just here for the radios to start unselected
        self.radio_x = Radiobutton(self, text='Home in X', value='x', variable=self.selected)
        self.radio_y = Radiobutton(self, text='Home in Y', value='y', variable=self.selected)
        self.radio_z = Radiobutton(self, text='Home in Z', value='z', variable=self.selected)
        self.radio_all = Radiobutton(self, text='Home All', value='all', variable=self.selected)
        self.radio_x.grid()
        self.radio_y.grid()
        self.radio_z.grid()
        self.radio_all.grid(sticky='w')
        
    def place_information_widget(self):
        self.x_led = Label(self, text=' ', bg='gray',width=2)
        self.x_led.grid(column=1, row=1,padx=(30,0))
        
        self.x_lbl = Label(self, text='Home in X')
        self.x_lbl.grid(column=2,row=1)
        
        self.y_led = Label(self, text=' ', bg='gray',width=2)
        self.y_led.grid(column=1, row=2,padx=(30,0))
        
        self.y_lbl = Label(self, text='Home in Y')
        self.y_lbl.grid(column=2,row=2)
        
        self.z_led = Label(self, text=' ', bg='gray',width=2)
        self.z_led.grid(column=1, row=3,padx=(30,0))
        
        self.z_lbl = Label(self, text='Home in Z')
        self.z_lbl.grid(column=2,row=3)
        
    def show_askyesnocancel(self):
        return messagebox.askyesnocancel('Ready to start?',
                                  """This action will move the CMM, make sure the space is clear.
                                  
                                  Ready to move the machine?""")
        
    def show_no_selection_message(self):
        return messagebox.showinfo('No selection',
                                   'Please choose a routine to start.')
        