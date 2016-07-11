import random
import string

fout = open('activation_code.txt','w')

addstr = ''
for count in range(1,201):
    addstr += '[' + str(count) + '] '
    for i in range(15):
       addstr += random.choice(string.letters + string.digits)
    addstr += '\n'

fout.write(addstr)
fout.close()
