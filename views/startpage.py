from tkinter import Frame, Button, PhotoImage, Label

class StartPageview(Frame):
    
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        #self.config['bg'] = 'gray'
        
        self.place_left_button()
        self.place_right_button()
        self.place_settings_button()
        self.place_logo()
        
    def place_left_button(self):
        self.left_btn = Button(self, text="LEFT")
        self.left_btn.grid(row=2, column=0)
    
    def place_right_button(self):
        self.right_btn = Button(self, text="RIGHT")
        self.right_btn.grid(row=2, column=2)
    
    def place_settings_button(self):
        self.settings_btn = Button(self, text="SETTINGS")
        self.settings_btn.grid(row=2, column=1)
    
    def place_logo(self):
        self.logo_photo = PhotoImage(file= "C:/Users/ITS_Servicio/Desktop/Desarrollo Software Diego/Learning/Intento de MVC B3C/images/new_logo.png").subsample(2,2)
        self.logo= Label(self,bg="gray",image = self.logo_photo)
        self.logo.grid(row=0,column=1)
    
        