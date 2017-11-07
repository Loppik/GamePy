from logic.Container import Container

class Consts:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800


    UP_DIRECTION = 0
    RIGHT_DIRECTION = 1
    DOWN_DIRECTION = 2
    LEFT_DIRECTION = 3

    WALK_1_CELL = Container([Container([70,0]), Container([0, -70]), Container([-70, 0]), Container([0, 70])])

    WALK_2_CELL = Container([Container([70,0]), Container([0, -70]), Container([-70, 0]), Container([0, 70]),
                             Container([140,0]), Container([0, -140]), Container([-140,0]), Container([0,140]),
                             Container([70,70]), Container([70,-70]), Container([-70,-70]), Container([-70,70])])

    WALK_3_CELL = Container([Container([70,0]), Container([0, -70]), Container([-70, 0]), Container([0, 70]),
                             Container([140,0]), Container([0, -140]), Container([-140,0]), Container([0,140]),
                             Container([70,70]), Container([70,-70]), Container([-70,-70]), Container([-70,70]),
                             Container([210,0]), Container([0,-210]), Container([-210,0]), Container([0,210]),
                             Container([70,140]), Container([140,70]), Container([70,-140]),
                             Container([140,-70]), Container([-140,70]),
                             Container([-70,-140]), Container([-140,-70]),
                             Container([-140,70]), Container([-70,140])])