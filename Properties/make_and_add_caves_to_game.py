from Objects.cave_generator import Cave_generator
from MainGameScreenConfig import *
from Properties.round_up_down import *
 

        
def make_and_add_caves_to_game(game_size_rect, game_blocks, cave_variables):
    cave_2d_list=[]
    block_list=[]
    for i in game_blocks:
        block_list.append((i.rect.x, i.rect.y))
    for y in range(game_size_rect[3]):
        cave_2d_list.append([])
        for x in range(game_size_rect[2]):
            if (x*BLOCK_SIZE, y*BLOCK_SIZE) not in block_list:
                #print(1)
                #cave_2d_list[y].append(-1)
                cave_2d_list[y].append(-1)
            else:
                cave_2d_list[y].append(0)
    cave_generator=Cave_generator(cave_2d_list, game_size_rect, cave_variables[0], cave_variables[1], cave_variables[2], cave_variables[3])
    cave_generator.generate_map()
    cave_generator.add_caves_to_game(game_blocks)
    #print(cave_generator.get_all_caves()[0])

    