HEIGHT = 900
WIDTH = 1500
import pyray
import constants
from datetime import datetime

class OutputService():
    def __init__(self, player):
        pass
        self._cur_time = datetime.now()
        self._player = player

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
    
    def draw_actor(self, actor):
        if actor.has_actors() == True:
            for member in actor.get_actors():
                self.draw_single_actor(member)
        else:
            self.draw_single_actor(actor)

    def draw_single_actor(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x() - (self._player.get_position().get_x() - constants.MAX_X / 2)
        y = actor.get_position().get_y() - (self._player.get_position().get_y() - constants.MAX_Y / 2)
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        pyray.draw_text(text, int(x), int(y), font_size, color)
    def draw_player(self, actor):
        center_x = constants.MAX_X / 2
        center_y = constants.MAX_Y / 2
        text = actor.get_text()
        x = center_x
        y = center_y
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        pyray.draw_text(text, int(x), int(y), font_size, color)
    def draw_display(self, actor):
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        pyray.draw_text(text, int(x), int(y), font_size, color)

    def flush_buffer(self):
        pyray.end_drawing()

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.TITLE)
        pyray.set_target_fps(constants.FRAME_RATE)

    def do_updates(self):
        self._prev_time = self._cur_time
        self._cur_time = datetime.now()

    def get_delta_time(self): #returns change in time since last update in seconds
        delta_time = self._cur_time - self._prev_time #DOES NOT return float, returns timedelta object due to datetime API
        return delta_time.total_seconds() #DOES return float

