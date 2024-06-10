import numpy as np
import math
import copy
import random
import matplotlib.pyplot as plt  






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



def without_tabu(schedule, tabu_features):
    for i in range(len(schedule) -1):
        for t in tabu_features:
            idx1= t[0]
            idx2= t[1]
            if schedule[i] == idx1 and schedule[i+1] == idx2:
                return False
    return True

def tabu(n, schedule):
    tabu_featues= []
    cmaxes= []
    iteracje= []
    for i in range(20000):
        if 3000%(i+1) == 120:
            print(i)
        iteracje.append(i)
        best_cmax= math.inf
       
        tabu_a= None
        tabu_b= None
        #(1,3) elementy 1 i 3 nie moga byc koło siebie

        tmp_schedules= []
       # print("deafult schedule")
       # print(schedule)
       # print("tabu schedule")
        
        #wygeneruj wszystkie uszeregowania 
        swap_idx = random.randint(0, len(schedule)- 1)
        tabu_a= swap_idx
        for i, e in enumerate(schedule):
            tmp_schedule= schedule[:]
            #if e != swap_idx:
            #print("zamien ", swap_idx, i)
            tmp_schedule[swap_idx], tmp_schedule[i] = tmp_schedule[i], tmp_schedule[swap_idx]
            tmp_schedules.append(tmp_schedule)
                #print(tmp_schedule)
        
        #sprawdz ktore nie sa tabu i wyberz best cmax
        min_cmax = math.inf
        best_idx = None

        for i, s in enumerate(tmp_schedules):
            if without_tabu(s, tabu_featues):
                cmax=  compute_cmax(s)
                #print(s, cmax)
                if cmax < min_cmax:
                    min_cmax = cmax
                    best_idx = i
                    tabu_b= s[1]
        #print("min cmax: ", min_cmax)
        cmaxes.append(min_cmax)
        
        #dla najmniejszego cmax dokonaj zmian w schedule i dodaj nowa ceche tabu
        if(len(tabu_featues) == n):
            tabu_featues.pop(0)
        if best_idx:
            #print(best_idx)
            schedule= tmp_schedules[best_idx]
            new_tabu_feature = [tabu_a, tabu_b]
            tabu_featues.append(new_tabu_feature)
       
       
  
            



       


      
                
                    
    plt.plot(iteracje,cmaxes)
    plt.show()        
    return best_cmax
        


            

        
zadania= []   

n, m= read_data("data002.txt")


schedule= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
tabu(12, schedule)



          