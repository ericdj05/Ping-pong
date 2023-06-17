from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,width,height,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height -80:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y < window_height -80:
            self.rect.y += self.speed
back= (200,255,255)
window_width = 600
window_height = 500
mw = display.set_mode((window_width,window_height))
mw.fill(back)

platform_left = Player('racket.png',30,200,40,100,20)
platform_right = Player('racket.png',520,200,40,100,20)
ball = GameSprite('tenis_ball.png',200,200,50,50,50)



font.init()
font1 = font.Font(None,36)

player1win = font1.render("Player 1 WIN!",True,(190,0,0))
player2win = font1.render("Player 2 WIN!",True,(190,0,0))



clock = time.Clock()
FPS = 60
game = True
finish = False
speed_x = 3
speed_y = 3



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        mw.fill(back)
        platform_left.reset()
        platform_right.reset()
        ball.reset()

        platform_left.update_l()
        platform_right.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


    if ball.rect.y > window_height-50 or ball.rect.y <0:
        speed_y *= -1

    if sprite.collide_rect(platform_left,ball) or  sprite.collide_rect(platform_right,ball):
        speed_x *= -1
        speed_y *= 1
    
    if ball.rect.x > window_width:
        finish = True
        mw.blit(player1win,(200,200))
    if ball.rect.x < 0:
        finish = True
        mw.blit(player2win,(200,200))
        

    

        



    display.update()
    clock.tick(FPS)