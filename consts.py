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

    RIGHT_ATTACK = Container([Container([35,20]), Container([70,50])])
    RIGHT_DOWN_ATTACK = Container([Container([50,50]), Container([70,70])])
    DOWN_ATTACK = Container([Container([20,50]), Container([50,70])])
    LEFT_DOWN_ATTACK = Container([Container([0,50]), Container([20,70])])
    LEFT_ATTACK = Container([Container([0,20]), Container([50,50])])
    LEFT_UP_ATTACK = Container([Container([0,0]), Container([20,20])])
    UP_ATTACK = Container([Container([20,0]), Container([50,20])])
    RIGHT_UP_ATTACK = Container([Container([50,0]), Container([70,20])])

    ATTACK_CONTAINER = Container([UP_ATTACK, RIGHT_UP_ATTACK, RIGHT_ATTACK, RIGHT_DOWN_ATTACK, DOWN_ATTACK, LEFT_DOWN_ATTACK, LEFT_ATTACK, LEFT_UP_ATTACK])
