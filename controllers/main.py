from views.main import View
from models.main import Model

from .startpage import StartPageController
from .with_B3C_home import With_B3C_Controller
from .settings_controller import SettingsController
from .homing_controller import Homing_Controller

class Controller:
    
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.start_page_controller = StartPageController(model, view)
        self.with_B3C_page_controller = With_B3C_Controller(model, view)
        self.settings_page_controller = SettingsController(model, view)
        self.homing_page_controller = Homing_Controller(model, view)
        
        self.model.hello.add_event_listener("Hello", self.hello_world)
        
        self.model.serial_manager.add_event_listener("update_ports",self.update_port_list)
        self.model.serial_manager.add_event_listener("update_connection_status",self.update_connection_status)
        self.model.serial_manager.add_event_listener("unexpected_disconnection",self.unexpected_disconnection)
        
        self.model.homing_routine.add_event_listener("axis_option",self.send_axis_to_protocol_selector)
        
        self.model.protocol_selector.add_event_listener("send_routine",self.send_commands_to_serial_manager)
        
        


   #def event_to_update_view_using_variables_etc_from_model(self, parent):
       #update the view using methods and variables from the model through parent.bla bla bla

    def hello_world(self, parent):
        print(parent.hello_counter, "Hello World!")
        
    def update_port_list(self, parent):
        self.settings_page_controller.update_ports_view()
    
    def update_connection_status(self, parent):
        self.settings_page_controller.update_view_connection_status()
        
    def unexpected_disconnection(self, parent):
        """Inside the main Controller's scope"""
        self.settings_page_controller.unexpected_disconnection()
        
    def send_axis_to_protocol_selector(self, parent):
        self.model.protocol_selector.send_routine_to_serial_manager(self.settings_page_controller.protocol,
                                                                    self.model.homing_routine.axis_option)
        
    def send_commands_to_serial_manager(self, parent):
        self.model.serial_manager.home_routine(self.model.protocol_selector.routine)

    
        

    def start(self) -> None:
        self.view.start_mainloop()