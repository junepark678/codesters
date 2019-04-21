# Only works in codesters


#set background
stage.set_background("scrollingspace")
stage.disable_all_walls()


#set up the sprites
p1_img = "https://i.pinimg.com/originals/0b/af/2c/0baf2c6260e6ee755ead19593433a4df.png"
p1 = codesters.Sprite(p1_img, -220, 0)
p1.set_size(0.1)
p1.turn_right(90)
p1.lives = 3
p2_img = "http://3.bp.blogspot.com/-cg1jtrxaZ8Y/Ufl5SmFUVaI/AAAAAAAAAzY/KBxNVcMmOB0/s1600/F5S4.png"
p2 = codesters.Sprite(p2_img, 220, 0)
p2.set_size(0.1)
p2.turn_left(90)
p2.lives = 3

left_firing = False
right_firing = False

#display moved up to be a global variable because it is used in places other than the
#main game loop
display = codesters.Text("Destroy your opponent!!", 0, 220, "red")

#fires a laser for player 1
def left_fire():
    global left_firing
    if left_firing is not True:
        left_firing = True
        laser = codesters.TriangleIso(p1.get_x(), p1.get_y(), 5, 10, "blue")
        laser.turn_right(90)
        laser.set_x_speed(10)
        left_firing = False

#fires a laser for player 2
def right_fire():
    global right_firing
    if right_firing is not True:
        right_firing = True
        laser = codesters.TriangleIso(p2.get_x(), p2.get_y(), 5, 10, "yellow")
        laser.turn_left(90)
        laser.set_x_speed(-10)
        right_firing = False

#controls for both ships
def w_key():
    p1.move_up(10)
stage.event_key("w", w_key)
def s_key():
    p1.move_down(10)
stage.event_key("s", s_key)
#firing controls for the first player
def d_key():
    left_fire()
stage.event_key("d", d_key)


def up_key():
    p2.move_up(10)
stage.event_key("up", up_key)
def down_key():
    p2.move_down(10)
stage.event_key("down", down_key)
#fire controls player 2
def left_key():
    right_fire()
stage.event_key("left", left_key)
#################################
#advanced code for AI ship
#setup for alien, starts in middle at small size, invisible
alien = codesters.Sprite("ufo", 0, 0)
alien.set_size(0.2)
alien.hide()
#alien movement function: randomly teleport alien ship to new location and then fire a laser.
def alien_move():
    alien.go_to(random.randint(-130, 130), random.randint(-220, 220))
    alien.show()
    alien_fire()
    stage.wait(2)
    alien.hide()
    stage.wait(2)
#alien firing function: fires a laser either left or right (random chance) after moving.
def alien_fire():
    laser = codesters.Ellipse(alien.get_x(), alien.get_y(), 25, 5, "red")
    if random.randint(0,1) == 0:
        laser.set_x_speed(-5)
    else:
        laser.set_x_speed(5)

#end advanced code for AI ship
#################################
def left_collision(sprite, hit_sprite):
    if hit_sprite.get_color() is "yellow" or hit_sprite.get_color() is "red":
        sprite.lives -= 1
        #remove the laser
        stage.remove_sprite(hit_sprite)
        #remove a heart sprite
        stage.remove_sprite(lives_sprites[p1.lives])
        if p1.lives == 0:
            display.set_text("Dinoship (Player 1) wins! >>>>>")
            end_game()
def right_collision(sprite, hit_sprite):
    if hit_sprite.get_color() is "blue" or hit_sprite.get_color() is "red":
        sprite.lives -= 1
        stage.remove_sprite(hit_sprite)
        #remove a heart sprite
        stage.remove_sprite(lives_sprites[p2.lives + 3])
        if p2.lives == 0:
            display.set_text("<<<<< Sharkship (Player2) wins!")
            end_game()
p1.event_collision(left_collision)
p2.event_collision(right_collision)

#################################
#advanced code for lives visualization
heart_sprite = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/2000px-Heart_coraz%C3%B3n.svg.png"
#setup list of 0 placeholders, these will be replaced with heart sprites
lives_sprites = [0, 0, 0, 0, 0, 0]
def display_lives():
    for life in range(p1.lives):
        heart = codesters.Sprite(heart_sprite, -230 + life * 30, 220)
        heart.set_size(0.01)
        lives_sprites[life] = heart
    for life in range(p2.lives):
        heart = codesters.Sprite(heart_sprite, 150 + life * 30, 220)
        heart.set_size(0.01)
        lives_sprites[life + 3] = heart
#################################

##Modified end game, moved into its own function because of alien code (takes time to run that, slows detection of end game)
##This code is run inside the collision functions now, instead of the main game loop
def end_game():
    display.go_to(0,0)
    stage.remove_sprite(p1)
    stage.remove_sprite(p2)
##

def game():
    #start game, display lives
    display_lives()
    #wait 3 seconds before the loop starts and the alien appears
    stage.wait(3)
    while p1.lives > 0 and p2.lives > 0:
        alien_move()
        stage.wait(0.0001)
game()



