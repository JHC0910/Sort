def insert_sort(dic):
    
    
    for i in range(1, len(dic)):
        
        j = i
       
        while j > 0:
            if dic[j] < dic[j-1]:
                dic[j], dic[j-1] = dic[j-1], dic[j]
                
            j -= 1
#            print(dic)
    
    return dic

def bubble_sort(dic):
    
    for i in range(len(dic)):
        j = 1
        while j < (len(dic) - i):
            if dic[j-1] > dic[j]:
                dic[j-1], dic[j] = dic[j], dic[j-1]
            j += 1
            
    return dic
    




a = [25,65,19,35,84,10,16,5,11,105,1,67,92,7]

print(bubble_sort(a))
