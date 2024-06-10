import math

class Zadanie:
    def __init__(self, p, w, d, id):
        self.p= p
        self.w= w
        self.d= d
        self.id= id




def readData(path):

    zadania= []
    file= open(path, 'r', encoding='utf-8')
    i= 0
    for line in file:
        line= line.replace("\n", "")
        data= line.split(" ")
        zadania.append(Zadanie(int(data[0]), int(data[1]), int(data[2]), int(i+1)))
       # print(zadania[i].p, zadania[i].w, zadania[i].d, zadania[i].id)
        i+= 1 
    return zadania

def prepareMasks(zadania):
    masks= []
    n= len(zadania)
    #print("dlugosc zdanL ", n)
    bn= int(math.pow(2,n)- 1)
    
    
    for i in range(1, bn+1):
        b = f"{i:0{n}b}"
        #print(z.id, b)
        b_mask= str(b[::-1])
        #print("i:, i, "" b_mask: ", b_mask)
        masks.append(b_mask)
        fees.append(0)
    

    return masks
def contain_same_elements(a, b):
    flag= True
    if len(a) == len(b):
        for e in a:
            if e not in b:
                return False
    else:
        return False

    return flag 

def find_fee(czlon):
    fee= 0
    for i in range(len(masks_zadania)):
        task= masks_zadania[i]
        if contain_same_elements(czlon, task):
            return fees[i]

        #porownaj czy czlon i zadania posiada te same elememty


    return fee 


def witi(zadania, masks):
    ctime= math.inf
    uszeregowanie= ''
   
    for m in masks:
       str_m= str(m)
       sub_zadania= []

       j= 0
       for b in str_m:
           if b == '1':
               sub_zadania.append(zadania[j])
               #print(b, " dodaje: ")
           j+=1
       masks_zadania.append(sub_zadania)
       #print("m: ", m, sub_zadania)
    
    i= 0
    for s in masks_zadania:
       #print("dlugosci: ", s, len(s))
       if len(s) == 1 :
          # print("obliczam dla jednego zadania")
           task= s[0]
           fee = max(task.p - task.d, 0)*task.w
           fees[i]= fee
       else:
           #print("obliczam dla wielu musze sprawdzic wczesniej")
           czlon= s[:len(s)-1]
           last_elemnt= s[-1]

           #teraz robie to dla jednej kombinacji, powinienen kazdy elemnt wyrzucic na koniec i obliczyc kare

           #znajdz kare czlonu
           czlon_fee= find_fee(czlon)
           #znajdz czas czlonu
           czlon_time= 0
           for c in czlon:
               czlon_time+= c.p
          
           last_elemnt_fee= max(czlon_time + last_elemnt.p - last_elemnt.d, 0)*last_elemnt.w
           fees[i]= czlon_fee + last_elemnt_fee
               
          
       i+=1
    
            
    return uszeregowanie, ctime





   
    

fees= []
masks_zadania= []
zadania= readData("data11.txt")
masks= prepareMasks(zadania)
best_uszeregowanie, min_fee= witi(zadania, masks)
print(masks[-1])
print(fees[-1])
#print(masks)
#print(masks_zadania)

#print(fees)