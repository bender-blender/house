from interface import Builder
from house import House



class BuilderCottage(Builder):
    """Строитель Коттедж

    Args:
        Builder (_type_): _description_
    """
    def __init__(self):
        self.house = House()

    def add_door(self,door:str):
        self.house.door = door
        return self
    
    def add_window(self,window:int):
        self.house.window = window
        return self
    
    def add_wall(self,wall:str):
        self.house.wall = wall
        return self
    
    def add_chimney(self,chimney:str):
        self.house.chimney = chimney
        return self
    
    def add_material(self,material:list):
        self.house.material = material
        return self
    
    def builder(self):
        return self.house
    


class BuilderApartment(Builder):
    """Строитель Квартира

    Args:
        Builder (_type_): _description_
    """
    def __init__(self):
        self.house = House()

    def add_door(self,door:str):
        self.house.door = door
        return self
    
    def add_window(self,window:int):
        self.house.window = window
        return self
    
    def add_wall(self,wall:str):
        self.house.wall = wall
        return self
    
    def add_chimney(self,chimney:str):
        self.house.chimney = chimney
        return self
    
    def add_material(self,material:list):
        self.house.material = material
        return self
    
    def builder(self):
        return self.house