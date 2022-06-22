class Consumer:

    def __init__(self, service):
            self.__service = service
    
    RUNNING = True  # class attribute

    def start(self):
            
        while self.RUNNING:
            updates = self.__service.check_for_updates()
            print(updates)  # just and example