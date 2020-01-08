import random
import arcade
import os
from random import shuffle


# --- Constants ---
SPRITE_SCALING_CLOTHING = 1
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
            shirts.center_y = i*SCREEN_HEIGHT/8 + 50

            # Add the pants to the lists
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
            pants.center_y = i*SCREEN_HEIGHT/8 + 50

            # Add the pants to the lists
            self.pants_list.append(pants)
        

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.pants_list.draw()
        self.shirts_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        print(self.pants_list)
        sprite_list = arcade.get_sprites_at_point((x, y), self.pants_list)
        print(sprite_list)
        sprite_list = arcade.get_sprites_at_point((x, y), self.shirts_list)
        print(sprite_list)
        """ Handle Mouse Motion """

    def on_update(self, delta_time):
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()