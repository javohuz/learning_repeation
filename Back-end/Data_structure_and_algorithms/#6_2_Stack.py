"""
Created on Tue Jul 18 11:54:27 2023

the stack  
it has creates without any help only with mission 

@author: User rashidovj
"""

class Stack:
    
    def __init__(self,*info):
        self.info = [a for a in info]
    
    def add_info(self ,*info):
        return [stack for stack in self.info]

    def get_info(self):
        return self.info
    
    def isEmpty(self):
        return len(self.info)==0

    def __repr__(self):
        return f"{self.info}"
    
    def __getitem__(self,index):
        return self.info[index]

    def __setitem__(self,index,value):
        self.info[index] = value
        
    def __call__(self):
        return self.info
    
    def pop_info(self):
        if len(self.info)==0 :
            return 'Stack is empty'
        else :
            return self.info.pop()
    
    def peek_info(self):
        if len(self.info)==0 :
            return 'Stack is empty'
        else :
            return self.info[-1]
    
sms_box = Stack()
last_one=sms_box.pop_info()
last_one=sms_box.peek_info()


print(type(sms_box()),last_one)
sms_box()




















