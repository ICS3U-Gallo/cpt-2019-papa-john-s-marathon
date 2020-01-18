# Developed by Rahul Gour
import arcade
import random
import time

WIDTH = 800
HEIGHT = 600
left_pressed = False
right_pressed = False


car_sprite = arcade.Sprite('Sprites3/car_sprite.png',
                           center_x=WIDTH / 2, center_y=40, scale=0.35)
instructions = arcade.Sprite("Sprites3/instruction_screen.png",
                             center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)
lose = arcade.Sprite('Sprites3/lose_screen.png',
                     center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)
win = arcade.Sprite('Sprites3/win_screen.png',
                    center_x=WIDTH / 2, center_y=HEIGHT / 2, scale=1)

# Sets up initial dimensions for traffic lines
down_motion = HEIGHT
grow_big = 10
grow_long = 2

down_motion2 = HEIGHT / 2
grow_big2 = 20
grow_long2 = 4
down_motion3 = HEIGHT

# Set up initial directions for gas money
direction = WIDTH / 2
added = 0

# Initial length for fuel tank
len_gas_money = 200


class Game3View(arcade.View):

    def __init__(self):
        super().__init__()
        self.total_time = 70.0

    def on_show(self):
        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        global down_motion, down_motion2, down_motion3
        global grow_big, grow_big2
        global grow_long, grow_long2
        global direction, added
        global len_gas_money
        global left_pressed, right_pressed
        arcade.start_render()

        # Set up timer
        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        sec_output = f"{seconds:02d}"
        arcade.draw_text(output, WIDTH * 0.2, HEIGHT * 0.9,
                         arcade.color.BLACK, 30)

        arcade.draw_rectangle_filled(WIDTH * 0.85, HEIGHT * 0.9,
                                     len_gas_money, 30, arcade.color.RED_DEVIL)
        arcade.draw_triangle_filled(WIDTH / 2, HEIGHT,
                                    WIDTH * 0.1666, 0, WIDTH * 0.8333, 0, arcade.color.BLACK)
        arcade.draw_rectangle_filled(WIDTH / 2, down_motion,
                                     grow_long, grow_big, arcade.color.WHITE)
        arcade.draw_rectangle_filled(WIDTH / 2, down_motion2,
                                     grow_long2, grow_big2, arcade.color.WHITE)
        money = arcade.Sprite('Sprites3/money.png', center_x=direction,
                              center_y=down_motion3, scale=0.35)
        arcade.draw_text("Gas Tank: ", 250, HEIGHT * 0.95,
                         arcade.color.WHITE, 25, width=WIDTH, align="center")

        # Resets initial dimensions of traffic lines
        if down_motion == 0:
            down_motion = HEIGHT
            grow_big = 10
            grow_long = 2

        if down_motion2 == 0:
            down_motion2 = HEIGHT
            grow_big2 = 10
            grow_long2 = 2

        # Generates a random direction for coins
        if down_motion3 == 0:
            down_motion3 = HEIGHT
            added = random.randint(-5, 6)
            direction = WIDTH / 2

        if seconds <= 0 and minutes <= 0:  # you win
            win.draw()
            minutes = 0
            direction = 0
            down_motion3 = 0
            car_sprite.center_x = WIDTH + 100

        elif minutes <= -1:  # proceeds to next game
            time.sleep(2)
            self.director.next_view()

        if len_gas_money <= 0:  # you lose
            lose.draw()
            len_gas_money = 0
            down_motion3 = 0
            direction = 0
            car_sprite.center_x = WIDTH + 100
            arcade.draw_text('PRESS ENTER TO PLAY AGAIN',
                             WIDTH * 0.35, HEIGHT * 0.35, arcade.color.BLACK, 20)

        if minutes >= 1:  # Opens instruction page
            instructions.draw()
            arcade.draw_text(sec_output, WIDTH * 0.355, HEIGHT * 0.08, arcade.color.BLACK, 30)
            down_motion3 = HEIGHT + 30

        elif minutes <= 1:  # draws sprites
            money.draw()
            car_sprite.draw()

    def on_key_press(self, key, key_modifiers):

        global left_pressed, right_pressed
        global len_gas_money, direction, down_motion3

        if key == arcade.key.RIGHT:
            right_pressed = True
            left_pressed = False

        if key == arcade.key.LEFT:
            left_pressed = True
            right_pressed = False

        if len_gas_money <= 0:
            if key == arcade.key.ENTER:  # restart Game
                time.sleep(1)
                self.total_time = 60.0
                len_gas_money = 150
                down_motion3 = HEIGHT
                car_sprite.center_x = WIDTH/2
                car_sprite.draw()

    def update(self, delta_time):
        global down_motion, down_motion2, down_motion3
        global grow_big, grow_big2
        global grow_long, grow_long2
        global direction, added
        global len_gas_money
        global left_pressed, right_pressed

        # Sets up motion
        self.total_time -= delta_time
        len_gas_money -= 0.25
        direction += added
        down_motion -= 4
        down_motion2 -= 4
        down_motion3 -= 15
        grow_big += 1
        grow_big2 += 1
        grow_long += 0.2
        grow_long2 += 0.2

        # Collision Detection
        money = arcade.Sprite('Sprites3/money.png', center_x=direction,
                              center_y=down_motion3, scale=0.35)
        hit = arcade.check_for_collision(car_sprite, money)
        if hit:
            len_gas_money += 1
            hit = False

        # Movement Parameters
        if left_pressed:
            car_sprite.center_x -= 6
            if car_sprite.center_x < WIDTH * 0.25:
                car_sprite.center_x += 6
        if right_pressed:
            car_sprite.center_x += 6
            if car_sprite.center_x > WIDTH * 0.75:
                car_sprite.center_x -= 6


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
    my_view = Game3View()
    my_view.director = FakeDirector(close_on_next_view=True)
    window.show_view(my_view)
    arcade.run()
