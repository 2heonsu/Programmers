def solution(x, n):
    answer = []
    ##할말없음 그냥 1~n 까지 반복 돌리구 i 만큼 곱해서 리스트에 어펜드
    for i in range(1,n+1):
        answer.append(x*i)
    return answer