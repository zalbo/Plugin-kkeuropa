import pry
import re
import sys

from Tkinter import *
from tkFileDialog import askopenfilename


root = Tk()
# Create single line text entry box
x_station_field_text = Entry(root)
x_station_field_text.pack()






#open and edit file

def procesfile():
    x_station = (x_station_field_text.get())


    file_gcode = askopenfilename(parent=root)
    with open(file_gcode) as f:
        content = f.readlines()


        array_index = []
        target_e = 7
        last_current_e = 0



        #example
        for index, val in enumerate(content):

            #find current_e
            match_e = re.search('E(\d+)', val)
            match_z = re.search('Z(\d+\.\d+)', val)

            if match_z:

                current_z = match_z.group(1)

            #cerca l'index da inserire il codice
            if match_e:
                current_e = int(match_e.group(1))
                if current_e % target_e == 0 and last_current_e != current_e:
                    current_e_precise = re.findall('E(\d+\.\d+)', val)[0]
                    current_x = re.findall('X(\d+\.\d+)', val)[0]
                    current_y = re.findall('Y(\d+\.\d+)', val)[0]
                    array_index.append([index,current_x,current_y,current_z,current_e_precise]) # [index, x , y , z , e]
                    last_current_e = current_e



                        #cerca la linea dell'array content e inserisce dove deve inserire

        for index, val in enumerate(content):
            for line_correct_to_insert in array_index:
                if index == line_correct_to_insert[0]:
                    current_x = line_correct_to_insert[1]
                    current_y = line_correct_to_insert[2]
                    current_z = line_correct_to_insert[3]
                    current_e_precise = line_correct_to_insert[4],
                    pry()
                    content.insert(index + 1 , ";TYPE:CUSTOM\nM83 ;pluginSet extruder to relative mode\nG1 Z10 F300\nG1 X190.000000 Y190.000000 F9000\nG1 Z15 F300\nM84 E0\nG1 Z10 F300\nG1 F9000\nM82\nG1 Z" + current_z + "\nG92 E" + current_e_precise + " ;Set Position\n")


#save the file
    import os
    filename = os.path.basename(file_gcode).replace('.gcode', '')
    thefile = open(filename +'_modificato.gcode', 'w+')
    for item in content:
        thefile.write(item)



# Print the contents of entry widget to console


# Create a button that will print the contents of the entry
button = Button(root, text='EDIT GCODE', command=procesfile)
button.pack()

root.mainloop()
