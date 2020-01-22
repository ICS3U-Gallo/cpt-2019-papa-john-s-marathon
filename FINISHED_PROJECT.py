
import arcade
import random
import os
import math

total_time=0

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "game 4"

change_x=0
change_y=0

move_or_not_x =False
move_or_not_y = False
win = False
time=0



def draw():
    arcade.start_render

    
def make_person(head_radius,
                chest_height,
                chest_width,
                leg_width,
                leg_height,
                arm_width,
                arm_length,
                arm_gap,
                shoulder_height):

    shape_list = arcade.ShapeElementList()

    shape = arcade.create_rectangle_filled((chest_width / 2) + (arm_gap + arm_width) / 2+10,
                                           (chest_height / 2) - shoulder_height / 2 - 50, arm_gap + arm_width,
                                           shoulder_height-50, arcade.color.BLUE_BELL)
    shape_list.append(shape)

    shape = arcade.create_rectangle_filled((chest_width / 2) + (arm_gap + arm_width) / 2+30,
                                           (chest_height / 2) - shoulder_height / 2 - 50, arm_gap + arm_width+20,
                                           shoulder_height+20, arcade.color.BLUE_BELL)
    shape_list.append(shape)


    # Head
    shape = arcade.create_ellipse_filled(0, chest_height / 2 + head_radius, head_radius, head_radius,
                                         arcade.color.WHITE)
    shape_list.append(shape)

    # Chest
    shape = arcade.create_rectangle_filled(0, 0, chest_width, chest_height, arcade.color.BLACK)
    shape_list.append(shape)

    # Left leg
    shape = arcade.create_rectangle_filled(-(chest_width / 2) + leg_width / 2, -(chest_height / 2) - leg_height / 2,
                                           leg_width, leg_height, arcade.color.RED)
    shape_list.append(shape)

    # Right leg
    shape = arcade.create_rectangle_filled((chest_width / 2) - leg_width / 2, -(chest_height / 2) - leg_height / 2,
                                           leg_width, leg_height, arcade.color.RED)
    shape_list.append(shape)

    # Left arm

    shape = arcade.create_rectangle_filled(-(chest_width / 2) - arm_width / 2 - arm_gap,
                                        (chest_height / 2) - arm_length / 2 - shoulder_height, arm_width, arm_length,
                                        arcade.color.BLUE)
    shape_list.append(shape)



    # Left shoulder
    shape = arcade.create_rectangle_filled(-(chest_width / 2) - (arm_gap + arm_width) / 2,
                                           (chest_height / 2) - shoulder_height / 2, arm_gap + arm_width,
                                           shoulder_height, arcade.color.BLUE_BELL)
    shape_list.append(shape)

    # Right arm
    shape = arcade.create_rectangle_filled((chest_width / 2) + arm_width / 2 + arm_gap,
                                           (chest_height / 2) - arm_length / 2 - shoulder_height, arm_width, arm_length,
                                           arcade.color.BLUE)
    shape_list.append(shape)

    # Right shoulder
    shape = arcade.create_rectangle_filled((chest_width / 2) + (arm_gap + arm_width) / 2,
                                           (chest_height / 2) - shoulder_height / 2, arm_gap + arm_width,
                                           shoulder_height, arcade.color.BLUE_BELL)
    shape_list.append(shape)

    shape = arcade.create_rectangle_filled(100, -22, 100, 20, arcade.color.BLUE_BELL)

    shape_list.append(shape)



    return shape_list


