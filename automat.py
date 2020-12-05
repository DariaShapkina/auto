from collections import *
import json
from pprint import pprint

class Automat:
    def __init__(self, filename):
         with open(filename, 'r', encoding='utf-8') as fh:
            data = json.load(fh)

         self.start = data[0]['start'][0]
         self.finish = data[0]['finish']
         self.matrix = data[0]['matrix']
         self.state = [False,0]
         if (data[0].get('priority') != None):
             self.priority = data[0]['priority'][0]
         else:self.priority =0
         if (data[0].get('name') != None):
             self.name = data[0]['name']
         else:self.name =""

         
    def typing(self,c):
        typing = ''
        if (c == '\\n' or c == '\\r' or c == '\\t' or c == " "):
            typing = 'whitespace'
        elif (c >= '0' and c <= '9'):
            typing = 'digit'
        elif ((c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')):
            typing = 'letter'
        elif (c == '.'):
            typing = 'point'
        elif ("+-=^/<>%^*".find(c) != -1):
            typing = 'oper'
        return typing

    
    def maxString(self, s, skip):
        self.state = [False,0]
        k = skip
        under = 0
        ss = self.matrix.get(self.start)
        while(k < len(s)):
                under = ss.get(s[k])
                if (under == None):
                    under = ss.get(self.typing(s[k]))
                if (under != None):
                    k = k+1
                    for i in self.finish:
                        if (i == under[0]):self.state = [True,k]                
                    ss = self.matrix.get(under[0])
                    if (ss == None): break           
                else: break              
        return self.state

    
    def __lt__(self, other):
        return self.priority < other.priority
    def __le__(self, other):
         return self.priority <= other.priority
    def __gt__(self, other):
        return other.priority < self.priority
    def __ge__(self, other):
        return other.priority <= self.priority
    def __cmp__(self, other):
            return self.priority == other.priority

class Lexer:
     def __init__(self, automats):
         self.automats = sorted(automats)
         #for i in self.automats:
          #   print(i.name)
         self.tok = []


     def tokens(self,s):
         index = 0
         while (index < len(s)):
             for i in self.automats:       
                 check = i.maxString(s[index:],0)
                 if (check[0]):
                     x = Token(i.name[0], s[index:index+check[1]])
                     self.tok.append(x)
                     index = index + check[1]
                     break
         return self.tok        
                    
            
class Token:
  def __init__(self, classname, token):
      self.classname = classname
      self.token = token
    
  def __str__(self):
    return '({}, {})'.format(self.classname, self.token)             



test1 = Automat('data.json')
print(test1.maxString("w1221ggg34411f",0))


test1 = Automat('data2.json')
print(test1.maxString("qwer.wwww.i",0))

test1 = Automat('key.json')
print(test1.maxString("begin1",0))

test = Automat('white.json')
print(test.maxString("  122.2begin1",0))

#####################

test = Lexer([Automat("id.json"), Automat('operation.json'),
                        Automat('double.json'),Automat('integer.json'),
                        Automat('bool.json'),Automat('key.json'),
                        Automat("white.json")])

for i in test.tokens("begin  if 3 - 1.88888/8 == True"):
    print(i)
