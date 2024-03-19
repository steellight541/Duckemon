from pygame import event, key, mouse, QUIT

class Events:
    """
    This class is used to get events from the window.
    """
    def QUIT_event(self):
        return QUIT
    
    def get_events(self):
        return event.get()

    def get_key(self, _key):
        return key.get_pressed()[_key]
    
    def get_mouse_pos(self):
        return mouse.get_pos()
    
    def get_mouse_click(self):
        return mouse.get_pressed()
    
    def get_all_keys(self):
        return key.get_pressed()