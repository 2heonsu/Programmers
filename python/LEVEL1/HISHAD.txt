def solution(x):
    ## 이렇게 풀어도 되려나... 
    strX=str(x) #1.입력 정수 일단 문자열로
    for i in range(len(strX)): #2.자리수만큼 돌려
        total+=int(strX[i]) #3.문자열 자리마다 int 바꿔서 total에 sum
    answer = (True if (x%total==0) else False) #4.x가 total로 나누어 떨어지면 T 아니면 F  
    return answer