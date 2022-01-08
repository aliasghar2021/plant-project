import pygame
width = 1200
height = 805
display =  pygame.display.set_mode ( ( width , height ) )
pygame.display.set_caption ( 'Plants' )
clock = pygame.time.Clock ()
white = ( 255 , 255 , 255 )
black = ( 0 , 0 , 0 )
red = ( 255 , 0 , 0 )
green = ( 0 , 255 , 0 )
dark_green = ( 0 , 210 , 0 )
blue = ( 0 , 0 , 255 )
rect_h = 100
rect_w = 250
rect_x = width / 2 - rect_w / 2
rect_y = 115

entekhab_rects_y = [ 99999 , rect_y - 10 , rect_y + 115 * 2 - 10 , rect_y + 115 * 4 - 10 ]
entekhab = 0
werq = 0

def rect ( x , y , w , h , color ) :
    pygame.draw.rect ( display , color , ( x , y , w , h ) )

while True :
    for event in pygame.event.get () :
        e_t = event.type
        if e_t == pygame.QUIT :
            pygame.quit ()
            quit ()
        if e_t == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :
                entekhab += 1
                werq = 1
            if event.key == pygame.K_UP :
                entekhab -= 1
                werq = 1
            if event.key == pygame.K_SPACE and werq == 1 :
                en = entekhab
                if en == 1 :
                    pygame.quit ()
                    quit ()
                if en == 2 :
                    print ( 2 )
                if en == 3 :
                    print ( 3 )
    if entekhab > 3 and werq == 1 :
        entekhab -= 3
    if entekhab < 1 and werq == 1 :
        entekhab = 3
    display.fill ( white )
    rect ( rect_x - 10 , entekhab_rects_y [ entekhab ] , rect_w + 20 , rect_h + 20 , dark_green )
    rect ( rect_x , rect_y , rect_w , rect_h , green )
    rect ( rect_x , rect_y + 115 * 2 , rect_w , rect_h , green )
    rect ( rect_x , rect_y + 115 * 4 , rect_w , rect_h , green )
    pygame.display.update ()
    clock.tick ( 100 )
