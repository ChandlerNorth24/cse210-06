from action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        items = cast.get_actors("items")
        player = cast.get_first_actor("players")
        self._output_service.clear_buffer()

        self._output_service.draw_player(player)
        for actor in items:
            self._output_service.draw_single_actor(actor)
        
        self._output_service.flush_buffer()