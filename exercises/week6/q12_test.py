import q12, tkinter.filedialog


## file_path = tkinter.filedialog.askopenfilename() # ask for data file, but now just go to the same file
file_path = 'C:/Python33/class/learntoprogram/exercises/week6/q12.txt'

print('file:', file_path) # print file to open
file = open(file_path, 'r') # open file for reading
print(q12.lines_startswith(file, 'l')) # print function call

file_path.close()
