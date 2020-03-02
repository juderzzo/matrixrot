from display import *
from draw import *
from parse import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
parse_file('Img', edges, transform, screen, color)
