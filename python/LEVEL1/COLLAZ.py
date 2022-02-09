def solution(num):
    answer = 0
    for i in range(500): #횟수 500제한
        if num==1: #num 1 이면 리턴
            return answer
        num=(num/2 if num%2==0 else num*3+1) #이건 홀수 짝수 판별해서 나누거나 곱하는거
        answer+=1
    return -1