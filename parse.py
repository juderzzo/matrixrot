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
    instructions = finput.read().split("\n")
    i = 0
    while(i < len(instructions)):
      upshift = 1
      if(instructions[i] == 'ident'):
        ident(transform)
      if(instructions[i] == 'apply'):
        matrix_mult(transform, verticies)
      if(instructions[i] == 'display'):
        clear_screen(screen)
        draw_lines(verticies, screen, color)
        display(screen)
      if(instructions[i] == "save"):
        clear_screen(screen)
        draw_lines(verticies, screen, color)
        display(screen)
        save_extension(screen, commands[i+1])
        upshift = 2
      if(instructions[i] == "line"):
        newverticies = instructions[i+1].split()
        add_edge(verticies, int(newverticies[0]), int(newverticies[1]), int(newverticies[2]), int(newverticies[3]), int(newverticies[4]), int(newverticies[5]))
        upshift = 2
      if(instructions[i] == "scale"):
        newverticies = instructions[i+1].split()
        matrix_mult(make_scale(int(newverticies[0]), int(newverticies[1]), int(newverticies[2])), transform)
        upshift = 2
      if(instructions[i] == "rotate"):
        nextstuff = instructions[i+1].split()
        if(nextstuff[0] == "x"):
          matrix_mult(make_rotX(int(nextstuff[1])), transform)
        if(nextstuff[0] == "y"):
          matrix_mult(make_rotY(int(nextstuff[1])), transform)
        if(nextstuff[0] == "z"):
          matrix_mult(make_rotZ(int(nextstuff[1])), transform)
        upshift = 2
      if(instructions[i] == "move"):
        newverticies = instructions[i+1].split()
        matrix_mult(make_translate(int(newverticies[0]), int(newverticies[1]), int(newverticies[2])), transform)
        upshift = 2
      if(instructions[i] == "quit"):
        break
      i += upshift
