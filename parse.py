from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""

def parse_file( filename, verticies, transform, screen, color ):

    finput = open(filename, 'r')
    orders = finput.read().split("\n")
    i = 0
    while(i < len(orders)):
      counter = 1
        #for each case we're gonna try to do the following
        #first get the string, then convert it to what we want the respective function to be
            
            if(orders[i] == "line"):
                #if we wanna draww a line lets just use our handy addedge command
              newverticies = orders[i+1].split()
              add_edge(verticies, int(newverticies[0]), int(newverticies[1]), int(newverticies[2]), int(newverticies[3]), int(newverticies[4]), int(newverticies[5]))
              counter = 2
            if(orders[i] == "scale"):
                #scaling is same as line
              newverticies = orders[i+1].split()
              matrix_mult(make_scale(int(newverticies[0]), int(newverticies[1]), int(newverticies[2])), transform)
              counter = 2
            if(orders[i] == "rotate"):
                #roate we need to multiply our respective transformation matrix
                #for each rotation matrix, we wanna multiple our respective coordinate by that matrix
              rotator = orders[i+1].split()
              if(rotator[0] == "x"):
                matrix_mult(make_rotX(int(rotator[1])), transform)
              if(rotator[0] == "y"):
                matrix_mult(make_rotY(int(rotator[1])), transform)
              if(rotator[0] == "z"):
                matrix_mult(make_rotZ(int(rotator[1])), transform)
              counter = 2
            if(orders[i] == "move"):
                #move just shifts it its the same as the other transoformations we got
              newverticies = orders[i+1].split()
              matrix_mult(make_translate(int(newverticies[0]), int(newverticies[1]), int(newverticies[2])), transform)
              counter = 2
      if(orders[i] == 'ident'):
          #ez pez
        ident(transform)
      if(orders[i] == 'apply'):
          #ok this just makes all the magic happen
        matrix_mult(transform, verticies)
      if(orders[i] == 'display'):
          #display from earlier, show the screen
        clear_screen(screen)
        draw_lines(verticies, screen, color)
        display(screen)
      if(orders[i] == "quit"):
        break
      i += counter
