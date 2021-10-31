# 카이사르(시저) 암호

plaintext = input('영어 대문자로만 되어 있는 원문을 입력하세요: ')
key = int(input('키로 쓸 수를 입력하세요: '))
result = ''

for j in plaintext:
    if j.isalpha():
        alpha_code = ord(j) - ord('A')
        changed_alpha_code = (alpha_code + key) % 26 + ord('A')
        result += chr(changed_alpha_code)
    else:
        result += j

print(result)
