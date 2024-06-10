import numpy as np
import copy
import math
import time


class Zadanie:
    def __init__(self, zadania, sum, id):
        self.zadania= zadania
        self.sum= sum
        self.id= id

def max_sort_zadania():
    z= sorted_zadania = copy.deepcopy(zadania)
    for i in range(len(z)):
        for j in range(len(z) -1):
            if z[j+1].sum > z[j].sum:
                z[j], z[j+1] = z[j+1], z[j]
    return z

def read_data(path):
    file= open(path, 'r', encoding='utf-8')

    for i, line in enumerate(file):
        line= line.replace("\n", "")
        data= line.split(" ")
        if i == 0: 
            n= int(data[0])
            m= int(data[1])
        else:
            sum= 0
            zz= []
            for z in data:
                sum+=int(z)
                zz.append(int(z))
                
            zadania.append(Zadanie(np.array(zz).reshape(m, 1), sum, i-1))
    return n, m

def compute_cmax(schedule):
    cmax= 0
    n= len(schedule)
    #print("mn", m ,n)
    #zbuduj cmax_tab
    for i, idx in enumerate(schedule):
        z= zadania[idx]

        if len(schedule) == 1:
            cmax= z.sum
        else:
            if i == 0:

                cmax_tab = z.zadania
            else:
                tmp= cmax_tab
                cmax_tab = np.hstack((tmp, z.zadania))
              
   
    # j w poziomie, i w pione, j po zadaniach na mszynie, i po maszynach
    if n > 1:
        #print(cmax_tab)
        reversed_cmax_tab= cmax_tab.copy()
        for j in range(m):
            for i in range(n):
                if j == 0:
                    if i != 0:
                        cmax_tab[j][i] = cmax_tab[j][i-1] + cmax_tab[j][i]
                        reversed_cmax_tab[m-1-j][n-1-i]= reversed_cmax_tab[m-1-j][n-1-i+1] + reversed_cmax_tab[m-1-j][n-1-i]
                else:
                    if i == 0:
                        cmax_tab[j][i]= cmax_tab[j][i] + cmax_tab[j-1][i]
                        reversed_cmax_tab[m-1-j][n-1-i]= reversed_cmax_tab[m-1-j][n-1-i] + reversed_cmax_tab[m-1-j+1][n-1-i]
                    else:
                        cmax_tab[j][i] = max(cmax_tab[j][i] + cmax_tab[max(j-1, 0)][i],
                                            cmax_tab[j][i] + cmax_tab[j][max(i-1, 0)])
                        reversed_cmax_tab[m-1-j][n-1-i] = max(reversed_cmax_tab[m-1-j][n-1-i] + reversed_cmax_tab[min(m-1-j+1, m-1)][n-1-i],
                                                            reversed_cmax_tab[m-1-j][n-1-i] + reversed_cmax_tab[m-1-j][min(n-1-i+1, n-1)])

        #print(cmax_tab)
        #print(reversed_cmax_tab)
        cmax= cmax_tab[m-1][n-1]
    return cmax

        


        



zadania= []

n, m= read_data("data060.txt")
sorted_zadania= max_sort_zadania()


#start

schedule= []
start= time.time()
for z in sorted_zadania:
    #znajdx miejsce dla nowego zadania
    if len(schedule) == 0:
        schedule.append(z.id)
    else:
        best_index= 0
        best_cmax= math.inf
        for j in range(len(schedule) +1):
            schedule.insert(j, z.id)
            current_cmax= compute_cmax(schedule)
            del schedule[j]
            if current_cmax < best_cmax:
                best_cmax= current_cmax
                best_index= j
        schedule.insert(best_index, z.id)
#meta
end= time.time()
print("TIME: ", end-start)

print("final odpowiedzi")
print(schedule)
print(compute_cmax(schedule))
        


    

 




