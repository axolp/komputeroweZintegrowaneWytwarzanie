import itertools
import math


class Zadanie:
    r= 0
    p= 0
    q= 0
    id= 0
    flag= ''
    rp= 0
    rq= 0
    pq= 0

    def __init__(self, r, p, q, id):
        self.r= r
        self.p= p
        self.q= q
        self.id= id
        self.flag= 'in_preperation'
        self.rp= r+p
        self.rq= r+q
        self.pq= p+q

def compute_cmax(zadania):
     cmax= 0

     t= 0
     t_styg= 0
     for z in zadania:
          if t >= z.r:
               t+= z.p
               t_styg= max(t_styg, t+z.q)

          else:
               t= z.r
               t+= z.p
               t_styg= max(t_styg, t+z.q)
     cmax= max(t, t_styg)

     return cmax

def sort_zadania_max(zadania, flag):
    tab= zadania[:]
    if flag == 'r':
        for i in range(len(tab)):
            for j in range(len(tab) -1):
                if tab[j].r < tab[j+1].r:
                    tab[j], tab[j+1] = tab[j+1],  tab[j]
        

    elif flag == 'q':
        for i in range(len(tab)):
                for j in range(len(tab) -1):
                    if tab[j].q < tab[j+1].q:
                        tab[j], tab[j+1] = tab[j+1],  tab[j]

    elif flag == 'rp':
        for i in range(len(tab)):
                for j in range(len(tab) -1):
                    if tab[j].rp < tab[j+1].rp:
                        tab[j], tab[j+1] = tab[j+1],  tab[j]

    elif flag == 'rq':
        for i in range(len(tab)):
                for j in range(len(tab) -1):
                    if tab[j].rq < tab[j+1].rq:
                        tab[j], tab[j+1] = tab[j+1],  tab[j]
    elif flag == 'pq':
        for i in range(len(tab)):
                for j in range(len(tab) -1):
                    if tab[j].pq < tab[j+1].pq:
                        tab[j], tab[j+1] = tab[j+1],  tab[j]

    return tab

def neh(zadania, permutation, n):
     dostepne= zadania[n:]
     
     indeks_zadania= 0
     while len(permutation) != len(zadania):
          best_cmax= math.inf
          best_i= 0
          for i in range(len(permutation) +1):
               trial_uszeregowanie= permutation[:]
               trial_uszeregowanie.insert(i, dostepne[indeks_zadania])
               current_cmax= compute_cmax(trial_uszeregowanie)

               if current_cmax < best_cmax:
                    best_cmax= current_cmax
                    best_i= i

          permutation.insert(best_i, dostepne[indeks_zadania])
          indeks_zadania+= 1

     return permutation

def find_best_starting_permutation(permutacje):
    opt= math.inf
    opt_permutacje= []
    for p in permutacje:
         usz= ''
         if compute_cmax(p) < opt:
                   opt= compute_cmax(p)
                   opt_permutacje= p
         for i in range(len(p)):
              usz+=str(p[i].id)
             
         #print(usz, compute_cmax(p))
    print("opt: ", opt)
    print("optymalna permutacja: ", opt_permutacje)
    return opt_permutacje

def pq_jan(zadania, n):
    dostepne= zadania[:n]

    permutacje= list(itertools.permutations(dostepne, len(dostepne)))
    best_starting_permutation= find_best_starting_permutation(permutacje)
    #for z in best_starting_permutation:
         #print(z.id)
    print("zaczynam neha")
    najlepsze_uszeregowanie= neh(zadania, list(best_starting_permutation), n)
    uszeregowanie= ''
    for z in najlepsze_uszeregowanie:
         print("neh id: ", z.id)
         uszeregowanie+= str(z.id)+" "
    opt_cmax= compute_cmax(najlepsze_uszeregowanie)
    print(uszeregowanie)
    return opt_cmax


#zaczytywanie do pliku
zadania= []
file= open('data3.txt', 'r', encoding='utf-8')
i= 0
for line in file:
    line= line.replace("\n", "")
    
    data= line.split(" ")
    
    zadania.append(Zadanie(int(data[0]), int(data[1]), int(data[2]), int(i+1)))
    #print(zadania[i].r, zadania[i].p, zadania[i].q, zadania[i].id)
    i+= 1 

#print(zadania)
max_r= sort_zadania_max(zadania, 'r')
#max_q= sort_zadania_max(zadania, 'q')
#max_rp= sort_zadania_max(zadania, 'rp')
#max_rq= sort_zadania_max(zadania, 'rq')
max_pq= sort_zadania_max(zadania, 'pq')


cmax= pq_jan(max_pq, 5)
print(cmax)