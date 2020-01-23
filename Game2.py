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
p_button_count = 0
c_button_count = 0
v_button_count = 0
o_button_count = 0
total_time = 0.0
extra = 0
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


class Chapter2View(arcade.View):

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
        arcade.draw_text("Press P to move the Pepperoni", 20, 125, arcade.color.BLACK, 25)
        arcade.draw_text("Press C to move the Cheese", 20, 100, arcade.color.BLACK, 25)
        arcade.draw_text("Press V to move the Vegetable", 20, 75, arcade.color.BLACK, 25)
        arcade.draw_text("Press again to release topping", 20, 50, arcade.color.BLACK, 25)
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
        if P_x > 125 or P_x < 325 and P_y > 540 or P_y < 140 and stop == False:
            peptop = True
        elif P_x > 125 or P_x < 325 and P_y > 540 or P_y < 140 and stop == False:
            peptop = True
        elif C_x > 125 or C_x < 325 and C_y > 540 or C_y < 140 and stop == False:
            cheetop = True
        elif V_x > 125 or V_x < 325 and V_y > 540 or V_y < 140 and stop == False:
            vegtop = True
        elif O_x > 125 or O_x < 325 and O_y > 540 or O_y < 140 and stop == False:
            ontop = True


    def on_key_press(self, key, modifiers):
        global Pepperoni, Cheese, Vegetable, Onion, p_button_count, v_button_count, o_button_count, c_button_count, stop
        if key == arcade.key.P:
            Pepperoni = True
            p_button_count += 1
        elif key == arcade.key.V:
            Vegetable = True
            v_button_count += 1
        elif key == arcade.key.C:
            Cheese = True
            c_button_count += 1
        elif key == arcade.key.O:
            Onion = True
            o_button_count += 1

        if p_button_count == 2 and key == arcade.key.P:
            Pepperoni = False
            p_button_count -= 2
        elif c_button_count == 2 and key == arcade.key.C:
            Cheese = False
            c_button_count -= 2
        elif v_button_count == 2 and key == arcade.key.V:
            Vegetable = False
            v_button_count -= 2
        elif o_button_count == 2 and key == arcade.key.O:
            Onion = False
            o_button_count -= 2

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
        global total_time, peptop, vegtop, cheetop, ontop, extra
        arcade.start_render()
        arcade.draw_text("Pizza Score", 190, 400, arcade.color.BLACK, 54)

        time_taken_formatted = 70 - total_time
        if peptop == True:
            extra += 10
            peptop = False
        elif vegtop == True:
            extra += 10
            vegtop = False
        elif cheetop == True:
            extra += 10
            cheetop = False
        elif ontop == True:
            extra += 10
            ontop = False
        time_taken_formatted2 = f"{time_taken_formatted + extra} points"
        arcade.draw_text(f"Score: {time_taken_formatted2}", WIDTH / 2, 200, arcade.color.BLACK, font_size=15, anchor_x="center")
        arcade.draw_text("Press M to move on", WIDTH/2, 150, arcade.color.BLACK, font_size=15, anchor_x="center")
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.M:
            self.director.next_view()
            #next_game == Game3View()
            #self.window.show_view(next_game)

def main():
    from utils import FakeDirector
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    menu_view = Chapter2View()
    window.show_view(menu_view)
    menu_view.director = FakeDirector(close_on_next_view=True)
    arcade.run()

if __name__ == "__main__":
    main()
