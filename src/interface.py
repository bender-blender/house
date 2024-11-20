
from abc import abstractmethod,ABC

class Builder(ABC):
    """Строитель

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def add_door(self):
        """Добавить двери

        Args:
            door (str): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    @abstractmethod
    def add_window(self):
        """Добавить окна

        Args:
            window (int): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    @abstractmethod
    def add_wall(self):
        """Добавить стены

        Args:
            wall (str): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    @abstractmethod
    def add_material(self):
        """Материалы

        Args:
            material (list): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    @abstractmethod
    def add_chimney(self):
        """Добавить дымоход

        Args:
            chimney (bool): _description_

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError