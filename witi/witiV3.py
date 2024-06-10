import math

class Zadanie:
    def __init__(self, p, w, d, id):
        self.p = p
        self.w = w
        self.d = d
        self.id = id

def readData(path):
    zadania = []
    with open(path, 'r', encoding='utf-8') as file:
        i = 0
        for line in file:
            line = line.replace("\n", "")
            data = line.split(" ")
            zadania.append(Zadanie(int(data[0]), int(data[1]), int(data[2]), int(i+1)))
            i += 1 
    return zadania

def prepareMasks(zadania):
    masks = []
    n = len(zadania)
    bn = int(math.pow(2, n) - 1)
    
    for i in range(1, bn + 1):
        b = f"{i:0{n}b}"
        b_mask = str(b[::-1])
        masks.append(b_mask)
        fees.append(0)
        schedules.append([])  
    
    return masks

def contain_same_elements(a, b):
    return sorted(a) == sorted(b)

def find_fee_and_schedule(czlon):
    czlon_ids = []
    for task in czlon:
        czlon_ids.append(task.id)
    
    for i in range(len(masks_zadania)):
        task_set = masks_zadania[i]
        task_set_ids = []
        for task in task_set:
            task_set_ids.append(task.id)
        
        if sorted(czlon_ids) == sorted(task_set_ids):
            return fees[i], schedules[i]
    return 0, []


def witi(zadania, masks):
    global fees, masks_zadania, schedules
    fees = [0] * len(masks)
    masks_zadania = []
    for m in masks:
        str_m = str(m)
        sub_zadania = []
        j = 0
        for b in str_m:
            if b == '1':
                sub_zadania.append(zadania[j])
            j += 1
        masks_zadania.append(sub_zadania)
    for i in range(len(masks_zadania)):
        s = masks_zadania[i]
        if len(s) == 1:
            task = s[0]
            fees[i] = max(task.p - task.d, 0) * task.w
            schedules[i] = [task.id] 
        else:
            min_fee = math.inf
            best_schedule = []
            for k in range(len(s)):
                temp_s = s[:k] + s[k+1:]
                last_element = s[k]

                czlon_fee, czlon_schedule = find_fee_and_schedule(temp_s)
                czlon_time = sum(task.p for task in temp_s)
                
                last_element_fee = max(czlon_time+last_element.p-last_element.d,0)*last_element.w
                total_fee = czlon_fee + last_element_fee
 
                if total_fee < min_fee:
                    min_fee = total_fee
                    best_schedule = czlon_schedule + [last_element.id]  
            
            fees[i] = min_fee
            schedules[i] = best_schedule  
          
    return schedules[-1], fees[-1]


fees = []
schedules = [] 
zadania = readData("data2.txt")
masks = prepareMasks(zadania)
best_schedule, min_fee = witi(zadania, masks)
print("Minimalna kara:", min_fee)
print("Najlepsze uszeregowanie:", best_schedule)