def make_boss(head_radius,
                chest_height,
                chest_width,
                leg_width,
                leg_height,
                arm_width,
                arm_length,
                arm_gap,
                shoulder_height):

    boss_shape_list = arcade.ShapeElementList()

    




    # Head
    shape = arcade.create_ellipse_filled(0, chest_height / 2 + head_radius, head_radius, head_radius,
                                         arcade.color.WHITE)
    boss_shape_list.append(shape)

    # Chest
    shape = arcade.create_rectangle_filled(0, 0, chest_width, chest_height, arcade.color.BLACK)
    boss_shape_list.append(shape)

    # Left leg
    shape = arcade.create_rectangle_filled(-(chest_width / 2) + leg_width / 2, -(chest_height / 2) - leg_height / 2,
                                           leg_width, leg_height, arcade.color.RED)
    boss_shape_list.append(shape)

    # Right leg
    shape = arcade.create_rectangle_filled((chest_width / 2) - leg_width / 2, -(chest_height / 2) - leg_height / 2,
                                           leg_width, leg_height, arcade.color.RED)
    boss_shape_list.append(shape)

    # Left arm

    shape = arcade.create_rectangle_filled(-(chest_width / 2) - arm_width / 2 - arm_gap,
                                        (chest_height / 2) - arm_length / 2 - shoulder_height, arm_width, arm_length,
                                        arcade.color.BLUE)
    boss_shape_list.append(shape)



    # Left shoulder
    shape = arcade.create_rectangle_filled(-(chest_width / 2) - (arm_gap + arm_width) / 2,
                                           (chest_height / 2) - shoulder_height / 2, arm_gap + arm_width,
                                           shoulder_height, arcade.color.BLUE_BELL)
    boss_shape_list.append(shape)

    # Right arm
    shape = arcade.create_rectangle_filled((chest_width / 2) + arm_width / 2 + arm_gap,
                                           (chest_height / 2) - arm_length / 2 - shoulder_height, arm_width, arm_length,
                                           arcade.color.BLUE)
    boss_shape_list.append(shape)

    # Right shoulder
    shape = arcade.create_rectangle_filled((chest_width / 2) + (arm_gap + arm_width) / 2,
                                           (chest_height / 2) - shoulder_height / 2, arm_gap + arm_width,
                                           shoulder_height, arcade.color.BLUE_BELL)
    boss_shape_list.append(shape)



    return boss_shape_list





    


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        head_radius = 15
        chest_height = 65
        chest_width = 35
        leg_width = 10
        leg_height = 40
        arm_width = 7
        arm_length = 35
        arm_gap = 5
        shoulder_height = 7

        self.score=0

        self.shape_list = make_person(head_radius,
                                      chest_height,
                                      chest_width,
                                      leg_width,
                                      leg_height,
                                      arm_width,
                                      arm_length,
                                      arm_gap,
                                      shoulder_height)
        
        self.boss_shape_list = make_person(head_radius,
                                      chest_height,
                                      chest_width,
                                      leg_width,
                                      leg_height,
                                      arm_width,
                                      arm_length,
                                      arm_gap,
                                      shoulder_height)

                        

        

    def setup(self):

        
        self.score=0



    def on_draw(self):


        # This command has to happen before we start drawing
        arcade.start_render()

        self.shape_list.draw()

        self.boss_shape_list.draw()

        if win == True:
            arcade.draw_text("YOU HAVE BEAT THE BOSS!", 150, 300,
                        arcade.color.WHITE, font_size=30)

            arcade.draw_text("ENJOY THAT MINIMUM WAGE PAYCHECK!", 150, 200,
                    arcade.color.WHITE, font_size=30)

        if total_time<500:
            arcade.draw_text("YOUR BOSS DOESNT WANT TO PAY YOU", 150, 500,
                arcade.color.WHITE, font_size=30)
            arcade.draw_text("FOR YOUR HARD WORK TODAY, SO", 150, 400,
                arcade.color.WHITE, font_size=30)

            arcade.draw_text("YOU MUST TAKE YOUR SWORD AND", 150, 300,
                    arcade.color.WHITE, font_size=30)
            arcade.draw_text("FIGHT FOR THAT PAYCHECK!!!!", 150, 200,
                    arcade.color.WHITE, font_size=30)

        




        output = f"BOSS HEALTH: {math.ceil(100-(self.score/10))}%"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 40)

    def on_update(self, delta_time):
        global move_or_not_x
        global move_or_not_y
        global time
        global score
        global change_x
        global change_y
        global win
        global total_time


        total_time+=1
        if total_time>500:
            if move_or_not_x == True:
                self.shape_list.center_x += x_movement
            if move_or_not_y == True:
                self.shape_list.center_y += y_movement
            
        
        if time<100:
            time += 1
        else:
            time = 0

        
        
        


        
        if total_time>500:
            if time==0:
                if self.boss_shape_list.center_x<100:
                    change_x = 5
                elif self.boss_shape_list.center_x>700:
                    change_x -= 5
                else:
                    change_x = random.randint(-1,1)
                if self.boss_shape_list.center_y<100:
                    change_y += 5
                elif self.boss_shape_list.center_y>500:
                    change_y -= 5
                else:
                    change_y += random.randint(-1, 1)
                

            self.boss_shape_list.center_x += change_x
            self.boss_shape_list.center_y += change_y




        if self.shape_list.center_x - self.boss_shape_list.center_x < -140 and self.shape_list.center_x - self.boss_shape_list.center_x > -180 and self.shape_list.center_y - self.boss_shape_list.center_y < 100 and self.shape_list.center_y - self.boss_shape_list.center_y > -100:
            self.score+=1

        if 100-(self.score/10) < 0:
            win=True
        
        if win == True:
            self.boss_shape_list.center_x = -1000
            self.shape_list.center_x = -500



    def on_key_press(self, key, modifiers):
        global x_movement
        global y_movement
        global move_or_not_x
        global move_or_not_y
        global punch

        #if key == arcade.key.SPACE:
            
        if key == arcade.key.LEFT:
            x_movement= -5
            move_or_not_x = True
        elif key == arcade.key.RIGHT:
            x_movement= 5
            move_or_not_x = True
        if key == arcade.key.UP:
            y_movement= 5
            move_or_not_y = True
        elif key == arcade.key.DOWN:
            move_or_not_y = True
            y_movement=-5
        
        if key == arcade.key.DOWN:
            punch=True

    def on_key_release(self, key, modifiers):
        global x_movement
        global y_movement
        global move_or_not_x
        global move_or_not_y

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            move_or_not_x == False
            x_movement = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            move_or_not_y == False
            y_movement = 0
        #if key == arcade.key.SPACE:
         #   punch = False


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()