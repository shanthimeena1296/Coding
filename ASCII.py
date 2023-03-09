def draw_stairs(n):
    # do something
    stairs = ''
    for i in range(n):
        for j in range(i):
            stairs += ' '
        stairs += 'I\n'
    return stairs.rstrip()
        
draw_stairs(7)