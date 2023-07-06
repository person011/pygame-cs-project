import math
def round_down(num, multiple):
        return num-(num%multiple)
def round_up(x, multiple):
    return int(math.ceil(x / multiple)) * multiple