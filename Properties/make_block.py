from MainGameScreenConfig import BLOCK_SIZE
def make_block(x, y, size=BLOCK_SIZE):
    return (x*size, y*size, size, size)
def block_size_to_real_size(block_size, size=BLOCK_SIZE):
    return block_size*BLOCK_SIZE