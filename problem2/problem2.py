import numpy as np

file = open('input.txt', 'r')

input = []
count = 0
count_dampened = 0
for line in file:
    #row = np.genfromtxt((line))
    line_num = np.asarray(list(map(int, line.split())))
    count_line = 0
    if (np.array_equal(line_num, np.sort(line_num)) or (np.array_equal(line_num,-np.sort(-line_num)))):
        for i in range(len(line_num)-1):
            if 1<= np.abs(line_num[i] - line_num[i+1])<= 3:
                count_line+=1
        if count_line==len(line_num)-1:
            count+=1
            continue

    for i in range(len(line_num)):
        line_temp = line_num.copy()
        line_temp = np.delete(line_temp,i)
        count_line = 0
        if (np.array_equal(line_temp, np.sort(line_temp)) or (np.array_equal(line_temp,-np.sort(-line_temp)))):
            for j in range(len(line_temp)-1):
                if 1<=np.abs(line_temp[j] - line_temp[j+1]) <= 3:
                    count_line+=1
            if count_line==len(line_temp)-1:
                count_dampened+=1
                break






        
print(count, count+count_dampened)


