import numpy as np
import copy
import math
class Maszyna():
    def __init__(self, id, zadania, sum=None):
        self. id= id
        self.zadania= zadania
        self.sum= sum

def readData(path):
    maszyny = []
    n= 0
    m= 0
    with open(path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            data = line.replace("\n", "").split(" ")
            if i == 0:
                n, m = int(data[0]), int(data[1])
                maszyny = [[] for _ in range(m)]
            else:
                for j, d in enumerate(data):
                    maszyny[j].append(int(d))   
                  
             

    
    return n, m, maszyny

def compute_cmax(maszyny, n, m):
    cmax= 0
    cmax_tab= np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            if i == 0:
                cmax_tab[i][j]= maszyny[i].zadania[j] + cmax_tab[i][ max(0, j-1) ]
            else:
                cmax_tab[i][j]= maszyny[i].zadania[j] + max(cmax_tab[i-1][j], cmax_tab[i][max(0, j-1)]) 
    print("tablica cmax: ")
    print(cmax_tab)
    cmax= cmax_tab[m-1, n-1]
    return cmax

def put_the_tasks_in_order(schedule, maszyny, n, m):
    ordered_tasks = [copy.deepcopy(maszyna) for maszyna in maszyny]
    czasy={}
    for i, idx in enumerate(schedule):
        tab= []
        sum= 0
        for j in range(m):
            ordered_tasks[j].zadania[i]= maszyny[j].zadania[idx] 
            sum+=maszyny[j].zadania[idx]
        czasy[idx]= sum

    print("uszeregowanie zadania: ")
    for m in ordered_tasks:
        print(m.zadania)
    return ordered_tasks, czasy

def max_sort(maszyny, czasy):
    items = list(czasy.items())
    n = len(items)
    for i in range(n):
        for j in range(n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    sorted_schedule = [item[0] for item in items]
    return sorted_schedule

def neh(maszyny, sorted_tasks, n, m):
    opt_schedule = []
    opt_cmax = math.inf

    for task in sorted_tasks:
        min_cmax = math.inf
        min_schedule = None

        for i in range(len(opt_schedule) + 1):
            temp_schedule = opt_schedule[:]
            temp_schedule.insert(i, task)
            ordered_tasks, _ = put_the_tasks_in_order(temp_schedule, maszyny, n, m)
            cmax = compute_cmax(ordered_tasks, n, m)
            if cmax < min_cmax:
                min_cmax = cmax
                min_schedule = temp_schedule

        opt_schedule = min_schedule
        opt_cmax = min_cmax
        print("Current best schedule:", opt_schedule, "with Cmax:", opt_cmax)

    return opt_cmax, opt_schedule
    




    return opt_cmax

#ODCZYTAJ DANE
n, m, zadania_na_maszyne= readData("dataxxx.txt")
maszyny = [Maszyna(i, zadania_na_maszyne[i]) for i in range(m)]

#KOLEJNSC, CMAXY
starting_schedule= list(range(n))
ordered_tasks, czasy = put_the_tasks_in_order(starting_schedule, maszyny, n, m)
sorted= max_sort(maszyny, czasy)
cmax = compute_cmax(ordered_tasks, len(starting_schedule), m) 
opt_cmax= neh(maszyny, sorted, n, m)




print("zaczytane zadania: ")
for xxx in maszyny:
        print(xxx.zadania) 
print("czasy: ", czasy)
print("posortowane: ", sorted)
print("cmax: ", cmax)

print("final: ", opt_cmax)



