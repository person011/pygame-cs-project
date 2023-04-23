import numpy as np
import random

def make_mountain(landscape):
    h_x=random.randint(0, len(landscape.landscape[0])-1)
    if landscape.get_landscapes_highest_block(h_x)==0:
        h_y=random.randint(1, len(landscape.landscape)-1)
    else:
        h_y=random.randint(landscape.get_landscapes_highest_block(h_x), len(landscape.landscape)-1)
    
    highest_point=(h_x, h_y)
    #highest_point=(9, 5)
    most_right=len(landscape.landscape[0])
    #print(highest_point)
    landscape.make_column(highest_point)
    last_left=highest_point
    last_right=highest_point
    
    right_minus_y=2
    right_plus_y=0
    
    left_minus_y=2
    left_plus_y=0
    disable_left=False
    disable_right=False
    i=0
    while True:
        #print(print_landscape(landscape.))
        if last_right[1]==1 and last_left[1]==1:
            if random.randint(1, 3)%2==0:
                break
        if left_minus_y==1 and right_minus_y==1:
            break
        if disable_left ==True and disable_right==True:
            break
        if last_left[0]<1:
            print(last_left, "l")
            disable_left=True
        if last_right[0]>most_right-2:
            print(last_right, "r")
            disable_right=True
        if disable_left==False:
            if last_left[1]<4:
                left_plus_y=1
            if last_left[1]<3:
                left_minus_y=1
                left_plus_y=0
            left_y=[last_left[1]-left_minus_y, last_left[1]+left_plus_y]
            left_y.sort()
            """if left_y[1]>5:
                left_y[1]=5
            if left_y[0]>=5:
                left_y[0]=left_y[1]-1"""
            left=(highest_point[0]-i-1, random.randint(left_y[0], left_y[1]))
            landscape.make_column(left)
            last_left=left
        if disable_right==False:
            if last_right[1]<4:
                right_plus_y=1
            
            if last_right[1]<3:
                
                
                right_plus_y=0
            if last_right[1]<=3:
                if last_right[1]>1:
                    right_minus_y=2
                elif last_right[1]==1:
                    right_minus_y=0
            #print(last_left[1]-right_minus_y, last_right[1]+right_plus_y)
            right_y=[last_right[1]-right_minus_y, last_right[1]+right_plus_y]
            right_y.sort()
            
            right=(highest_point[0]+i+1, random.randint(right_y[0], right_y[1]))
            landscape.make_column(right)
            last_right=right
        #if disable_left==False and disable_right==False:
            #print(right_y[0], right_y[1], left_y[0], left_y[1], right_minus_y)
        #else:
            #print("help", disable_left, disable_right, right_y, last_right, right_minus_y, right_plus_y)
        #print(last_left)
        #print(last_right[0]-right_minus_x, last_right[1])
        #print(random.randint(last_right[0]-right_minus_x, last_right[0]))
        i+=1
    #print(h_x, get_landscapes_highest_block(landscape, h_x))
    return landscape.landscape