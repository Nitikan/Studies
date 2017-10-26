
import arcade

from random import randint

from pyglet.window import key

SCREEN_HEIGHT = 600

SCREEN_WIDTH = 600

keys = key.KeyStateHandler()

class Circle:

    def __init__(self,x,y,vx,vy):

        self.x = x

        self.y = y

        self.vy = vy

        self.vx = vx

    def move(self):

        self.x+=self.vx

        self.y+= self.vy

        if(abs(SCREEN_HEIGHT-self.y)<=20 or abs(SCREEN_HEIGHT-self.y)>=580):

            self.vy*=-1

        if(abs(SCREEN_WIDTH-self.x)<=20 or abs(SCREEN_WIDTH-self.x)>=580):

            self.vx*=-1

    def draw(self):

        arcade.draw_circle_outline(self.x,self.y,20,arcade.color.BLACK)



class Player:

    def __init__(self,x,y):

        self.x = x

        self.y = y

    def draw(self):

        arcade.draw_circle_filled(self.x,self.y,10,arcade.color.BLUE)

    def wall(self):

        if(abs(SCREEN_HEIGHT-self.y)<=20):

            self.y = 580

        elif(abs(SCREEN_HEIGHT-self.y)>=580):

            self.y = 20 

        if(abs(SCREEN_WIDTH-self.x)<=20):

            self.x = 580  

        elif(abs(SCREEN_WIDTH-self.x)>=580):

            self.x = 20 

    def control(self,keys):

        if(keys[key.W]):

            self.y+=5

        if(keys[key.S]):

            self.y-=5

        if(keys[key.A]):

            self.x-=5   

        if(keys[key.D]):

            self.x+=5

    def on_hit(self,circle):

        check = False

        if((abs(self.x-(circle.x))<=30 and abs(self.y-(circle.y))<=30)):

            check =True

        return check

player = Player(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)

circles=[]

n = 10

def initialize():

    for i in range(n):

        circle = Circle(randint(100,SCREEN_WIDTH-100),randint(100,SCREEN_HEIGHT-100),randint(-5,5),randint(-5,5))

        circles.append(circle)

def on_draw(delta_time):

    arcade.start_render()

    for c in circles:

        c.move()

        c.draw()

        if(player.on_hit(c)):

           print("hit")

        else:

           print("nonhit")

    player.control(keys)

    player.wall()

    player.draw()

def main():

    initialize()

    arcade.open_window(SCREEN_HEIGHT,SCREEN_WIDTH,"KUY")

    arcade.set_background_color(arcade.color.WHITE)

    arcade.get_window().push_handlers(keys)

    arcade.schedule(on_draw,1/80)

    arcade.run()

if __name__=='__main__':

    main()