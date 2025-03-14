import threading
import queue
from typing import Callable, TypeVar, Any

Self = TypeVar("Self", bound="ObservableModel")

class ObservableModel:
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = super(ObservableModel, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self._event_listeners: dict[str, list[Callable[[Any], None]]] = {}
            self._event_queue: queue.Queue[tuple[str, Any]] = queue.Queue()
            self._event_thread = threading.Thread(target=self._process_events, daemon=True)
            self._event_thread.start()
        #print(f"{self.__class__.__name__} inicializado correctamente")

        
    
    def add_event_listener(self, event: str, fn: Callable[[Self], None]) -> Callable:
        try:
            self._event_listeners[event].append(fn)
        except KeyError:
            self._event_listeners[event] = [fn]
            
        return lambda: self._event_listeners[event].remove(fn)
    
    def trigger_event(self, event: str) -> None:
        if event not in self._event_listeners:
            return
        self._event_queue.put((event, self))
        
    def _process_events(self):
        while True:
            try:
                event, instance = self._event_queue.get()
                for fn in self._event_listeners.get(event, []):
                    fn(instance)
                self._event_queue.task_done()
            except Exception as e:
                print("Error processing event:", e)
