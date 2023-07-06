import random

def make_mountain(landscape):
    h_x=random.randint(0, len(landscape.landscape[0])-1)
    h_y=random.randint(1,len(landscape.landscape)-1)
    highest_point=(h_x,h_y)
    landscape.make_column(highest_point)
    last_right=highest_point
    last_right_end=False
    last_left=highest_point
    last_left_end=False
    while True:
        if last_left_end==True and last_right_end==True:
            break
        left_random_y=random.randrange(3)
        right_random_y=random.randrange(3)
        
        if last_right[1]==len(landscape.landscape[0])-2:
            right_random_y=random.randrange(2)
        elif last_right[1]==len(landscape.landscape[0])-1:
            if random.randrange(1)==0:
                last_right_end=True
            else:
                right_random_y=0
        
        if last_left[1]==len(landscape.landscape[0])-2:
            left_random_y=random.randrange(2)
        elif last_left[1]==len(landscape.landscape[0])-1:
            if random.randrange(1)==0:
                last_left_end=True
            else:
                left_random_y=0
        
        if last_right[0]+1 < len(landscape.landscape[0]):
            new_right=(last_right[0]+1, last_right[1]-right_random_y)
            landscape.make_column(new_right)
            last_right=new_right
        else:
            last_right_end=True
            
        if last_left[0]-1 >= 0:
            new_left=(last_left[0]-1, last_left[1]-left_random_y)
            landscape.make_column(new_left)
            last_left=new_left
        else:
            last_left_end=True

    return landscape.landscape