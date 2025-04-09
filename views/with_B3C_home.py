from tkinter import Frame, PhotoImage, Label, Button
from tkinter import messagebox

class with_B3C_HomePage(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.place_logo()
        self.place_send_home_btn()
        self.place_stress_test_btn()
        self.place_sensors_btn()
        self.place_PH10_tester_btn()
        self.place_status_btn()
        self.place_tune_encoders_btn()
        self.place_exit_btn()
        
    def place_logo(self):
        self.logo_photo = PhotoImage(file= "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/images/new_logo.png").subsample(2,2)
        self.logo= Label(self,bg="gray",image = self.logo_photo)
        self.logo.grid(row=0,column=1)
    
    def place_send_home_btn(self):
        self.send_home_btn = Button(self, text="Home")#Podría poner una casita de logo con una flecha
        self.send_home_btn.grid(row=1, column=0)
    
    def place_sensors_btn(self):
        self.sensors_page_btn = Button(self, text="Sensors")
        self.sensors_page_btn.grid(row=1, column=1)
    
    def place_status_btn(self):
        self.status_page_btn = Button(self, text="Status")
        self.status_page_btn.grid(row=1, column=2)
    
    def place_stress_test_btn(self):
        self.stress_test_btn = Button(self, text="Stress Test")
        self.stress_test_btn.grid(row=2, column=0)
        
    def place_PH10_tester_btn(self):
        self.PH10_tester_btn = Button(self, text="PH10")
        self.PH10_tester_btn.grid(row=2, column=1)
    
    def place_tune_encoders_btn(self):
        self.tune_encoders_btn = Button(self, text="Tune encoders")
        self.tune_encoders_btn.grid(row=2, column=2)
    
    def place_exit_btn(self):
        self.exit_btn = Button(self, text="EXIT")
        self.exit_btn.grid(row=3, column=1)
        
    def show_no_serial_connection(self):
        messagebox.showwarning("No serial connection", 
                               "Please connect to the serial port before proceeding.")
        