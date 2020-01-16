import arcade
import random
import sys

WIDTH = 800
HEIGHT = 600
left_pressed = False
right_pressed = False

car_sprite = arcade.Sprite('Sprites/car_sprite.png', center_x=WIDTH / 2, center_y=40, scale=0.35)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.total_time = 60.0

    def setup(self):
        global down_motion, down_motion2, down_motion3
        global grow_big, grow_big2
        global grow_long, grow_long2
        global direction, added
        global len_gas_money
        self.total_time = 60.0


        down_motion = HEIGHT
        grow_big = 10
        grow_long = 2

        down_motion2 = HEIGHT / 2
        grow_big2 = 20
        grow_long2 = 4
        down_motion3 = HEIGHT

        direction = WIDTH/2
        added = 0
        len_gas_money = 200


    def on_draw(self):
        global down_motion, down_motion2, down_motion3
        global grow_big, grow_big2
        global grow_long, grow_long2
        global direction, added
        global len_gas_money
        global left_pressed, right_pressed
        arcade.start_render()

        minutes = int(self.total_time) // 60
        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60
        # Figure out our output
        output = f"Time: {minutes:02d}:{seconds:02d}"
        # Output the timer text.
        arcade.draw_text(output, WIDTH*0.2, HEIGHT*0.9, arcade.color.BLACK, 30)


        arcade.draw_rectangle_filled(WIDTH*0.85, HEIGHT*0.9, len_gas_money, 30, arcade.color.RED_DEVIL)
        arcade.draw_triangle_filled(WIDTH / 2, HEIGHT, WIDTH * 0.1666, 0, WIDTH * 0.8333, 0, arcade.color.BLACK)
        arcade.draw_rectangle_filled(WIDTH / 2, down_motion, grow_long, grow_big, arcade.color.WHITE)
        arcade.draw_rectangle_filled(WIDTH / 2, down_motion2, grow_long2, grow_big2, arcade.color.WHITE)
        money = arcade.Sprite('Sprites/money.png', center_x=direction, center_y=down_motion3, scale=0.35)
        arcade.draw_text("Gas Tank: ",
                         250, HEIGHT*0.95, arcade.color.WHITE, 25, width=WIDTH, align="center")

        if down_motion == 0:
            down_motion = HEIGHT
            grow_big = 10
            grow_long = 2

        if down_motion2 == 0:
            down_motion2 = HEIGHT
            grow_big2 = 10
            grow_long2 = 2

        if down_motion3 == 0:
            down_motion3 = HEIGHT
            added = random.randint(-6, 7)
            direction = WIDTH/2

        if seconds <= 0: #you win
            you_win()

        if len_gas_money <= 0: #you lose
            you_lose()


        money.draw()
        car_sprite.draw()




    def on_key_press(self, key, key_modifiers):

        global left_pressed
        global right_pressed
        if key == arcade.key.RIGHT:
            right_pressed = True
            left_pressed = False

        if key == arcade.key.LEFT:
            left_pressed = True
            right_pressed = False
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        global down_motion, down_motion2, down_motion3
        global grow_big, grow_big2
        global grow_long, grow_long2
        global direction, added
        global len_gas_money
        global left_pressed, right_pressed
        self.total_time -= delta_time
        len_gas_money -= 0.9
        direction += added
        down_motion -= 4
        down_motion2 -= 4
        down_motion3 -= 15
        grow_big += 1
        grow_big2 += 1
        grow_long += 0.2
        grow_long2 += 0.2

        money = arcade.Sprite('Sprites/money.png', center_x=direction, center_y=down_motion3, scale=0.35)
        hit = arcade.check_for_collision(car_sprite, money)
        if hit == True:
            len_gas_money += 1
            hit = False


        if left_pressed:
            car_sprite.center_x -= 6
            if car_sprite.center_x < WIDTH * 0.25:
                car_sprite.center_x += 6
        if right_pressed:
            car_sprite.center_x += 6
            if car_sprite.center_x > WIDTH * 0.75:
                car_sprite.center_x -= 6

def you_lose():
    len_gas_money = 0
    left_pressed = False
    right_pressed = False
    down_motion3 = HEIGHT
    direction = WIDTH / 2
    down_motion = 0
    down_motion2 = 0
    self.total_time += delta_time

def you_win():
    left_pressed = False
    right_pressed = False
    down_motion3 = HEIGHT
    direction = WIDTH / 2
    down_motion = 0
    down_motion2 = 0
    self.total_time += delta_time


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
