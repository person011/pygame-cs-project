import random
from Properties.make_block import make_block
from Objects.block import block_map

class Cave_generator:
    def __init__(self, land, rect, alive_chance, birth_limit, death_limit, number_of_iterations):
        self.empty_land=[[0 for i in range(len(land[0]))] for i in range(len(land))]
        self.land_with_empty_space=[row[:] for row in land]
        
        self.land=self.remove_empty_space(land)
        
        self.num_to_land = {0:'-', 1:'#', 2:'~'}
        self.alive_chance=alive_chance
        self.birth_limit=birth_limit
        self.death_limit=death_limit
        self.number_of_iterations=number_of_iterations
        self.rect=rect
        self.block_keys=block_map
    def remove_empty_space(self, land):
        new_land=self.empty_land.copy()
        for y in range(len(land)):
            for x in range(len(land[0])):
                if land[y][x]==-1:
                    new_land[y][x]=0
        return new_land
    def replace_tile_with_empty_space(self, land, land_without_spaces):
        new_land=self.empty_land.copy()
        for y in range(len(land)):
            for x in range(len(land[0])):
                if land_without_spaces[y][x] == -1:
                    new_land[y][x]=0
                else:
                    new_land[y][x]=land[y][x]
        return new_land
    
    def print_land(self):
        for i in self.land:
            print(''.join( [self.num_to_land[e] for e in i]))
        print()
            
    def fill_land_with_random(self):

        for i in range(len(self.land)):
            
            for ii in range(len(self.land[0])):
                
                random_chance=random.random()
                
                if random_chance<self.alive_chance:
                    self.land[i][ii]=1
                    
                else:
                    self.land[i][ii]=0
        
    def count_surrounding_alive_cells(self, land, x, y):
        index={0:-1, 1:0, 2:1}
        count=0
        
        for i in range(3):
            xi=index[i]
            for ii in range(3):
                yii=index[ii]
                if (x+xi)>=0 and (x+xi)<len(land[0]):
                    if (y+yii)>=0 and (y+yii)<len(land):
                        if xi!=0 or yii!=0:
                            
                            if land[y+yii][x+xi]==1:
                                count+=1
        return count
    def simulate(self, old_land):
        new_land=self.empty_land
        for y in range(len(old_land)):
            for x in range(len(old_land[0])):
                nac=self.count_surrounding_alive_cells(old_land, x, y)
                if old_land[y][x]==1:
                    if nac<self.death_limit:
                        
                        new_land[y][x]=0
                    else:
                        new_land[y][x]=1
                        
                else:
                    if nac>self.birth_limit:
                        new_land[y][x]=1
                        
                    else:
                        new_land[y][x]=0
                        
        return new_land
    
    def generate_map(self):
        self.fill_land_with_random()
        for i in range(self.number_of_iterations):
            self.land=self.simulate(self.land)
        self.land=self.replace_tile_with_empty_space(self.land, self.land_with_empty_space)

    def flood_fill(self, coordinates, old, field, cave):
    
        def fill(x ,y, old, new, field, cave):
            
            if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
                return
            if field[y][x] != old:
                return
            
            cave.append((y, x))
            field[y][x] = new
            fill(x+1, y, old, new, field, cave)
            fill(x-1, y, old, new, field, cave)
            fill(x, y+1, old, new, field, cave)
            fill(x, y-1, old, new, field, cave)
        field2= [row[:] for row in field]
        fill(coordinates[1] ,coordinates[0], old, "super donut", field2, cave)
        
        return cave
    
    def find_cave_start(self, forbidden_caves):
        for y in range(len(self.land)):
            for x in range(len(self.land[0])):
                if self.land[y][x] == 0:
                    if (y, x) not in forbidden_caves:
                        return y, x
        return None

    def get_all_caves(self):
        caves=[]
        cave_count=0
        while True:
            cave_start=self.find_cave_start(caves)
            if cave_start:
                self.flood_fill(cave_start, 0, self.land, caves)
                cave_count+=1
            else:
                break
        return cave_count, caves
    
    def add_caves_to_game(self, game_blocks):
        #for y in range(len(self.land)):
            #for x in range(len(self.land[0])):

        
        block_list=[]
        for i in game_blocks:
            block_list.append((i.rect.x, i.rect.y))
        new_blocks_to_be_added=[]
        blocks_to_be_deleted=[]
        #print(len(block_list))
        for y in range(len(self.land)):
            for x in range(len(self.land[0])):
                new_block_rect=make_block(x+self.rect[0], (len(self.land)-y)+self.rect[1])
                #print(new_block_rect)
                if (new_block_rect[0], new_block_rect[1]) in block_list:
                    if self.land[y][x] not in self.block_keys:
                        blocks_to_be_deleted.append((new_block_rect[0], new_block_rect[1]))
                
        new_game_blocks=[i for i in game_blocks if (i.rect.x, i.rect.y) not in blocks_to_be_deleted]
        #new_game_blocks.extend(new_blocks_to_be_added)
        #print(len(new_blocks_to_be_added),45)
        #print(len(game_blocks), 1)
        game_blocks[:]=new_game_blocks.copy()
        
    