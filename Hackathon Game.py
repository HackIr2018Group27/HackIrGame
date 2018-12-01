import os 
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0) #sets screen to top left corner

from pygame import * 

init()
size = width, height = 1000, 700
screen = display.set_mode(size)

# defining colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
font = font.SysFont("Times New Roman",50)
# setting states for the menu
state = 'MAIN'
running = True # boolean to control game loop
myClock = time.Clock()
button = mx = my = 0 # initialize button, and mouse x and y
mousebox = Rect(mx, my, 1, 1)

buttonList = [Rect(350, 150, 300, 100), Rect(350, 300, 300, 100),
              Rect(350, 450, 300, 100), Rect(350, 600, 300, 100)]

# method to display the main menu
def drawMenu(mousebox):
    if state == 'MAIN':
        mainMenuBackground = image.load("Main Background.png")         
        screen.blit(mainMenuBackground, Rect(0, 0, width, height))
        
        logo = image.load("Logo.png")         
        #screen.blit(logo, Rect(300, 0, 300, 200))
        logoTransformed = transform.scale(logo, (300, 300))
        screen.blit(logoTransformed, (350, 0))        
        
        #for displaying the local box
        draw.rect(screen, WHITE, buttonList[1])
        localButton = image.load("Local Button.png")         
        screen.blit(localButton, Rect(350, 300, 300, 100))        
        
        #for displaying the online box
        draw.rect(screen, WHITE, buttonList[2])
        onlineButton = image.load("Online Button.png")         
        screen.blit(onlineButton, Rect(350, 450, 300, 100))   
        
        # for displaying the quit box
        draw.rect(screen, WHITE, buttonList[3])
        quitButton = image.load("Quit Button.png")         
        screen.blit(quitButton, Rect(350, 600, 300, 100))         
    
    elif state == 'LOCAL':
        localBackground = image.load("Local Background.png")         
        screen.blit(localBackground, Rect(0, 0, width, height))       
                    
        # for displaying the easy local box
        draw.rect(screen, WHITE, buttonList[0])
        easyButton = image.load("Easy Button.png")         
        screen.blit(easyButton, buttonList[0])         
        
        #for displaying the hard local box
        draw.rect(screen, WHITE, buttonList[1])
        hardButton = image.load("Hard Button.png")         
        screen.blit(hardButton, buttonList[1])          
        
        # for displaying the local disco box
        draw.rect(screen, WHITE, buttonList[2])
        discoButton = image.load("Disco Button.png")         
        screen.blit(discoButton, buttonList[2])          
    
    elif state == 'ONLINE':
        onlineBackground = image.load("Online Background.png")         
        screen.blit(onlineBackground, Rect(0, 0, width, height))
        
        # for displaying the easy online box
        draw.rect(screen, WHITE, buttonList[0])
        easyButton = image.load("Easy Button.png")         
        screen.blit(easyButton, buttonList[0])         
            
        
        #for displaying the normal online box
        draw.rect(screen, WHITE, buttonList[1])
        normalButton = image.load("Normal Button.png")         
        screen.blit(normalButton, buttonList[1])        
        
        # for displaying the hard online box
        draw.rect(screen, WHITE, buttonList[2])
        hardButton = image.load("Hard Button.png")         
        screen.blit(hardButton, buttonList[2])         
        
        # for displaying the online disco box
        draw.rect(screen, WHITE, buttonList[3]) 
        discoButton = image.load("Disco Button.png")         
        screen.blit(discoButton, buttonList[3])          

while running: # do as long as running is true
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT: #check if X has been clicked on screen
            running = False # set boolean to False will quit loop
        if evnt.type == MOUSEBUTTONDOWN: # check if button pressed 
            mx, my = evnt.pos    # grab the mouse x and y      
            button = evnt.button # grab the button that was pressed
            mousebox = Rect(mx, my, 1, 1)
            
            if button == 1:
                if state == 'MAIN':
                    if buttonList[1].colliderect(mousebox):
                        state = 'LOCAL'
                    elif buttonList[2].colliderect(mousebox):
                        state = 'ONLINE'
                    elif buttonList[3].colliderect(mousebox):
                        running = False
                        
                elif state == 'LOCAL':
                    if buttonList[0].colliderect(mousebox):
                        state = 'LOCALEASY'
                    elif buttonList[1].colliderect(mousebox):
                        state = 'LOCALHARD'
                    elif buttonList[2].colliderect(mousebox):
                        state = 'LOCALDISCO'
                        
                elif state == 'ONLINE':
                    if buttonList[0].colliderect(mousebox):
                        state = 'ONLINEEASY'
                    elif buttonList[1].colliderect(mousebox):
                        state = 'ONLINENORMAL'
                    elif buttonList[2].colliderect(mousebox):
                        state = 'ONLINEHARD'
                    elif buttonList[3].colliderect(mousebox):
                        state = 'ONLINEDISCO'
        if evnt.type == KEYDOWN:
            if evnt.key == K_ESCAPE:
                state = 'MAIN'
    drawMenu(mousebox) # draw the menu   
    button = 0 # resetting button to 0 every time through the loop.  Why?
    myClock.tick(60)
    display.flip()
quit()