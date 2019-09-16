# texto / binários

file = open('teste.txt', 'r')
for line in file:
    line = line.replace('\n', '')
    print(line)
file.close()

file = open('teste.txt', 'w')
file.write('ola weuler\n')
file.write('academia de python')
file.close()

# open()

# read()

# readline()

# readlines()

# with
with open('teste.txt', 'r') as file:
    for line in file:
        print(line)
    