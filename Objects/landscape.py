import numpy as np
from Properties.make_block import make_block
#from MainGameScreenConfig import block_size
import random
class Landscape:
    def __init__(self, rect,block_keys):
        self.size=(rect[2], rect[3])
        self.rect=rect
        self.landscape=np.zeros(shape=(self.size[1], self.size[0]), dtype=int)
        self.block_keys=block_keys
    def print(self, show_coordinates=False):
        max_number_size_y=len(str(len(self.landscape)-1))
        #max_number_size_x=len(str(len(self.landscape[0])-1))
        coordinates_y=""
        if show_coordinates:
            coordinates_x=[str(i)[-1] for i in range(len(self.landscape[0]))]
            coordinate_x_space=[" " for i in range(max_number_size_y+1)]
        for i in range(len(self.landscape)):
            if show_coordinates:
                #if len(str(i))!=max_number_size_y:
                coordinates_y=str(len(self.landscape)-i-1).zfill(max_number_size_y)
                
            print(coordinates_y, self.landscape[len(self.landscape)-i-1])
        if show_coordinates:
            
            print("".join(coordinate_x_space), ', '.join(coordinates_x))
            
            
    def get_landscapes_highest_block(self, x_point):
        #print()
        #print_landscape(landscape)
        for i in range(len(self.landscape)):
            #print(i, x_point)
            if self.landscape[i][x_point]==0:
                return i
        return None
    def make_column(self, point):
        for i in range(point[1]):
            if random.random()<0.1 and i ==point[1]-1:
                self.landscape[i][point[0]]=2
            else:
                self.landscape[i][point[0]]=1
        return self.landscape
    def add_landscape_to_game(self, game_blocks):
        for i in range(len(self.landscape)):
            for ii in range(len(self.landscape[0])):
                
                if self.landscape[i][ii] in self.block_keys:
                    game_blocks.append(self.block_keys[self.landscape[i][ii]](make_block(ii+self.rect[0], len(self.landscape)-i+self.rect[1])))
                    #print(make_block(ii, len(self.landscape)-i))
                    #print(make_block(ii+self.rect[0], len(self.landscape)-i+self.rect[1]))