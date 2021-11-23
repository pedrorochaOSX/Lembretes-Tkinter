class Lembrete:
    def __init__(self, data:str, info:str):
        self.data = data
        self.info = info

    def set_info(self, info:str):
        self.info = info

    def set_data(self, data:str):
        self.data = data     

    def get_data(self):
      return self.data
    
    def get_info(self):
        return self.info  
        

    def __repr__(self):
        return f'{self.data}  |  {self.info}'
