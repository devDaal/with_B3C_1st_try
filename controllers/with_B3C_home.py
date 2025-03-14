from views.main import View
from models.main import Model

class With_B3C_Controller:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["left_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.home_page) 
        self.frame.send_home_btn.config(command = self.homing_page)
        self.frame.PH10_tester_btn.config(command = self.say_hello)      
        
    def home_page(self):
        self.view.switch("startpage")
        
    def homing_page(self):
        self.view.switch("homing_page")
    
    def say_hello(self):
        self.model.hello.say_hello()