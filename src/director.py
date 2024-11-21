
from builder import Builder

class CottageDirector:
    """Директор Коттеджа
    """

    def __init__(self):
        self.builder = Builder()
    
    def build(self):
        """Построить дом
        """
        self.builder.add_name("Коттедж")
        self.builder.add_door("Стеклянная")
        self.builder.add_wall("Бетон")
        self.builder.add_window(10)
        self.builder.add_material(["Гипсокартон","Бетон"," Дерево","Стекло"])
        self.builder.add_chimney(True)
        self.builder.create_room(8)
        return self.builder.house

class ApartamentDirector:
    """Директор Квартиры 
    """
    def __init__(self):
        self.builder = Builder()
    
    def build(self):
        """Построить дом
        """
        self.builder.add_name("Квартира")
        self.builder.add_door("Деревянная")
        self.builder.add_wall("Бетон")
        self.builder.add_window(10)
        self.builder.add_material(["Бетон"," Дерево","Стекло","Смеси"])
        self.builder.add_chimney(False)
        self.builder.create_room(3)
        return self.builder.house
    
class ManorDirector:
    """Директор Усадьба
    """
    def __init__(self):
        self.builder = Builder()
    
    def build(self):
        """Построить дом
        """
        self.builder.add_name("Усадьба")
        self.builder.add_door("Деревянная")
        self.builder.add_wall("Мрамор")
        self.builder.add_window(15)
        self.builder.add_material(["Бетон"," Дерево","Стекло","Смеси","Мрамор","Панели","Черепица","Ламинат"])
        self.builder.add_chimney(True)
        self.builder.create_room(15)
        return self.builder.house
