from math import *
from itertools import tee


def read_from_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    x_coord = list(map(int, lines[0].split(",")))
    y_coord = list(map(int, lines[1].split(",")))
    return list(zip(x_coord, y_coord))


def write_into_file(filename, text):
    with open(filename, 'w') as filename:
        filename.write(text)


def distance(stud0, stud1):
    d = pow(pow(stud0[0] - stud1[0], 2) + pow(stud0[1]-stud1[1], 2), 0.5)
    return d

# def pair_adjacent2(iterable):
#     # "s -> (s0, s1), (s2, s3), (s4, s5), ..."
#     a = iter(iterable)
#     return zip(a, a)


def pair_adjacent(list):
    # "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(list)
    next(b, None)
    return zip(a, b)


def max_dist(list_of_dist):
    return round(max(list_of_dist), 2)



stud_coords = read_from_file('eggs.in')
print(stud_coords)
print(sorted(stud_coords))

list_of_distances = []
for stud0, stud1 in pair_adjacent(sorted(stud_coords)):
    print(stud0, stud1)
    list_of_distances.append(distance(stud0, stud1))
print(list_of_distances)

print("The longest distance of a throw: " + str(max_dist(list_of_distances)))

write_into_file("eggs.out", str(max(list_of_distances)))

