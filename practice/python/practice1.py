def string_input():
    return input()

def string_print(first_str, second_str):
    return first_str + ' ' + second_str

def float_input():
    return input().split()

def float_sub(first_float, second_float):
    first_float = float(first_float)
    second_float = float(second_float)
    if second_float > first_float:
        return second_float - first_float
    return first_float - second_float

# 문자열 입력
print("첫번째 문자열을 입력하시오 : ", end='')
first_str = string_input()
print("두번째 문자열을 입력하시오 : ", end='')
second_str = string_input()

# 문자열 합쳐서 출력
conc_str = string_print(first_str, second_str)
print("합쳐진 문자열 : " + conc_str)

# 실수 2개 입력
print("실수 2개를 입력하시오 : ", end='')
first_float, second_float = float_input()

# 실수의 차 출력
print("두 실수의 차 : %f" % float_sub(first_float, second_float))