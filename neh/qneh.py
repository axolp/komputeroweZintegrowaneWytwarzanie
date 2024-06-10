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

def generate_qneh_arrays(schedule):
    cmax= 0
    a= []
    b= []
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
        a= cmax_tab
        b= reversed_cmax_tab
       # print("b", b)
    return a, b

        
def compute_qneh(schedule, z, j,  tab, r_tab):
    cmax= 0
    #vertcial_segment= []
    z= z.zadania
    #print("j", j)
   
    best_cmax= 0
    for i in range(m):
        if j == 0:
            a= z[i][0] + r_tab[i][j]
        elif j == n:
            a= z[i][0] + tab[i][j-1]
        else:
            a= z[i][0] + tab[i][j-1] + r_tab[i][j]
            #vertcial_segment.append(z+tab[i][j])
            #print(i, a)
        if a > best_cmax:
            best_cmax= a
    cmax= best_cmax
    return cmax

        



zadania= []

n, m= read_data("data110.txt")
sorted_zadania= max_sort_zadania()
#schedule= [0,1,2]
#a, b= generate_qneh_arrays(schedule)
schedule= []
cmax= 0
start= time.time()
for z in sorted_zadania:
    #znajdx miejsce dla nowego zadania
    if len(schedule) == 0 or len(schedule) == 1: #w 50 procentach bedzie powodowac problem
        schedule.append(z.id)
    else:
        #print(schedule)
        cmax_tab, reversed_cmax_tab= generate_qneh_arrays(schedule)
        best_index= 0
        best_cmax= math.inf
        for j in range(len(schedule)):
            #print(reversed_cmax_tab)
            current_cmax= compute_qneh(schedule, z, j, cmax_tab, reversed_cmax_tab)
            if current_cmax < best_cmax:
                best_cmax= current_cmax
                best_index= j
        schedule.insert(best_index, z.id)
        cmax= best_cmax
end= time.time()

print("CZAS:", end-start)
print("final odpowiedzi")
print(schedule)
print(cmax)

        


    

 




