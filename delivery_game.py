import arcade
WIDTH = 800
HEIGHT = 600
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        global down_motion, down_motion2
        global grow_big, grow_big2
        global grow_long, grow_long2

        down_motion = HEIGHT
        grow_big = 10
        grow_long = 2
        down_motion2 = HEIGHT/2
        grow_big2 = 20
        grow_long2 = 4
        left_pressed = False
        right_pressed = False

    def on_draw(self):
        global down_motion, down_motion2
        global grow_big, grow_big2
        global grow_long, grow_long2
        car_sprite = arcade.Sprite('Sprites/car_sprite.png', center_x=WIDTH / 15, center_y=128, scale=0.4)

        arcade.start_render()  # keep as first line
        # Draw everything below here.
        arcade.draw_triangle_filled(WIDTH/2, HEIGHT, WIDTH*0.1666, 0, WIDTH*0.8333, 0, arcade.color.BLACK)
        arcade.draw_rectangle_filled(WIDTH / 2, down_motion, grow_long, grow_big, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(WIDTH / 2, down_motion2, grow_long2, grow_big2, arcade.color.YELLOW)
        if down_motion == 0:
            down_motion = HEIGHT
            grow_big = 10
            grow_long = 2

        if down_motion2 == 0:
            down_motion2 = HEIGHT
            grow_big2 = 10
            grow_long2 = 2
        car_sprite.draw()







    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """



    def on_key_release(self, key, key_modifiers):

        if key == arcade.key.D:
            right_pressed = True

        if key == arcade.key.A:
            left_pressed = True

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        global down_motion, down_motion2
        global grow_big, grow_big2
        global grow_long, grow_long2
        down_motion -=4
        down_motion2 -=4
        grow_big += 1
        grow_big2 += 1
        grow_long += 0.2
        grow_long2 += 0.2


    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
