from views.main import View
from models.main import Model

class Sensors_Controller:
    
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["sensors_page"]
        self._bind()
        
    def _bind(self):
        self.frame.exit_btn.config(command = self.home_page)
    
    
    def home_page(self):
        self.view.switch("left_page")