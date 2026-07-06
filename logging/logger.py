# Logging module.

class Logger:

    # Initialize module.
    def __init__(self, module_name:str)->None:
        self.__setattr__("name", module_name)
    
    # Log output
    def log(self, x:str):
        print(f"[ LOG ] >> [ {self.__getattribute__("name")} ] >> {x} ||")
    
    # Log module loading.
    def init_log(self, x:str=""):
        print(f"[ INIT ] >> [ {self.__getattribute__("name")} ] >> {x if x else "SUCCESS"} ||")
    
    # Log module error.
    def error_log(self, x:str):
        print(f"[ ERROR ] >> [ {self.__getattribute__("name")} ] >> {x} ||")
    
    # Log module warnings.
    def warn_log(self, x:str):
        print(f"[ WARNING ] >> [ {self.__getattribute__("name")} ] >> {x} ||")
    
    # Log module terminating.
    def quit_log(self, x:str):
        print(f"[ QUITTING ] >> [ {self.__getattribute__("name")} ] >> {x} ||")