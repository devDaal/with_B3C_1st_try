from tkinter import Button, Frame, Label, messagebox, StringVar, Radiobutton
from tkinter.ttk import Combobox

class Settingsview(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.place_control_selection_widget()
        self.place_port_selection_widget()
        self.place_title()
        self.place_PH10_button()
        self.place_exit_btn()
        
        
    def place_exit_btn(self):
        self.exit_btn = Button(self, text="EXIT", 
                               font=("Robot",12,"bold"), bg='red', fg='white')
        self.exit_btn.grid(row=3, sticky='sw', padx=5, pady=(5,0)) 
        
    def place_title(self):
        title = Label(self, text='SETTINGS', font = ("Robot",12,"bold"))
        title.grid(row=0,column=0,padx=10, pady=10)
        
    def place_port_selection_widget(self):
        container = Frame(self)
        container.grid(column=1, row=1)
        
        lbl = Label(container, text='PORT SELECTION',font=("Robot",12,"normal"))
        lbl.grid(pady=5,padx=5)
        
        self.combo_port = Combobox(container, state='readonly')
        self.combo_port.grid()       
        
        self.connect_btn = Button(container, text="CONNECT", width=11,
                                  font=("Robot",12,"bold"),fg='white',bg='green')    
        self.connect_btn.grid(row=1,column=1, padx=5)
        
    def place_control_selection_widget(self):
        container = Frame(self)
        container.grid(column=0, row=1)
        
        lbl = Label(container, text='CONTROL SELECTION',font=("Robot",12,"normal"))
        lbl.grid(pady=5,padx=5)
        
        self.selected_protocol = StringVar()
        self.selected_protocol.set("0") #This is just here for the radios to start unselected
        self.radio_DC = Radiobutton(container, text='DC Protocol', value='dc', variable=self.selected_protocol)
        self.radio_LEITZ = Radiobutton(container, text='Leitz Protocol', value='ltz', variable=self.selected_protocol)
        self.radio_SHEFFIELD = Radiobutton(container, text='Sheffield Protocol', value='sh', variable=self.selected_protocol)
        self.radio_REFLEX = Radiobutton(container, text='Reflex Protocol', value='rfx', variable=self.selected_protocol)
        self.radio_DC.grid(sticky='w',padx=(10,0))
        self.radio_LEITZ.grid(sticky='w',padx=(10,0))
        self.radio_SHEFFIELD.grid(sticky='w',padx=(10,0))
        self.radio_REFLEX.grid(sticky='w',padx=(10,0))
        
    def place_PH10_button(self):
        container = Frame(self)
        container.grid(column=0, row=2,padx=(5,0) ,sticky='w')
        
        self.ph10_btn = Button(container, text="PH10 Tester",
                                  font=("Robot",12,"bold"),fg='white',bg='green')    
        self.ph10_btn.grid()
        
    def show_selection_needed(self):
        messagebox.showwarning('Selection required',
                               "You haven't selected a control yet, please do so.")
        
    def show_disconnection_needed(self):
        messagebox.showwarning('Protocol already selected',
                               "You already selected a protocol, if you need to change it, please disconnect and connect again.")
        
    def show_succesfull_connection(self):
        messagebox.showinfo('Succesfull connection',
                            'The connection has been succesfull.')
        
    def show_succesfull_disconnection(self):
        messagebox.showinfo('Succesfull disconnection',
                            'The disconnection has been succesfull.')
    
    def show_connection_error(self):
        messagebox.showerror('Connection Error',
                             'There was a general connection error.')
        
    def show_decode_error(self):
        messagebox.showerror('Connection Error',
                             'There was a decoding error in the connection.')
        
    def show_unexpected_disconection_error(self):
        messagebox.showerror('Connection Error',
                             'There was an unexpected connection error.')