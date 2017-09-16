from random import randint

bricks_at = []

#Excluding the walls, the board is a 17x17 grid with positions ranging from [0...16][0...16]

#While adding bricks ensure that you don't put bricks where a wall exists

#You can manually add bricks or randomize

number_of_bricks = 80 #THIS IS NOT THE TOTAL NUMBER OF BRICKS THAT WILL APPEAR

for i in range(number_of_bricks):
    bricks_at.append([randint(0,16),randint(0,16)])

#Dont put bricks on walls

i = 1
while(i < 16):
    j = 1
    while(j < 16):
        if [i,j] in bricks_at:
            bricks_at.remove([i,j])

        j += 2
    i += 2

#If bricks assigned at [0,0] / [0,1] / [1,0] / [16,16] / [15,16] / [16,15] then remove

not_allowed = [[0,0],[0,1],[1,0],[16,16],[15,16],[16,15]]

for i in not_allowed:
    if i in bricks_at:
        bricks_at.remove(i)
