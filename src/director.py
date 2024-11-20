from builders import (
    BuilderCottage,
    BuilderApartment
)




class DirectorCottage:
    """Директор Коттедж
    """

    def __init__(self,builder:BuilderCottage):
        self.builder = builder

    def construct_cottage(self):
        self.builder.add_door("Стеклянная")
        self.builder.add_window(10)
        self.builder.add_wall("Беттон")
        self.builder.add_chimney("Присутствует")
        self.builder.add_material(["Беттон","Гипсокартон","Камень"])
        return self.builder.house
    
class DirectorApartament:
    """Директор Квартира
    """

    def __init__(self,builder:BuilderApartment):
        self.builder = builder

    def construct_apartament(self):
        self.builder.add_door("Деревянная")
        self.builder.add_window(4)
        self.builder.add_wall("Беттон")
        self.builder.add_chimney("Отсутствует")
        self.builder.add_material(["Беттон"])
        return self.builder.house
