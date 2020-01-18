import random

import arcade

WIDTH = 800
HEIGHT = 600
press = False
hold = False


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        self.cheese = arcade.Sprite(center_y=100, center_x=100)
        self.cheese.texture = arcade.make_soft_square_texture(50, arcade.color.YELLOW, outer_alpha=255)
        self.cheeses = arcade.SpriteList()

        self.pepperoni = arcade.Sprite(center_x=200, center_y=100)
        self.pepperoni.texture = arcade.make_soft_circle_texture(50, arcade.color.RED, outer_alpha=255)
        self.pepperonis = arcade.SpriteList()

        #self.enemy_texture = arcade.make_soft_square_texture(50, arcade.color.RED, outer_alpha=255)
        #self.enemies = arcade.SpriteList()

        #for _ in range(3):
            #pepperoni = arcade.Sprite()
            #pepperoni.center_y = 100
            #pepperoni.center_x = 200
            #pepperoni.texture = self.pepperoni_texture
            #self.pepperonis.append(pepperoni)

        #for _ in range(3):
            #cheese = arcade.Sprite()
            #cheese.center_x = 100
            #cheese.center_y = 100
            #cheese.texture = self.cheese_texture
            #self.cheeses.append(cheese)

            #enemy = arcade.Sprite()
            #enemy.center_x = random.randrange(0, WIDTH)
            #enemy.center_y = random.randrange(HEIGHT//2, HEIGHT)
            #enemy.texture = self.enemy_texture
            #self.enemies.append(enemy)

        #self.laser_texture = arcade.make_soft_square_texture(30, arcade.color.ORANGE, outer_alpha=255)
        #self.lasers = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()  # keep as first line

        # Draw everything below here.
        arcade.draw_circle_filled(WIDTH/2, HEIGHT/2, 300, arcade.color.BEIGE)
        arcade.draw_text("Pepperoni", 100, 175, arcade.BLACK, 25)
        self.pepperonis.draw()
        self.cheeses.draw()

        #self.player.draw()
        #self.enemies.draw()
        #self.lasers.draw()

    def update(self, delta_time):
        global press, hold
        self.pepperonis.update()
        
        self.cheese.update()
        
        #self.lasers.update()

        #for enemy in self.enemies:
            #lasers_in_contact = enemy.collides_with_list(self.lasers)
            #if lasers_in_contact:
                #enemy.kill()
                #for laser in lasers_in_contact:
                    #laser.kill()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        global press, hold
        pepperoni = arcade.Sprite()
        if hold == True:
            pepperoni.center_x = x
            pepperoni.center_y = y
        #self.player.center_x = x
        #self.player.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        global press, hold
        press = True
        pepperoni = arcade.Sprite()
        if press == True and x <= 150 and x >= 50 and y <= 150 and y >= 50 and hold == False:
            pepperoni.center_y = y
            pepperoni.center_x = x
            hold = True
            press = False
        elif press == True and hold == True:
            pepperoni.center_y = y
            pepperoni.center_x = x
            hold = False
            press = False

        self.pepperonis.append(pepperoni)
        #laser = arcade.Sprite()
        #laser.center_x = self.player.center_x
        #laser.center_y = self.player.center_y
        #laser.change_y = 3
        #laser.texture = self.laser_texture
        #laser.width = 5

        #self.lasers.append(laser)


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    arcade.run()


if __name__ == "__main__":
    main()
