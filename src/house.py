

class House:
    """Дом
    """

    def __init__(self):
        self.name = None
        self.door = None
        self.window = None
        self.wall = None
        self.material = None
        self.chimney = False
        self.room = []
    




    def __str__(self) -> str:
        return f"Название:{self.name}\nДверь:{self.door}\nОкна:{self.window}\nСтены:{self.wall}\nМатериалы:{self.material}\nДымоход:{self.chimney}\nКомнаты:{self.room}"
