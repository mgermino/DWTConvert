import sys
import pygame
import random



#################
# global colors #
#################
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


###############################
# fills background with white #
###############################
def drawBackGround(screen):
    screen.fill(white)


##############################################
# draws a rectangular box for pong character #
##############################################
def drawCharacterOne(screen, x, y):
    pygame.draw.rect(screen, black, [0+x, 0+y, 10, 50], 0)

def drawCharacterTwo(screen, x, y):
    pygame.draw.rect(screen, black, [630-x, 0+y, 10, 50], 0)


##################
# draws the ball #
##################
def drawBall(screen, x, y):
    pygame.draw.circle(screen, black, (x, y), 7, 0)


def main():

    done = False
    pygame.init()



    frame = 0
    whoseTurn = 2
    firstTurnDisplay = 1

    ###################
    # defining scores #
    ###################
    playerOneScore = 0
    playerTwoScore = 0

    ##############################################################
    # defining fonts that will be used to display scores in-game #
    ##############################################################
    font = pygame.font.Font(None, 15)
    font2 = pygame.font.Font(None, 30)



    ###################
    # defining colors #
    ###################
    white = (255, 255, 255)
    black = (0, 0, 0)

    ############################
    # defining character speed #
    ############################
    ySpeed = 0
    ySpeed2 = 0

    ###############################
    # defining character position #
    ###############################
    xCoord = 10
    xCoord2 = 10
    yCoord = 220
    yCoord2 = 220

    ##########################
    # defining ball position #
    ##########################
    ballX = 320
    ballY = 240
    ballXChange = 0
    ballYChange = 0

    screen = pygame.display.set_mode((640, 480))


    #########################
    # game controlling loop #
    #########################
    while done == False:

        #######################################################
        # game moved too fast so I made it half-speed in O(1) #
        #######################################################

        if frame % 2 == 0:


            #####################
            # boundary checking #
            #####################
            if yCoord == 0:
                ySpeed = 0
            if yCoord == 430:
                ySpeed = 0
            if yCoord2 == 0:
                ySpeed2 = 0
            if yCoord2 == 430:
                ySpeed2 = 0
            if ballY == 5:
                ballYChange = ballYChange*-1
            if ballY == 475:
                ballYChange = ballYChange*-1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        firstTurnDisplay += 1
                        ballXChange = 1*whoseTurn
                    if event.key == pygame.K_SPACE:
                        ballYChange = -1*random.choice([-1, 1])


                ###############################################################################################
                #if user presses a key and therefore makes a move (Player 1: W = up, S = down                 #
                #                                                  Player 2: Up Arrow = up, Down Arrow = down)#
                ###############################################################################################
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if yCoord == 0:
                            ySpeed = 0
                            break
                        ySpeed =- 1

                    if event.key == pygame.K_s:
                        if yCoord == 430:
                            ySpeed = 0
                            break
                        ySpeed = 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if yCoord2 == 0:
                            ySpeed2 = 0
                            break
                        ySpeed2 =- 1

                    if event.key == pygame.K_DOWN:
                        if yCoord2 == 430:
                            ySpeed2 = 0
                            break
                        ySpeed2 = 1

                ##############################
                # if user lets go of the key #
                ##############################
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                            ySpeed = 0
                    if event.key == pygame.K_s:
                            ySpeed = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        ySpeed2 =- 0
                    if event.key == pygame.K_DOWN:
                        ySpeed2 = 0


            ############################
            # if ball touches a paddle #
            ############################
            if (yCoord2<=ballY<=yCoord2+50 and 620<=ballX<=630) or (yCoord<=ballY<=yCoord+50 and 10<=ballX<=20):
                ballXChange = ballXChange*-1
                ballYChange = ballYChange*random.choice([1, -1])


            #############
            # bot logic #
            #############
            #yCoord2 += ballYChange

            ################################
            # if ball hits side, add score #
            ################################
            if ballX == 640:
                playerOneScore += 1
                ballXChange = 0
                ballYChange = 0
                ballX = 320
                ballY = 240
                drawBall(screen, ballX, ballY)
                whoseTurn = 1
                xCoord = 10
                xCoord2 = 10
                yCoord = 220
                yCoord2 = 220

            if ballX == 0:
                playerTwoScore += 1
                ballXChange = 0
                ballYChange = 0
                ballX = 320
                ballY = 240
                drawBall(screen, ballX, ballY)
                whoseTurn = 1
                xCoord = 10
                xCoord2 = 10
                yCoord = 220
                yCoord2 = 220

            drawBackGround(screen)
            pygame.draw.line(screen, black, (320, 0), (320, 480), 2)


            ###################################################
            # moves the character depending on keyboard input #
            ###################################################
            yCoord = yCoord + ySpeed
            drawCharacterOne(screen, xCoord, yCoord)
            yCoord2 = yCoord2 + ySpeed2
            drawCharacterTwo(screen, xCoord2, yCoord2)

            ###################
            # displays scores #
            ###################
            screen.blit(font.render("Score: %d" % playerOneScore, True, black, white), (120, 20), None, 0)
            screen.blit(font.render("Score: %d" % playerTwoScore, True, black, white), (470, 20), None, 0)


            if firstTurnDisplay == 1:
                screen.blit(font.render("--------->PRESS SPACE TO START<---------", True, black, white), (200, 200), None, 0)
                screen.blit(font.render("UP = W", True, black, white), (25, 220), None, 0)
                screen.blit(font.render("DOWN = S", True, black, white), (25, 245), None, 0)
                screen.blit(font.render("UP = UpArrow", True, black, white), (520, 220), None, 0)
                screen.blit(font.render("DOWN = DownArrow", True, black, white), (480, 245), None, 0)


            #######################################################################
            # if either play has a score greater than 10 and is up by 2, they win #
            #######################################################################
            if playerOneScore >= 10 and playerOneScore - playerTwoScore > 1:
                screen.blit(font2.render("Player One Wins!!!", True, black, white), (228, 200), None, 0)
            elif playerTwoScore >= 10 and playerTwoScore - playerOneScore > 1:
                screen.blit(font2.render("Player Two Wins!!!", True, black, white), (228, 200), None, 0)




            ballX += ballXChange
            ballY += ballYChange


        drawBall(screen, ballX, ballY)
        pygame.display.flip()
        #frame += 1



if __name__ == "__main__":
    main()
