HEIGHT = 900
WIDTH = 1500
import pyray
import constants

class OutputService:
    def __init__(self):
        pass

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
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        pyray.draw_text(text, x, y, font_size, color)

    def flush_buffer(self):
        pyray.end_drawing()

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.TITLE)
        pyray.set_target_fps(constants.FRAME_RATE)
        
