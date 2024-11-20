

class House:
    """Дом
    """
    def __init__(self):
        self.door = None
        self.window = None
        self.wall = None
        self.material = None
        self.chimney = False
    
    def __str__(self) -> str:
        return f"Дверь:{self.door}\nОкна:{self.window}\nСтены:{self.wall}\nМатериалы:{self.material}\nДымоход:{self.chimney}"
