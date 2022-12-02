import random 
def make_mountain(list):
    highest_point=(random.randint(0, 19), random.randint(0, 4))
    print(highest_point)

landscape=[
        [],
        [],
        [],
        [],
        [],

    ]
for i in range(5):
    for ii in range(20):
        
        landscape[i].append(0)
        
def print_landscape(landscape):
    print(landscape[0])
    print(landscape[1])
    print(landscape[2])
    print(landscape[3])
    print(landscape[4])
print_landscape(landscape)
make_mountain