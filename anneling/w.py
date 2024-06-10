import numpy as np
import math
import copy
import random
import matplotlib.pyplot as plt  # Import matplotlib for plotting






class Zadanie:
    def __init__(self, zadania, sum, id):
        self.zadania= zadania
        self.sum= sum
        self.id= id

def read_data(path):
    
    file= open(path, 'r', encoding='utf-8')
    for i, line in enumerate(file):
        line= line.replace("\n", "")
        data= line.split(" ")
        if i == 0:
            n= int(data[0]) -1
            m= int(data[1]) 
        else:
            tmp= []
            sum= 0
            for z in data:
                tmp.append(int(z))
                sum+= int(z)
            tmp= np.array(tmp).reshape((m,1))
            zadania.append(Zadanie(tmp, sum, i))
    return n, m

def compute_cmax(schedule):
    n= len(schedule)
    cmax_array= zadania[schedule[0]].zadania
    for s in range(1, len(schedule)):
        cmax_array= np.hstack((cmax_array, zadania[schedule[s]].zadania))
    #print(cmax_array)

    for j in range(m):
        for i in range(n):
            #print("j, i: ", j, i , cmax_array[j][i])
            if j == 0:
                if i > 0:
                    cmax_array[j][i]= cmax_array[j][i] + cmax_array[j][max(i -1, 0)] 
            else:
                cmax_array[j][i]= cmax_array[j][i] + max(cmax_array[j][max(i-1, 0)],cmax_array[max(j-1, 0)][i])
    #print(cmax_array)
    return cmax_array[-1][-1]

def sig(x):
 return 1/(1 + np.exp(-x))

def decision(p):
    decision= random.random() <p
    return decision

def simulate_annealing(t, n, t_drop, schedule):
        cmax= compute_cmax(schedule)
        itr= 0
        for j in range(n):
            if t <0.1:
                break
            
            tmp_schedule= schedule[:]
            swap_idx = random.randint(0, len(schedule)- 1)
            destination_idx= random.randint(0, len(schedule)- 1)
            tmp_schedule[swap_idx], tmp_schedule[destination_idx] = tmp_schedule[destination_idx], tmp_schedule[swap_idx]
           
            new_cmax= compute_cmax(tmp_schedule)
            print(new_cmax)
            itr+=1 
            iteracje.append(itr)
            cmaxy.append(new_cmax)

            if new_cmax < cmax:
                cmax= new_cmax
                schedule= tmp_schedule
                #print("new schedule: ", schedule)
            else:
                #print("licze prawdopodobniestwo")
                d= new_cmax - cmax
                p= math.pow(math.e, -(d/t))
                print("p: ", p)
                if decision(p):
                     schedule= tmp_schedule
                     #print("new schedule delta: ", schedule)

                t*= t_drop
        return cmax
        


            

        
zadania= []   
cmaxy= []   
iteracje= []
n, m= read_data("data000.txt")


schedule= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
cmax= compute_cmax(schedule)
print(cmax)


simulate_annealing(1000, 30000, 0.99, schedule)

plt.plot(iteracje,cmaxy)
plt.show()

          