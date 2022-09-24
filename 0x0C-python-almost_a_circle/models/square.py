#!/usr/bin/python3
"""create class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """init class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """overriding str"""
        a, b, c, d = self.id, self.x, self.y, self.width
        return ("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    def update(self, *args, **kwargs):
        """update class args"""
        var_arg = ["id", "size", "x", "y"]
        if (args):
            for i, arg in enumerate(args):
                if i < 4:
                    setattr(self, var_arg[i], arg)
        for key, value in kwargs.items():
            if (hasattr(self, key)):
                setattr(self, key, value)

    def to_dictionary(self):
        """create dictionary"""
        dic_arg = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y}
        return (dic_arg)
