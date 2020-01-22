import random
import arcade
import os
from random import shuffle

# --- Constants ---
SPRITE_SCALING_CLOTHING = 1.7
SPRITE_SCALING = 0.75
CLOTHING_COUNT = 8

WIDTH = 800
HEIGHT = 600
TITLE = "Game 1"

class Game1View(arcade.View):
# class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.pants_list = None
        self.shirts_list = None
        self.sillouhette = None

        self.score = 0

        # self.set_mouse_visible(True)

        arcade.set_background_color(arcade.color.CYAN)

    # def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.shirts_list = arcade.SpriteList()
        self.pants_list = arcade.SpriteList()

        # Score
        self.score = 0

        j = [[i] for i in range(CLOTHING_COUNT)]
        shuffle(j)
        print(j)

        for i in range(CLOTHING_COUNT):
            
            # Create the shirts instance
            shirts = arcade.Sprite("resources/images/items/shirts"+str(j[i][0])+".png",
                                 SPRITE_SCALING)

            # Position the shirts
            shirts.center_x = 50
<<<<<<< HEAD
            shirts.center_y = i*HEIGHT/8+shirts.height/2
=======
            shirts.center_y = i*SCREEN_HEIGHT/8+shirts.height/2
>>>>>>> 6747fccc9298fd8ab3d88792c62c82ab380a38a4
            shirts.guid = "s"+str(j[i][0])
            # Add the shirts to the lists
            self.shirts_list.append(shirts)

        j = [[i] for i in range(CLOTHING_COUNT)]
        shuffle(j)
        print(j)
        for i in range(CLOTHING_COUNT):
            # Create the pants instance
            pants = arcade.Sprite("resources/images/items/pants"+str(j[i][0])+".png",
                                 SPRITE_SCALING)

            # Position the pants
            pants.center_x = 150
<<<<<<< HEAD
            pants.center_y = i*HEIGHT/8+pants.height/2
=======
            pants.center_y = i*SCREEN_HEIGHT/8+pants.height/2
>>>>>>> 6747fccc9298fd8ab3d88792c62c82ab380a38a4
            pants.guid = "p"+str(j[i][0])
            # Add the pants to the lists
            self.pants_list.append(pants)
        
        self.sillouhette = arcade.Sprite("resources/images/items/sillhouette.png",1.3)
<<<<<<< HEAD

        self.sillouhette.center_x = 500      
        self.sillouhette.center_y = HEIGHT/2
        self.instructions = 1 


    def on_draw(self):
        if self.instructions==1:
            arcade.draw_text("Click to continue", 100, 100, arcade.color.YELLOW, 20)
            arcade.draw_text("Click on shirts and pants to make the best combo", 100, 200, arcade.color.YELLOW, 20)

        else:
                
            """ Draw everything """
            arcade.start_render()
            self.sillouhette.draw()
            self.shirts_list.draw()
            self.pants_list.draw()

            i=1
            for sprite in self.shirts_list:
                arcade.draw_text(str(i), sprite.center_x-5 , sprite.center_y-5, arcade.color.YELLOW, 20)
                i=i+1
            i=1
            for sprite in self.pants_list:
                arcade.draw_text(str(i), sprite.center_x-5 , sprite.center_y-5, arcade.color.YELLOW, 20)
                i=i+1

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, WIDTH - 100, HEIGHT - 30, arcade.color.BLACK, 14)

    def on_mouse_release(self, x, y, dx, dy):

        self.instructions = 2
=======

        self.sillouhette.center_x = 500      
        self.sillouhette.center_y = SCREEN_HEIGHT/2


    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.sillouhette.draw()
        self.shirts_list.draw()
        self.pants_list.draw()

        i=1
        for sprite in self.shirts_list:
            arcade.draw_text(str(i), sprite.center_x-5 , sprite.center_y-5, arcade.color.YELLOW, 20)
            i=i+1
        i=1
        for sprite in self.pants_list:
            arcade.draw_text(str(i), sprite.center_x-5 , sprite.center_y-5, arcade.color.YELLOW, 20)
            i=i+1

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30, arcade.color.BLACK, 14)

    def on_mouse_release(self, x, y, dx, dy):

>>>>>>> 6747fccc9298fd8ab3d88792c62c82ab380a38a4
        sprite_list = arcade.get_sprites_at_point((x, y), self.shirts_list)
        if len(sprite_list) > 0:
            i = 0
            guid=None
            for sprite in self.shirts_list:
                if(sprite.scale==SPRITE_SCALING_CLOTHING):
                    guid = sprite.guid
                    sprite.scale=SPRITE_SCALING
                    sprite.center_x = 50
<<<<<<< HEAD
                    sprite.center_y = i*HEIGHT/8+sprite.height/2
=======
                    sprite.center_y = i*SCREEN_HEIGHT/8+sprite.height/2
>>>>>>> 6747fccc9298fd8ab3d88792c62c82ab380a38a4
                    self.score = self.score-int(guid[1])
                    break
                i=i+1
            print(sprite_list[0].guid, guid)
            if(sprite_list[0].guid!=guid):
                sprite_list[0].center_x=500
                sprite_list[0].center_y=380
                sprite_list[0].scale=SPRITE_SCALING_CLOTHING
                self.score = self.score+int(sprite_list[0].guid[1])
        sprite_list = arcade.get_sprites_at_point((x, y), self.pants_list)
        if len(sprite_list) > 0:
            i = 0
            guid=None
            for sprite in self.pants_list:
                if(sprite.scale==SPRITE_SCALING_CLOTHING):
                    guid = sprite.guid
                    sprite.scale=SPRITE_SCALING
                    sprite.center_x = 150
<<<<<<< HEAD
                    sprite.center_y = i*HEIGHT/8+sprite.height/2
=======
                    sprite.center_y = i*SCREEN_HEIGHT/8+sprite.height/2
>>>>>>> 6747fccc9298fd8ab3d88792c62c82ab380a38a4
                    self.score = self.score-int(guid[1])
                    break
                i=i+1
            print(sprite_list[0].guid, guid)
            if(sprite_list[0].guid!=guid):
                sprite_list[0].center_x=500
                sprite_list[0].center_y=200
                sprite_list[0].scale=SPRITE_SCALING_CLOTHING
                self.score = self.score+int(sprite_list[0].guid[1])

    def on_update(self, delta_time):
        pass

# def main():
#     """ Main method """
#     window = MyGame()
#     window.setup()
#     arcade.run()


# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    """This section of code will allow you to run your View
    independently from the main.py file and its Director.
    You can ignore this whole section. Keep it at the bottom
    of your code.
    It is advised you do not modify it unless you really know
    what you are doing.
    """
    from utils import FakeDirector

    window = arcade.Window(WIDTH, HEIGHT)
    my_view = Game1View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()