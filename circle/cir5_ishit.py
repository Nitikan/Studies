import arcade
from random import randint
from pyglet.window import key

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
class Player : 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def control(self,keys):
        if keys[key.LEFT]:
            self.x -= 4
        if keys[key.RIGHT]:
            self.x += 4
        if keys[key.UP]:
            self.y += 4
        if keys[key.DOWN]:
            self.y -= 4
    
    def is_hit(self,circle):
        if((abs(self.x-(circle.x))<=10+circle.r and abs(self.y-(circle.y))<=10+circle.r)):
            return 1s

    def draw(self):
        arcade.draw_circle_filled(self.x,self.y,10,arcade.color.LIGHT_BLUE)

class Circle : 
    def __init__(self,x,y,vx,vy,r=20):
        self.x = x 
        self.y = y 
        self.vx = vx
        self.vy = vy
        self.r = r

    def move(self): 
        if(SCREEN_HEIGHT - self.y <= 20 or self.y<=20 ):
            self.vy = -self.vy
            self.y += self.vy
        else : 
            self.y += self.vy

        if(SCREEN_WIDTH - self.x <= 20 or self.x <= 20 ):
            self.vx = -self.vx
            self.x += self.vx
        else:
            self.x += self.vx


    def draw(self):
        arcade.draw_circle_outline(self.x,self.y,self.r, arcade.color.BLACK)

circles = [] 
player = Player(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
n = 5
keys = key.KeyStateHandler()

def initialize():
    for i in range(n):
        circle = Circle(randint(100, SCREEN_WIDTH-100),randint(100, SCREEN_HEIGHT-100),randint(-5,5),randint(-5,5),randint(10,50))
        circles.append (circle)

def on_draw(delta_time):
    arcade.start_render()  
    for c in circles:
        c.move()
        c.draw()
        if player.is_hit(c):
            quit()

    player.control(keys)
    player.draw()   
        

def main():
    initialize()
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "C")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.get_window().push_handlers(keys)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
 
if __name__ == '__main__':
    main()
