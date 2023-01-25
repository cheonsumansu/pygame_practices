import random, pygame, sys
from sys import exit


display_width = 550
display_height = 750

alpaca0 = pygame.image.load("./zzrsource/alpaca00.png")
alpaca1 = pygame.image.load("./zzrsource/alpaca11.png")
alpaca_size = alpaca0.get_rect().size
alpaca_width = alpaca_size[0]
alpaca_height = alpaca_size[1]
#print(alpaca_width)     #81
#print(alpaca_height)    #111
rainbow = pygame.image.load("./zzrsource/rainbow_pic.png")
rainbow_size = rainbow.get_rect().size
rainbow_width = rainbow_size[0]
rainbow_height = rainbow_size[1]
#print(rainbow_width)    #28
#print(rainbow_height)   #35

startscreen = (200, 200, 200)
background1 = (191, 169, 168)   #(163, 175, 183)    (191, 169, 168)
background2 = (194, 148, 125)   #(141, 147, 155)    (194, 148, 125)
background3 = (136, 132, 157)   #(71, 94, 110)      (136, 132, 157)
background4 = (104, 103, 143)   #(44, 66, 89)       (104, 103, 143)
background5 = (61, 69, 105)     #(33, 54, 75)       (61, 69, 105)
background6 = (33, 39, 73)      #(25, 42, 62)       (33, 39, 73)
whitecolor = (255, 255, 255)
greycolor = (140, 140, 140)
titlepic = pygame.image.load("./zzrsource/title_pic.png")
retrypic = pygame.image.load("./zzrsource/gameover_pic.png")

pygame.init()

playing_screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("alpaca_hates_rainbows")
game_font = pygame.font.Font("./zzrsource/DungGeunMo.ttf", 30)
clock = pygame.time.Clock()

global playing
global gameover
global keyenter

class make_rainbow :
    def __init__(self) :
        self.x = random.randint(0, int(display_width-rainbow_width))
        self.y = -rainbow_height
    def drop_rainbow(self, rainbow_speed) :
        self.y += rainbow_speed
    def draw_rainbow(self) :
        playing_screen.blit(rainbow, (self.x, self.y))


def start_playing() :
    global keyenter
    keyenter = False
    
    while True :
        playing_screen.fill(startscreen)
        playing_screen.blit(titlepic, (80, 160))
        howtostart = game_font.render("press the enter to start", True, greycolor)
        playing_screen.blit(howtostart, (95, 570))
        pygame.display.update()

        for event in pygame.event.get() :
            if event.type==pygame.QUIT :
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN :
                if event.key==pygame.K_RETURN :
                    keyenter = True
                
        if keyenter :
            break


def gameover_played(alpaca_x_pos, alpaca_y_pos) :
    global keyenter
    keyenter = False
    
    while True :
        playing_screen.blit(alpaca1, (alpaca_x_pos, alpaca_y_pos))
        playing_screen.blit(retrypic, (115, 220))
        pygame.display.update()

        for event in pygame.event.get() :
            if event.type==pygame.QUIT :
                pygame.quit()
                exit()
            elif event.type==pygame.KEYDOWN :
                if event.key==pygame.K_y :
                    playing = True
                    gameover= False
                    main_playing()
                elif event.key==pygame.K_n :
                    playing = False
                    start_playing()
                    if keyenter==True :
                        main_playing()


def main_playing() :
    start_ticks = pygame.time.get_ticks()
    
    alpaca_x_pos = (display_width/2)-(alpaca_width/2)
    alpaca_y_pos = display_height-alpaca_height
    alpaca_speed = 0.3
    alpaca_x = 0
    alpaca_y = 0

    rainbow_speed = 0
    rainbow_list = []
    level = ''
    time_count = 0
    drop_number = 0
    global playing
    global gameover
    playing = True
    gameover = False


    while playing :        
        if not gameover :
            dt = clock.tick(40)
            time_count += 1
            if time_count<400 :
                level = '1'
                drop_number = 30
                rainbow_speed = 3
                playing_screen.fill(background1)
            elif time_count>=400 and time_count<800 :
                level = '2'
                drop_number = 20
                rainbow_speed = 7
                playing_screen.fill(background2)
            elif time_count>=800 and time_count<1200 :
                level = '3'
                drop_number = 13
                rainbow_speed = 11
                playing_screen.fill(background3)
            elif time_count>=1200 and time_count<1600 :
                level = '4'
                drop_number = 8
                rainbow_speed = 15
                playing_screen.fill(background4)
            elif time_count>=1600 and time_count<2000 :
                level = '5'
                drop_number = 4
                rainbow_speed = 21
                playing_screen.fill(background5)
            else :
                level = '00'
                drop_number = 2
                rainbow_speed = 35
                playing_screen.fill(background6)

            if time_count%drop_number==0 :
                rainbow_list.append(make_rainbow())
            for rb in rainbow_list :
                rb.drop_rainbow(rainbow_speed)
                rb.draw_rainbow()

            for event in pygame.event.get() :
                if event.type==pygame.QUIT :
                    playing = False
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.KEYDOWN :
                    if event.key==pygame.K_LEFT :
                        alpaca_x -= alpaca_speed
                    elif event.key==pygame.K_RIGHT :
                        alpaca_x += alpaca_speed
                elif event.type==pygame.KEYUP :
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT :
                        alpaca_x = 0

            alpaca_x_pos += alpaca_x*dt
            if alpaca_x_pos<0 :
                alpaca_x_pos = 0
            elif alpaca_x_pos>display_width-alpaca_width :
                alpaca_x_pos = display_width-alpaca_width

            for rb in rainbow_list :
                if rb.y>alpaca_y_pos and rb.y<alpaca_y_pos+alpaca_height-8 :
                    if (rb.x>alpaca_x_pos and rb.x<alpaca_x_pos+alpaca_width-8) or\
                    (rb.x+rainbow_width>alpaca_x_pos and rb.x+rainbow_width<alpaca_x_pos+alpaca_width-8) :
                        playing = False
                        gameover = True

            playing_screen.blit(alpaca0, (alpaca_x_pos, alpaca_y_pos))

            elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000
            playingtime = game_font.render(str(int(elapsed_time)), True, whitecolor)
            playing_screen.blit(playingtime, (500, 10))
        
            level_str = 'Lv. '+level
            nowlevel = game_font.render(level_str, True, whitecolor)
            playing_screen.blit(nowlevel, (15, 10))
            pygame.display.update()


        if gameover :
            gameover_played(alpaca_x_pos, alpaca_y_pos)



start_playing()
if keyenter==True :
    main_playing()
