import math

def robot_movement (movement):
    position = [0, 0]
    lst = movement.split (' ')
    up, down, left, right = 0, 0, 0, 0

    up += int (lst[1])
    down += int (lst[3])
    left += int (lst[5])
    right += int (lst[7])

    position[0] += right - left
    position[1] += up - down

    return f'(x, y) = {tuple(position)}'


movement = input ("Enter your points in order(POSITION(str), MOVEMENT(number))\n==> ")
print (robot_movement (movement))




# Another Solution



pos = [0,0]


while True:
    s = input ()
    if not s:
        break

    movement = s.split (" ")
    direction = movement[0]
    steps = int (movement[1])

    if (direction == 'UP'):
        pos[0] += steps
    elif (direction == 'DOWN'):
        pos[0] -= steps
    elif (direction == 'LEFT'):
        pos[1] -= steps
    elif (direction == 'RIGHT'):
        pos[1] += steps
    else:
        pass


print (int (round (math.sqrt (pos[1]**2 + pos[0]**2))))