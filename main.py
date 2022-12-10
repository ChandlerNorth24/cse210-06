from cast import Cast
from player import Player
from script import Script
from move_actors_action import MoveActorsAction
from draw_actors_action import DrawActorsAction
from control_actors_action import ControlActorsAction
from director import Director
from output_service import OutputService
from input_service import InputService
from basic_item import basic_item
from point import Point
from load_assets_action import LoadAssetsAction
from unload_assets_action import UnloadAssetsAction


def main():

    cast = Cast()
    player = Player()
    cast.add_actor("players", player)
    addBasicItemsForTesting(cast)
    #add more actors here
    print("added player")

    output_service = OutputService(player)
    #outputservice needs to be started with a player in order to calculate changes due to screen motion
    input_service = InputService()

    script = Script()
    script.add_action("loading", LoadAssetsAction(output_service))
    script.add_action("unloading", UnloadAssetsAction(output_service))
    script.add_action("input", ControlActorsAction(input_service))
    script.add_action("update", MoveActorsAction(output_service))
    #move actors needs output service too because actors need to get deltatime to update their positions
    #which is in output service
    script.add_action("output", DrawActorsAction(output_service))
    #add more scripts here, like collisions

    director = Director(output_service)
    director.start_game(cast, script)

def addBasicItemsForTesting(cast):
    positions = [[45, 45],
        [800, 800],
        [20, 800],
        [1500, 1500]]
    for position in positions:
        testItem = basic_item(Point(position[0], position[1]))
        cast.add_actor("items", testItem)

if __name__ == "__main__":
    main()