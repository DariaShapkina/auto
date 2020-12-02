from collections import *
import json
from pprint import pprint

global MAX , T 

def MaxString(A,s,k):
    global MAX , T 
    if (k> len(s)):
        return (T, MAX)
    else:
        data = OrderedDict()
        with open(A, 'r', encoding='utf-8') as fh:
            #открываем файл на чтение    
            data = json.load(fh) 
        start = data[0]['start'][0]
        finish = data[0]['finish']
        matrix = data[0]['matrix']
        ss = matrix.get(start) #подсловарь начального значения
        state = True
        check = False
        maxi = 0
        t = 0
        while (state == True and k < len(s)):
            if (ss !=None):
                     under = ss.get(s[k])
              #ключ в подсловаре состояний; under - следующее
            #состояние       
            else:
                under = None 
   
            if (under == None): #если в состоянии нет ключа со значением
                #текущего символа, то заканчиваем цикл
                if (check):
                    T = True
                    MAX = maxi
                state = False
            elif (k == len(s)-1):
                
                for i in finish:                 
                    if (i == under[0]):
                        maxi = t+1
                        check = True
                        break
               
                if (check):
                    T = True
                    MAX = maxi
                state = False
            else: #иначе переходи в следующее состояние
                t = t + 1
                k = k + 1 #следующий символ
                for i in finish:                 
                    if (i == under[0]):     
                        maxi = t 
                        check = True #автомат конечен уже
                        break
            
                ss = matrix.get(under[0]) #берем состояние в которое перешли и его
                #следующие состояния (словарь след. состояний)
               
                
        return(T, MAX)
            
    
        


A = 'data.json'
s = "122234411f"
k = 0
MAX = 0
T = False
print (MaxString(A,s,k))


A = 'data2.json'
s = "qwer.wwww.i"
k = 0
MAX = 0
T = False
print (MaxString(A,s,k))

A = 'key.json'
s = "begin"
k = 0
MAX = 0
T = False
print (MaxString(A,s,k))



