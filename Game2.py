import arcade
import os

WIDTH = 640
HEIGHT = 480
Pepperoni = False
Cheese = False
Vegetable = False
Onion = False
peptop = False
cheetop = False
vegtop = False
ontop = False
stop = False

TITLE = "Pizza Toppings"
P_x = 100
P_y = 400
C_x = 100
C_y = 300
V_x = 100
V_y = 200
O_x = 100
O_y = 100
button_count = 0
total_time = 0.0
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


class Instructions(arcade.View):

    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(WIDTH / 2, HEIGHT / 2, 25, arcade.color.RED)
        arcade.draw_circle_filled(WIDTH / 2 - 200, HEIGHT / 2 + 50, 25, arcade.color.RED)
        arcade.draw_circle_filled(WIDTH / 2 + 200, HEIGHT / 2 + 200, 25, arcade.color.RED)
        arcade.draw_circle_filled(WIDTH / 2 - 100, HEIGHT / 2 + 175, 25, arcade.color.RED)
        arcade.draw_circle_filled(WIDTH / 2 + 200, HEIGHT / 2 - 175, 25, arcade.color.RED)
        arcade.draw_text("Tutorial", 250, 300, arcade.color.GREEN, 25)
        arcade.draw_text("Click and Drop Pizza toppings using your mouse", 20, 150, arcade.color.BLACK, 25)
        arcade.draw_text("Press P to move the Pepperoni", 20, 100, arcade.color.BLACK, 25)
        arcade.draw_text("Press C to move the Cheese", 20, 75, arcade.color.BLACK, 25)
        arcade.draw_text("Press V to move the Vegetable", 20, 50, arcade.color.BLACK, 25)
        arcade.draw_text("Press Enter to play", 20, 200, arcade.color.BLACK, 25)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            game = MyGame()
            self.window.show_view(game)


class MyGame(arcade.View):

    def __init__(self):
        super().__init__()#WIDTH, HEIGHT, TITLE)
        self.total_time = 0.0

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(HEIGHT / 2 + 125, WIDTH / 2 - 80, 200, arcade.color.DARK_YELLOW)
        arcade.draw_circle_filled(HEIGHT / 2 + 125, WIDTH / 2 - 80, 175, arcade.color.DARK_RED)
        arcade.draw_circle_filled(HEIGHT / 2 + 125, WIDTH / 2 - 80, 150, arcade.color.YELLOW)
        arcade.draw_circle_filled(P_x, P_y, 25, arcade.color.RED)
        arcade.draw_circle_outline(V_x, V_y, 10, arcade.color.GREEN)
        arcade.draw_rectangle_filled(C_x, C_y, 50, 50, arcade.color.ORANGE)
        arcade.draw_circle_outline(O_x, O_y, 25, arcade.color.PURPLE)

        minutes = int(total_time)//60
        seconds = int(total_time) % 60
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 50, 50, arcade.color.BLACK, 25)

    def on_update(self, delta_time):
        global total_time, peptop
        total_time += delta_time
        if stop == True:
            total_time -= 1
        if P_x > 125 or P_x < 325 and P_y > 540 or P_y < 140:
            peptop = True

    def on_key_press(self, key, modifiers):
        global Pepperoni, Cheese, Vegetable, Onion, button_count, stop
        if key == arcade.key.P:
            Pepperoni = True
            button_count += 1
        elif key == arcade.key.V:
            Vegetable = True
            button_count += 1
        elif key == arcade.key.C:
            Cheese = True
            button_count += 1
        elif key == arcade.key.O:
            Onion = True
            button_count += 1

        if button_count == 2 and key == arcade.key.P:
            Pepperoni = False
            button_count -= 2
        elif button_count == 2 and key == arcade.key.C:
            Cheese = False
            button_count -= 2
        elif button_count == 2 and key == arcade.key.V:
            Vegetable = False
            button_count -= 2
        elif button_count == 2 and key == arcade.key.O:
            Onion = False
            button_count -= 2

        if key == arcade.key.ENTER:
            stop = True
            finish_screen = FinishScreen()
            self.window.show_view(finish_screen)


    def on_mouse_press(self, x, y, button, modifiers):
        global P_y, P_x, C_x, C_y, V_x, V_y, O_x, O_y, Pepperoni, Cheese, Vegetable, Onion
        print(x, y)
        if arcade.MOUSE_BUTTON_LEFT and Pepperoni == True:
            P_x = x
            P_y = y
        elif arcade.MOUSE_BUTTON_LEFT and Cheese == True:
            C_y = y
            C_x = x
        elif arcade.MOUSE_BUTTON_LEFT and Vegetable == True:
            V_x = x
            V_y = y
        elif arcade.MOUSE_BUTTON_LEFT and Onion == True:
            O_x = x
            O_y = y


class FinishScreen(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        global total_time
        arcade.start_render()
        arcade.draw_text("Pizza Score", 190, 400, arcade.color.BLACK, 54)

        time_taken_formatted = f"{70 - total_time} points"
        arcade.draw_text(f"Score: {time_taken_formatted}", WIDTH / 2, 200, arcade.color.WHITE, font_size=15, anchor_x="center")

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    menu_view = Instructions()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()
