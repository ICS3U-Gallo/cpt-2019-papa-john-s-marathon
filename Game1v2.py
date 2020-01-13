import random
import arcade
import os
from random import shuffle


# --- Constants ---
SPRITE_SCALING_CLOTHING = 1.7
SPRITE_SCALING = 0.75
CLOTHING_COUNT = 8

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Game 1"


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

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

        self.set_mouse_visible(True)

        arcade.set_background_color(arcade.color.CYAN)

    def setup(self):
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
            shirts.center_y = i*SCREEN_HEIGHT/8+shirts.height/2
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
            pants.center_y = i*SCREEN_HEIGHT/8+pants.height/2
            pants.guid = "p"+str(j[i][0])
            # Add the pants to the lists
            self.pants_list.append(pants)
        
        self.sillouhette = arcade.Sprite("resources/images/items/sillhouette.png",1.3)

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

        sprite_list = arcade.get_sprites_at_point((x, y), self.shirts_list)
        if len(sprite_list) > 0:
            i = 0
            guid=None
            for sprite in self.shirts_list:
                if(sprite.scale==SPRITE_SCALING_CLOTHING):
                    guid = sprite.guid
                    sprite.scale=SPRITE_SCALING
                    sprite.center_x = 50
                    sprite.center_y = i*SCREEN_HEIGHT/8+sprite.height/2
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
                    sprite.center_y = i*SCREEN_HEIGHT/8+sprite.height/2
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

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
