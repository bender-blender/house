

from house import House

class Builder:
    """Строитель
    """

    def __init__(self):
        self.house = House()
    
    def add_name(self,name:str):
        self.house.name = name
        return self

    def add_door(self,door:str):
        """Добавить двери
        """
        self.house.door = door
        return self

        
    
    def add_window(self,window:int):
        """Добавить окна        
        """
        self.house.window = window
        return self 
    
    def add_wall(self,wall:str):
        """Добавить стены
        """
        self.house.wall = wall
        return self

    
    def add_material(self,material:list):
        """Материалы
        """
        self.house.material = material
        return self
        
    
    
    def add_chimney(self,chimney:bool):
        """Добавить дымоход        
        """
        self.house.chimney = chimney
        return self
    
    def create_room(self,count:int):
        """Создать комнаты
        """
        for i in range(count):
            self.house.room.append([])
    
    def build(self):
        return self.house