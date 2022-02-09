def solution(phone_number):
    ##음 복잡해이지만 그냥 문자열 곱 연산 + 슬라이싱
    return '*'*(len(phone_number)-4) + phone_number[len(phone_number)-4:len(phone_number)]