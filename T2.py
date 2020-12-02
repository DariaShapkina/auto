from collections import *
import json
from pprint import pprint

global MAX , T 


h = OrderedDict() #подкласс словаря у которого можно изменять порядок элементов

h = dict(zip(['1', '2', '3','4', '5', '6', '7' ],
                       ["white.json", 'operation.json',
                        'double.json','integer.json',
                        'bool.json','key.json','id.json']))


h2 = dict(zip(['1', '2', '3','4', '5', '6', '7' ],
                       ['пробел', 'операция',
                        'тип double',' тип integer',
                        'bool','ключевое слово','id']))


def automaton(A,s,k,pr):
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
        
        if (pr != '5' and pr != '6' ):
            while (state == True and k < len(s)):
                typing = ''
                if (s[k] == '\\n' or s[k] == '\\r' or s[k] == '\\t' or s[k] == " "):
                    typing = 'whitespace'
                elif (s[k] >= '0' and s[k] <= '9'):
                    typing = 'digit'
                elif ((s[k] >= 'a' and s[k] <= 'z') or (s[k] >= 'A' and s[k] <= 'Z')):
                    typing = 'letter'
                elif (s[k] == '.'):
                    typing = 'point'
                elif ("+-=^/<>%^*".find(s[k]) != -1):
                    typing = 'oper'
                    
                         
                under = ss.get(typing) #ключ в подсловаре состояний; under - следующее
                #состояние
               
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
        else:
             
             while (state == True and k < len(s)):
                 if (ss !=None):
                     under = ss.get(s[k])
                     
                 else:
                     under = None
                 if (under == None ): #если в состоянии нет ключа со значением
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

                
       
                
       

def automaton_running(s):
    global MAX, T
    MAX = 0
    T = 0
    index = 0
    str1 = ""
    while (index < len(s)):
        MAX = 0
        T = 0
        i = 0
        str1 = s[index:]
    
        for n,t in h.items():
            
            k = automaton(t,str1,0,n)
            i = i + 1

            if (k[0] == True):
                print(s[index:index+k[1]]," это ", h2.get(n))
                index = index + k[1]
                break
            if (i == len(h)):
                index = index + 1
                
    return()
        
    
    

s = "dfr22  = 3 + 8"
automaton_running(s)
s2 = "begin if 3 - 1.8888 == True"
automaton_running(s2)

