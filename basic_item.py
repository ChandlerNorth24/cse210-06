from object_found import object_found
from point import Point
from color import Color
import constants

class basic_item(object_found):

    def __init__(self, point):

        super().__init__()
        self._text = "$"
        self._font_size = 15
        self._color = Color(245,245,245)
        self._position = Point(point._x, point._y)
        self._velocity = Point(0,0)

    def found_object(self):
        pass
    