def solution(n):
    listNum=[]
    strNum='' #필요 변수 초기화
    strNum=str(n) #문자열로만들고
    listNum=list(strNum) #리스트함수사용하기위해 리스트로 변환
    listNum.sort() #오름차순정렬
    listNum.reverse() #리스트 뒤집기
    strNum='' #위 과정 역으로
    for i in listNum:
        strNum+=i
    return int(strNum)