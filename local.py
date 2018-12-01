from pygame import *
from math import *
import random




def game(difficulty, suddenDeath, boundX, boundY, screen):

    init()
    import entities

    ORANGE = (253,102,0)
    BLUE = (0,120,255)

    background = image.load("TODO").convert_alpha()
    fontGeneral = font.Font('resources/fonts/Calibri.ttf', 30)

    intro = [image.load().convert_alpha(), image.load().convert_alpha(), image.load().convert_alpha(), image.load().convert_alpha()]
    radius = 25
    bulletRadius = 25
    firingSpeed = 333

    running = True

    controls = True

    player1 = entities.Player(250, 350, suddenDeath, ORANGE, radius)
    player1Bullets = []
    player1gun = [False, False, False, False]
    startTicks1 = 0
    wins1 = 0

    player2 = entities.Player(250, 350, suddenDeath, BLUE, radius)
    player2Bullets = []
    player2gun = [False, False, False, False]
    startTicks2 = 0
    wins2 = 0


    bulletDirectionsX = [0, 0, -10, 10]

    bulletDirectionsY = [10, -10, 0, 0]

    screen.blit(background, (0,0))

    player1.draw(screen)

    player2.draw(screen)

    display.flip()

    for photo in intro:

        screen.blit(photo, ((boundX/2)-(photo.get_width/2)), ((boundY/2)-(photo.get_height/2)))
        display.flip()
        time.wait(2000)


    while running:


        for evnt in event.get():
            if evnt.type == QUIT:
                quit()

            if controls:
                if evnt.type == KEYDOWN:
                    # handles keyboard movement (if key pressed, corresponding direction = True)
                    if evnt.key == K_w:
                        player1.directions[0] = True
                    if evnt.key == K_s:
                        player1.directions[1] = True
                    if evnt.key == K_a:
                        player1.directions[2] = True
                    if evnt.key == K_d:
                        player1.directions[3] = True

                    if evnt.key == K_f:
                        player1gun[0] = True
                    if evnt.key == K_v:
                        player1gun[1] = True
                    if evnt.key == K_c:
                        player1gun[2] = True
                    if evnt.key == K_b:
                        player1gun[3] = True

                    if evnt.key == K_i:
                        player2.directions[0] = True
                    if evnt.key == K_k:
                        player2.directions[1] = True
                    if evnt.key == K_j:
                        player2.directions[2] = True
                    if evnt.key == K_l:
                        player2.directions[3] = True

                    if evnt.key == K_UP:
                        player2gun[0] = True
                    if evnt.key == K_DOWN:
                        player2gun[1] = True
                    if evnt.key == K_LEFT:
                        player2gun[2] = True
                    if evnt.key == K_RIGHT:
                        player2gun[3] = True


                # sets apt. directions to false if key is no longer pressed
                if evnt.type == KEYUP:

                    if evnt.key == K_w:
                        player1.directions[0] = False
                    if evnt.key == K_s:
                        player1.directions[1] = False
                    if evnt.key == K_a:
                        player1.directions[2] = False
                    if evnt.key == K_d:
                        player1.directions[3] = False

                    if evnt.key == K_f:
                        player1gun[0] = False
                    if evnt.key == K_v:
                        player1gun[1] = False
                    if evnt.key == K_c:
                        player1gun[2] = False
                    if evnt.key == K_b:
                        player1gun[3] = False

        for dir in range(len(player1gun)):
            if player1gun[dir]:
                if time.get_ticks() - startTicks1 > firingSpeed:

                    if difficulty:
                        player1.show = 30

                    player1Bullets.append(entities.Bullet(player1.x, player1.y, player1.x + bulletDirectionsX[dir], player1.y + bulletDirectionsY[dir], player2, player1Bullets, ORANGE, bulletRadius, boundX, boundY))
                    startTicks1 = time.get_ticks()

            if player2gun[dir]:
                if time.get_ticks() - startTicks2 > firingSpeed:

                    if difficulty:
                        player1.show = 30

                    player2.show = 30
                    player1Bullets.append(entities.Bullet(player2.x, player2.y, player2.x + bulletDirectionsX[dir], player2.y + bulletDirectionsY[dir], player1, player2Bullets, BLUE, bulletRadius, boundX, boundY))
                    startTicks2 = time.get_ticks()

        player1.update(player2, player2Bullets)

        player2.update(player1, player1Bullets)

        """drawing everything"""

        screen.blit(background, (0,0))

        for bullet in player1Bullets:

            bullet.update()
            bullet.check(player2)
            bullet.draw(screen)

        for bullet in player2Bullets:

            bullet.update()
            bullet.check(player1)
            bullet.draw(screen)



        if not difficulty:

            player1.draw(screen)

            player2.draw(screen)

        else:

            if(player1.show > 0):
                player1.draw(screen)

            if(player2.show > 0):
                player2.draw(screen)


            player1.show -= 1

            player2.show -= 2

            text = fontGeneral.render(str(wins1), 1, ORANGE)
            screen.blit(text, (30, boundY - 45, 40, 40))

            text = fontGeneral.render(str(wins2), 1, BLUE)
            screen.blit(text, (boundX - 30, boundY - 45, 40, 40))



        if player2.health <= 0 or player1.health <= 0:

            controls = False

            screen.blit(background, (0, 0))

            if not player1.health:
                player2.draw(screen)

                wins2 += 1

            else:
                player1.draw(screen)
                wins1 += 1

            if wins1 >= 3:

                text = fontGeneral.render("Player 1 wins!", 1, ORANGE)
                screen.blit(text, Rect((boundX/2)-(text.get_width()/2), (boundY/2)-(text.get_height()/2), text.get_width(), text.get_height()))

                display.flip()
                time.wait(2000)

                return 1

            elif wins2 >=3:

                text = fontGeneral.render("Player 2 wins!", 1, BLUE)
                screen.blit(text, Rect((boundX / 2) - (text.get_width() / 2), (boundY / 2) - (text.get_height() / 2),
                                       text.get_width(), text.get_height()))


                display.flip()
                time.wait(2000)

                return 1




        display.flip()
















