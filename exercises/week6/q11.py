import tkinter.filedialog

file_path = tkinter.filedialog.askopenfilename() # ask for data file
print('file:', file_path) # print file to open

data_file = open(file_path, 'r') # open file for reading


# data_file refers to a file open for reading.
for line in data_file:
    print(line.rstrip('\n'))
