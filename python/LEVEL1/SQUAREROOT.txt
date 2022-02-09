def solution(n):#그냥 수학문제인듯?

    if n ==1:
        return 4
    
    for i in range(2,n+1):
        if n/i== i :
            return (i+1)*(i+1) 
        
    return -1