import tkinter.filedialog
words_file = open(tkinter.filedialog.askopenfilename(), 'r')
board_file = open(tkinter.filedialog.askopenfilename(), 'r')
print(words_file.read())
print(board_file.read())


