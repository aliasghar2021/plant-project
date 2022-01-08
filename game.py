import pygame
width = 1200
height = 800
display = pygame.display.set_mode ( ( width , height ) )
pygame.display.set_caption ( 'Plants' )
clock = pygame.time.Clock ()

white = ( 255 , 255 , 255 )
black = ( 0 , 0 , 0 )
red = ( 255 , 0 , 0 )
green = ( 0 , 255 , 0 )
blue = ( 0 , 0 , 255 )

def rect ( x , y , w , h , color ) :
    pygame.draw.rect ( display , color , ( x , y , w , h ) )
while True :
    for event in pygame.event.get () :
        e_t = event.type
        if e_t == pygame.QUIT :
            pygame.quit ()
            quit ()
    display.fill ( white )
    pygame.display.update ()
    clock.tick ( 100 )
