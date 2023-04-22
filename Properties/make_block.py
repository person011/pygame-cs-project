from MainGameScreenConfig import BLOCK_SIZE
def make_block(x, y, size=BLOCK_SIZE):
    return (x*size, y*size, size, size)