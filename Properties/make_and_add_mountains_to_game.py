from Objects.mountain_generator import Mountain_generator

from Properties.make_mountains import make_mountain

def make_and_add_mountains_to_game(game_size_rect, num_of_mountains, game_blocks):
    landscape=Mountain_generator(game_size_rect)
    for i in range(num_of_mountains):
        make_mountain(landscape)
        
    
    landscape.add_landscape_to_game(game_blocks)