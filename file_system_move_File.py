import os

source = 'main.txt'

dest = 'newfile.txt'

os.rename(source, dest)

print('O arquivo foi renomeado.')