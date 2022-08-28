def solution(phone_number):
    byul_number = len(phone_number) - 4
    byul = "*" * byul_number
    back_phone_number = phone_number[len(phone_number)-4:]
    result = byul + back_phone_number
    return result
x = solution("4444")
print(x)