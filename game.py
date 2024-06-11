import pygame as pg
import sys
import time
from aiplayer import *

def main():

    pg.init()
    
    clock = pg.time.Clock()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    size = width, height = 1440, 900
    white = (255, 255, 255)
    black = (0, 0, 0)
    gameOver = False
    winner = ""
    playerCount = None
    
    player = None
    screenTitle = True
    drawBoard = True
    boardList = []
    boardListX = []
    boardListO = []
    
    smallFont = pg.font.Font("OpenSans-Regular.ttf", 75)
    mediumFont = pg.font.Font("OpenSans-Regular.ttf", 90)
    largeFont = pg.font.Font("OpenSans-Regular.ttf", 130)
    moveFont = pg.font.Font("OpenSans-Regular.ttf", 320)

    markerX = moveFont.render("X", True, white)
    markerXrect = markerX.get_rect()
    markerO = moveFont.render("O", True, white)
    markerOrect = markerO.get_rect()
    
    for i in range(9):
        boardList.append(0)
        boardListO.append(0)
        boardListX.append(0)

    while True:
        #exit function
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
                
        # let player choose player couunt
        if playerCount == None:
            #make buttons
            buttonOneP = pg.Rect(round(width/7), height- 250, (round(width/7 * 2)), 150)
            buttonTwoP = pg.Rect(round(width/7) * 4, height - 250, (round(width/7) * 2), 150)
            pg.draw.rect(screen, white, buttonOneP)
            pg.draw.rect(screen, white, buttonTwoP)
            #text on buttons
            onePtext = smallFont.render("En spelare", True, black)
            onePtextRect = onePtext.get_rect()
            onePtextRect.center = buttonOneP.center
            screen.blit(onePtext, onePtextRect)
            twoPtext = smallFont.render("Två spelare", True, black)
            twoPtextRect = twoPtext.get_rect()
            twoPtextRect.center = buttonTwoP.center
            screen.blit(twoPtext, twoPtextRect)
            #clickable
            click, _, _ = pg.mouse.get_pressed()
            if click == 1:
                mouse = pg.mouse.get_pos()
                if buttonOneP.collidepoint(mouse):
                    playerCount = 1
                    time.sleep(0.3)
                elif buttonTwoP.collidepoint(mouse):
                    playerCount = 2
                    player = "X"
                    playerNow = "X"
                    time.sleep(0.3)
        #pick side screen
        elif player == None and playerCount == 1:
            #draw buttons
            title = largeFont.render("Tre I Rad", True, white)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), 70)
            screen.blit(title, titleRect)
            buttonX = pg.Rect(round(width/7), height- 250, (round(width/7 * 2)), 150)
            buttonO = pg.Rect(round(width/7) * 4, height - 250, (round(width/7) * 2), 150)
            pg.draw.rect(screen, white, buttonX)
            pg.draw.rect(screen, white, buttonO)
            
            #text on buttons
            Xtext = mediumFont.render("Välj X", True, black)
            XtextRect = Xtext.get_rect()
            XtextRect.center = buttonX.center
            screen.blit(Xtext, XtextRect)
            Otext = mediumFont.render("Välj O", True, black)
            OtextRect = Otext.get_rect()
            OtextRect.center = buttonO.center
            screen.blit(Otext, OtextRect)
            
            #button interaction
            click, _, _ = pg.mouse.get_pressed()
            if click == 1:
                mouse = pg.mouse.get_pos()
                if buttonX.collidepoint(mouse):
                    player = "X"
                    playerNow = "X"
                    time.sleep(0.2)
                elif buttonO.collidepoint(mouse):
                    player = "O"
                    playerNow = "X"
                    time.sleep(0.2)
                    
        #play screen
        else:
            if drawBoard == True:
                screen.fill("black")
                playSquare = []
                x = width/5
                y = (height - (width/5 * 3))/2
                for i in range(3):
                    for o in range(1, 4):
                        playSquare.append(pg.Rect(x * o, y + (i * width/5), width/5, width/5))        
                for i in range(9):
                    pg.draw.rect(screen, white, playSquare[i], 5, border_radius=1)
                borderSquare = pg.Rect(width/5, y, width/5 * 3, width/5 * 3)
                pg.draw.rect(screen, white, borderSquare, 10, border_radius=1)
                drawBoard = False
                
            
            else:
                if gameOver == False:
                    if playerCount == 1:
                        if player == playerNow:
                            click, _, _ = pg.mouse.get_pressed()
                            if click == 1:
                                mouse = pg.mouse.get_pos()
                                for i in range(9):
                                    if playSquare[i].collidepoint(mouse):
                                        if boardList[i] == 0:
                                            if playerNow == "X":
                                                markerXrect.center = playSquare[i].center
                                                screen.blit(markerX, markerXrect)
                                                boardList[i] = 1
                                                boardListX[i] = 1
                                                if evaluate(boardList) == 0:
                                                    winner = "tie"
                                                    gameOver = True
                                                    screen.fill("black")
                                                elif evaluate(boardList) == 1:
                                                    winner = "X"
                                                    gameOver = True
                                                    screen.fill("black")
                                                playerNow = "O"
                                                time.sleep(0.15)
                                            else:
                                                markerOrect.center = playSquare[i].center
                                                screen.blit(markerO, markerOrect)
                                                boardList[i] = -1
                                                boardListO[i] = 1
                                                if evaluate(boardList) == 0:
                                                    winner = "tie"
                                                    gameOver = True
                                                    screen.fill("black")
                                                elif evaluate(boardList) == -1:
                                                    winner = "O"
                                                    gameOver = True
                                                    screen.fill("black")
                                                playerNow = "X"
                                                time.sleep(0.15)
                        else:
                            aiaction = play(boardList)
                            time.sleep(0.1)
                            if player == "X":
                                markerOrect.center = playSquare[aiaction].center
                                screen.blit(markerO, markerOrect)
                                boardList[aiaction] = -1
                                boardListO[aiaction] = -1
                                if evaluate(boardList) == 0:
                                    winner = "tie"
                                    gameOver = True
                                    screen.fill("black")
                                elif evaluate(boardList) == -1:
                                    winner = "O"
                                    gameOver = True
                                    screen.fill("black")
                                playerNow = "X"
                                time.sleep(0.15)
                            else:
                                markerXrect.center = playSquare[aiaction].center
                                screen.blit(markerX, markerXrect)
                                boardList[aiaction] = 1
                                boardListX[aiaction] = 1
                                if evaluate(boardList) == 0:
                                    winner = "tie"
                                    gameOver = True
                                    screen.fill("black")
                                elif evaluate(boardList) == 1:
                                    winner = "X"
                                    gameOver = True
                                    screen.fill("black")
                                playerNow = "O"
                                time.sleep(0.15)
                                
                    if playerCount == 2:
                        
                        if playerNow == "X":
                            
                            boxhiderRect = pg.Rect(50, 70, 220, 200)
                            pg.draw.rect(screen, black, boxhiderRect)
                            turnText = smallFont.render("Xs tur", True, white)
                            turnRect = turnText.get_rect()
                            turnRect.center = (170, 140)
                            screen.blit(turnText, turnRect)
                        else:
                            boxhiderRect = pg.Rect(50, 70, 220, 200)
                            pg.draw.rect(screen, black, boxhiderRect)
                            turnText = smallFont.render("Os tur", True, white)
                            turnRect = turnText.get_rect()
                            turnRect.center = (170, 140)
                            screen.blit(turnText, turnRect)
                            
                    click, _, _ = pg.mouse.get_pressed()
                    if click == 1:
                        mouse = pg.mouse.get_pos()
                        for i in range(9):
                            if playSquare[i].collidepoint(mouse):
                                if boardList[i] == 0:
                                    if playerNow == "X":
                                        markerXrect.center = playSquare[i].center
                                        screen.blit(markerX, markerXrect)
                                        boardList[i] = 1
                                        boardListX[i] = 1
                                        if evaluate(boardList) == 0:
                                            winner = "tie"
                                            gameOver = True
                                            screen.fill("black")
                                        elif evaluate(boardList) == 1:
                                            winner = "X"
                                            gameOver = True
                                            screen.fill("black")
                                        playerNow = "O"
                                        time.sleep(0.15)
                                    else:
                                        markerOrect.center = playSquare[i].center
                                        screen.blit(markerO, markerOrect)
                                        boardList[i] = -1
                                        boardListO[i] = 1
                                        if evaluate(boardList) == 0:
                                            winner = "tie"
                                            gameOver = True
                                            screen.fill("black")
                                        elif evaluate(boardList) == -1:
                                            winner = "O"
                                            gameOver = True
                                            screen.fill("black")
                                        playerNow = "X"
                                        time.sleep(0.15)
                else:
                    match winner:
                        case "X":
                            Xwin = largeFont.render("X vinner", True, white)
                            XwinRect = Xwin.get_rect()
                            XwinRect.center = ((width / 2), 70)
                            screen.blit(Xwin, XwinRect)
                        case "O":
                            Owin = largeFont.render("O vinner", True, white)
                            OwinRect = Owin.get_rect()
                            OwinRect.center = ((width / 2), 70)
                            screen.blit(Owin, OwinRect)
                        case "tie":
                            Tie = largeFont.render("Oavgjort, ingen vinner", True, white)
                            TieRect = Tie.get_rect()
                            TieRect.center = ((width / 2), 70)
                            screen.blit(Tie, TieRect)
                    buttonRestart = pg.Rect(round(width/7), height- 250, (round(width/6 * 2)), 150)
                    buttonQuit = pg.Rect(round(width/7) * 4, height - 250, (round(width/6) * 2), 150)
                    pg.draw.rect(screen, white, buttonRestart)
                    pg.draw.rect(screen, white, buttonQuit)
                    
                    RestartText = smallFont.render("Spela igen", True, black)
                    RestartTextRect = RestartText.get_rect()
                    RestartTextRect.center = buttonRestart.center
                    screen.blit(RestartText, RestartTextRect)
                    QuitText = smallFont.render("Avsluta spel", True, black)
                    QuitTextRect = QuitText.get_rect()
                    QuitTextRect.center = buttonQuit.center
                    screen.blit(QuitText, QuitTextRect)
                    
                    click, _, _ = pg.mouse.get_pressed()
                    if click == 1:
                        mouse = pg.mouse.get_pos()
                        if buttonRestart.collidepoint(mouse):
                            time.sleep(0.2)
                            main()
                        elif buttonQuit.collidepoint(mouse):
                            sys.exit()
                #implementera funkitonallitet för knappar call main()
        pg.display.flip()
        clock.tick(60)

def evaluate(boardState):
    if abs(boardState[0] + boardState[1] + boardState[2]) == 3:
        if boardState[0] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[3] + boardState[4] + boardState[5]) == 3:
        if boardState[3] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[6] + boardState[7] + boardState[8]) == 3:
        if boardState[6] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[0] + boardState[3] + boardState[6]) == 3:
        if boardState[0] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[1] + boardState[4] + boardState[7]) == 3:
        if boardState[1] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[2] + boardState[5] + boardState[8]) == 3:
        if boardState[2] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[0] + boardState[4] + boardState[8]) == 3:
        if boardState[0] == -1:
            return -1
        else:
            return 1
    elif abs(boardState[2] + boardState[4] + boardState[6]) == 3:
        if boardState[2] == -1:
            return -1
        else:
            return 1
    elif 0 not in boardState:
        return 0
    else:
        return 2

if __name__ == '__main__':
    main()