import pry

#open file
with open('gcodesano/cube.gcode') as f:
    content = f.readlines()

#example
content[0] = "ciao\n"


#save the file
thefile = open('cube.gcode', 'w')
for item in content:
  thefile.write(item)
