# 사이트별로 비밀번호를 만들어 주는 프로그램을 만드시오

# 예)http://naver.com 
# rule 1 : http:// 부분은 제외함 -> naver.com 
# rule 2 : 처음 만나는 점(.) 이후 부분은 제외함 -> naver 
# rule 3 : 비밀번호는 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com" 
url = "http://daum.net" 
url = "http://google.com" 
url = "http://youtube.com" 
my_rule = url.replace("http://", "") # rule no.1
print(my_rule)

my_rule = my_rule[:my_rule.index(".")] # rule no.2
print(my_rule)

password = my_rule[:3] + str(len(my_rule)) + str(my_rule.count("e")) + "!" # rule no.3

print("{0}의 비밀번호는 {1} 입니다. ". format(url, password)) # example