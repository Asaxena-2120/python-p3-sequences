#!/usr/bin/env python3

def print_fibonacci(length):
    answer=[]
    if length>0:
        answer.append(0)
        
        if length >1:
            answer.append(1)
        
       
            if length>2:
                
        
        
                
        
                for i in range(2,length):
                    answer.append(answer[i-1]+answer[i-2])
                    

    print(answer)


  