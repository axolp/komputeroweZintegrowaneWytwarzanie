class Zadanie:
    r= 0
    p= 0
    q= 0
    id= 0
    flag= ''

    def __init__(self, r, p, q, id):
        self.r= r
        self.p= p
        self.q= q
        self.id= id
        self.flag= 'in_preperation'



def sort_zadania_max(zadania):
    for i in range(len(zadania)):
        for j in range(len(zadania) -1):
            if zadania[j].q < zadania[j+1].q:
                zadania[j], zadania[j+1] = zadania[j+1],  zadania[j]


    return zadania

def shrage(zadania):
    n= len(zadania)
    cmax= 0
    tbd= []
    zrobione= []
    t= 0
    t_styg= 0
    kolejnosc= ''
    while len(zrobione) != len(zadania):

        #wybierz zadania ktore sa gotowe do wejscia na maszyne
        for i in range(len(zadania)):
            print("wyswietlam i z petli: ", i)
            z= zadania[i]

            if z.r <= t and z.flag == 'in_preperation':
                z.flag= 'waiting_for_the_machine'
                tbd.append(z)

            else:
                t+= 1

        #z zadana gotowych do wejscia na maszyne wybierz te o najwiekszym q
        tbd_sort= sort_zadania_max(tbd)

        for i in range(len(tbd_sort)):
            print(tbd_sort[i].q)

        for i in range(len(tbd_sort)):
            if tbd_sort[i].flag == 'waiting_for_the_machine':
                tbd_sort[i].flag= 'done'
                zrobione.append(tbd_sort[i])
                t+= tbd_sort[i].p
                print("dodaje zadanie: ", tbd_sort[i].id, "o czasie r: ", tbd_sort[i].r, "jest czas:", t)
                kolejnosc= kolejnosc +  str(tbd_sort[i].id)+ " "
                t_styg= t + tbd_sort[i].q
                break

        cmax= max(t, t_styg)
        print("kolejnosc: ", kolejnosc) 
    return zrobione


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


zadania= []
file= open('data3.txt', 'r', encoding='utf-8')
i= 0
for line in file:
    line= line.replace("\n", "")
    
    data= line.split(" ")
    
    zadania.append(Zadanie(int(data[0]), int(data[1]), int(data[2]), int(i+1)))
    print(zadania[i].r, zadania[i].p, zadania[i].q, zadania[i].id)
    i+= 1 



print(compute_cmax(shrage(zadania)))



