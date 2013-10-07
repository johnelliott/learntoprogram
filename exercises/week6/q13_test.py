import tkinter.filedialog, q13

to_filename = 'C:/Python33/class/learntoprogram/exercises/week6/q13.txt' #tkinter.filedialog.asksaveasfilename() # make file to write to
print('file:', to_filename) # print file to open
file = open(to_filename, 'w') # open file for writing

q13.write_to_file(file, ['sentence one!','second! non sentence','THis is the thirdd']) # call function to test

file.close() # close file when done

## Now read and print to check that it's been written

file = open(to_filename, 'r') # open file for reading
contents = file.read() # read file into variable
print(contents) # print to prompt
file.close() # close file when done

# YESS

