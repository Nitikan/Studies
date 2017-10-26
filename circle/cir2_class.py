import arcade
from random import randint

class Circle : 
    def __init__(self,x,y,vx,vy):
        self.x = x 
        self.y = y 
        self.vx = vx
        self.vy = vy

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
        arcade.draw_circle_outline(self.x,self.y,20, arcade.color.BLACK)

circles = [] 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
n = 10

def initialize():
    for i in range(n):
        circle = Circle(randint(100, SCREEN_WIDTH-100),randint(100, SCREEN_HEIGHT-100),randint(-3,3),randint(-3,3))
        circles.append (circle)

def on_draw(delta_time):
    arcade.start_render()  
    for c in circles:
        c.move()
        c.draw()   
        

def main():
    initialize()
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "C")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
 
if __name__ == '__main__':
    main()