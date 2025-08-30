import numpy as np

input = np.loadtxt('input.txt')

first_list = np.sort(input[:,0])
second_list = np.sort(input[:,1])

print(int(np.sum(np.abs(first_list-second_list))))

sim_index = 0
for number1 in first_list:
    count = 0
    for number2 in second_list:
        if number2 == number1:
            count+=1
    sim_index+=number1*count

print(int(sim_index))
    


