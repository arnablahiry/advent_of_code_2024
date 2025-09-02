import numpy as np



with open('input.txt','r') as f:

    lines = []
    for line in f:
        lines.append(list(line.strip()))


count = 0

for i in range(len(lines)):
    for j in range(len(lines[i])-3):
        line_hor = ''.join(lines[i][j:j+4])
        if line_hor=='XMAS' or line_hor[::-1]=='XMAS':
            count+=1

for i in range(len(lines)-3):
    for j in range(len(lines[i])):
        line_vert = ''.join([lines[i+k][j] for k in range(4)])
        if line_vert=='XMAS' or line_vert[::-1]=='XMAS':
            count+=1

for i in range(len(lines)-3):
    for j in range(len(lines[i])-3):
        line_diag = ''.join([lines[i+k][j+k] for k in range(4)])
        if line_diag=='XMAS' or line_diag[::-1]=='XMAS':
            count+=1

for i in range(len(lines)-3):
    for j in range(len(lines[i])-3):
        line_diag = ''.join([lines[i+k][len(lines[i])-(j+k)-1] for k in range(4)])
        if line_diag=='XMAS' or line_diag[::-1]=='XMAS':
            count+=1
print(count)



count_part2 = 0
for i in range(len(lines)-2):
    for j in range(len(lines[i])-2):
        hor_limit = j+2
        ver_limit = i+2
        mas1 = ''.join([lines[i+k][j+k] for k in range(3)])      
        mas2 = ''.join([lines[i+k][hor_limit-k] for k in range(3)])     

        if (mas1=='MAS' or mas1[::-1]=='MAS') and (mas2=='MAS' or mas2[::-1]=='MAS'):
            count_part2 += 1

print(count_part2)
