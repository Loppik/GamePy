import pygame, sys

pygame.init()
size = width, height = 1000, 800

screen = pygame.display.set_mode(size)


i = 0
j = 0
map_cell_pos = [0, 70, 140, 210, 280, 350, 420, 490, 560, 630, 700, 770, 840]


cell = pygame.image.load("cell2.png")
cell1 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[0]))
cell2 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[1]))
cell3 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[2]))
cell4 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell5 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[4]))
cell6 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[5]))
cell7 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[6]))
cell8 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[7]))
cell9 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[8]))
cell10 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[9]))
cell11 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[10]))
cell12 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell13 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell14 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell15 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell16 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell17 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell18 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell19 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))
cell20 = cell.get_rect(topleft=(map_cell_pos[0], map_cell_pos[3]))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if cell1.collidepoint(mouse_pos):
                print("1")



    screen.fill((255, 255, 255))

    screen.blit(cell, cell1)
    screen.blit(cell, cell2)
    screen.blit(cell, cell3)
    screen.blit(cell, cell4)
    screen.blit(cell, cell5)
    screen.blit(cell, cell6)
    screen.blit(cell, cell7)
    screen.blit(cell, cell8)
    screen.blit(cell, cell9)
    screen.blit(cell, cell10)

    pygame.display.flip()