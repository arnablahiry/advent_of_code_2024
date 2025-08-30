import numpy as np

mul_enabled = True

with open('input.txt','r') as f:
    numbers = []
    for line in f:
       i=0
       while i<(len(line)):
        
            str_dont = ''+line[i:i+7]
            str_do = ''+line[i:i+4]
            if str_dont=="don't()":
                i+=7
                mul_enabled = False
            if str_do == "do()":
                i+=4
                mul_enabled = True

            str = ''+line[i:i+4]
            if str == 'mul(' and mul_enabled:
                j=i+4
                num1 = ''
                num2=''
                while j<len(line) and line[j]!=',' and len(num1)<3:
                    if line[j].isdigit():
                        num1 += line[j]
                        j+=1
                    else:
                        break
                # must have a comma next
                if j < len(line) and line[j] == ',':
                    j += 1
                    char = line[j]
                else:
                    i += 1
                    continue
                while j<len(line) and line[j]!=')'and len(num2)<3:
                    if line[j].isdigit():
                        num2 += line[j]
                        j+=1
                    else:
                        break
                
                if line[j]==')':
                    j+=1
                else:
                    i+=1
                    continue

                

                if num1!='' and num2!='':
                    numbers.append((float(num1), float(num2)))
                    i=j
                else:
                    i+=1
            else:
                i+=1
                
            

numbers = np.asarray(numbers)
print(int(np.sum(numbers[:,0]*numbers[:,1])))



   