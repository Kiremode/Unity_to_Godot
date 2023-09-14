#unity script to godot script converter
import re
from scripts.look_up_table import look_up_table, look_up
from scripts.regEx_search import regEx_search

file = input("Enter the folder path: ")

#redesign: 
# get output folder
# recreate folder structure
# check if 2D or 3D
#remove the public / private / protected keywords by voides
# make a function that goes over the lookuptable and replaces the keys with the values
# go through each line of the file and replace the keys with the values with the regex function

def convert(file):
    #remove the .cs extension
    file_read = open(file, "r")
    #file = open(file + ".cs", "r")
    file_name = file[:-3]
    #add the _godot.cs extension to a new file
    new_file = open(file_name + "_godot.cs", "w+")

    #go through each line of the file
    for line in file_read:
        #go through each key in the look_up table
        line = regEx_search(new_file,line)
        line = look_up_table(line)
        for command, replacement in look_up.items():
            pass
            #if the key is in the line
            if command in line:
                #replace the key with the value
                line = line.replace(command, replacement, 1)
                break
        #write the new line to the new file
        new_file.write(line)

convert(file)
