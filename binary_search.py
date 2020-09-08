def BinarySearch(dic, target):
    
    odd_mid = int((len(dic)-1)/2)
    even_mid = int((len(dic))/2)
    
    if len(dic) == 1:
        if dic[0] == int(target):
            print("Target has been found!!")
        else:
            return print("Not found!!")
    elif len(dic) > 1:
        
        if len(dic)%2 == 1: 
            if dic[odd_mid] == target:
                print("Target has been found!!")
            elif dic[odd_mid] != target:
                if dic[odd_mid] > target:
                    left_dic = dic[:odd_mid]
                    return BinarySearch(left_dic, target)
                elif dic[odd_mid] < target:
                    right_dic = dic[odd_mid:]
                    return BinarySearch(right_dic, target)
            
        elif len(dic)%2 == 0:
            if dic[even_mid] == target:
                print("Target has been found!!")
            elif dic[even_mid] != target:
                if dic[even_mid] > target:
                    left_dic = dic[:even_mid]
                    return BinarySearch(left_dic, target)
                elif dic[even_mid] < target:
                    right_dic = dic[even_mid:]
                    return BinarySearch(right_dic, target)
       

a = [1,5,8,10,51]

BinarySearch(a, 5)

