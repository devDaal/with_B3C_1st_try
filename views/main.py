from typing import TypedDict
from .startpage import StartPageview
from .with_B3C_home import with_B3C_HomePage
from .settings import Settingsview
from .homing import Homingview
from .root import Root


class Frames(TypedDict):
    startpage: StartPageview
    
class View:
    
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}
        
        self._add_frame(Homingview, 'homing_page')
        self._add_frame(Settingsview, 'settings_page')
        self._add_frame(with_B3C_HomePage, 'left_page')
        self._add_frame(StartPageview, 'startpage') #Last page here is going to be top page at screen
        
        
    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")
        
    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()
        
    def start_mainloop(self) -> None:
        self.root.mainloop()