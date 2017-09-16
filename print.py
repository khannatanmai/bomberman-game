import board as b
import bomberman as bm
import enemy as e
import bricks as brk
import bomb
import time
import getch
import non_blocking_input as nbi

instance = b.board()
bman_obj = bm.bomberman()
enemy_obj = e.enemy()
brick_obj = brk.brick()
bomb_obj = bomb.bomb()

def user_input():
    #Input from player
    ch = nbi.get_char_keyboard_nonblock()

    if(ch == 'q'): #QUIT GAME
        print('\n'*60)
        print("Are you sure you want to quit? (y/n)")
        inp_ch = getch.getch()

        if(inp_ch in ['y','Y']):
            return 0
        
    bman_obj.move(ch,instance.layout,bomb_obj)

def render():
    instance.update(bman_obj, enemy_obj, brick_obj, bomb_obj)
    for i in range(38):
        for j in range(76):
            print(instance.layout[i][j], end='') #to not put a newl after the line as print does that automatically
        print('\n', end='')

def work():
    game_time = 180
    won = 0
    
    while(game_time > 0):
        
        #Print Game Time Left
        print("Time Left: " + str(int(game_time))
              + "\t\t\tLives Left: " + str(bman_obj.lives_left)
              +"\t\t\t\tScore: " + str(bman_obj.score))
        
        #Render the board
        render()

        #Get input
        if(user_input() == 0):
            game_time = 0

        #Game over if lives over
        if(bman_obj.lives_left <= 0):
            time.sleep(1)
            break

        #Game won if enemy dies
        if(enemy_obj.alive == 0):
            bman_obj.score += 100
            time.sleep(1)
            won = 1
            break
        
        #Move the enemy
        enemy_obj.move(instance.layout)

        time.sleep(0.2)

        #Countdown bombs
        bomb_obj.countdown()
               
        game_time -= 0.2
        #Clear Screen
        print('\n'*60)
        
        
    #Game Over Screen
    print('\n'*60)
    print("GAME OVER!")

    if(won == 0):
        print("You lost! :(")
    else:
        print("You won! :)")

    print("Final Score: " + str(bman_obj.score))
    getch.getch()

