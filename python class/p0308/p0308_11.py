#strip() 공백제거
ss='apple은 당도가 높고, apple의 색상은 빨강, 녹색이 있습니다'
s1 = '    파이         썬     '
s2 = '파이썬'

#빈공백 제거
print(s1.lstrip()) #왼쪽 공백만 제거
print(s2.rstrip()) #오른쪽 공백만 제거
print(s1.strip()) # 왼쪽, 오른쪽 공백 모두 제거
# s_input = input('지금 현재 배우고 있는 과목을 입력하세요 >> ').strip()
# if s_input == s2:
#      print('정답입니다.')
# else:
#      print('오답입니다')
# if s1.lstrip() == s2:
     # print('같습니다')
# else:
     # print('다릅니다')
     
# replace - 문자열을 다른 문자열로 대체
print(s1.replace('파','자'))
print(ss.replace('apple','사과'))
print(s1.replace(' ',''))

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다. \
     2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. \
     지난해 이마트 창립 이후 적자를 기록했고, 신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서\
     위기 극복을 위한 새로운 리더십을 내세웠다."
     
print(news.replace(' ',''))
# 그룹 ->group
print(news.replace('그룹','group')) # news에 반영이 안됨 출력만. 비파괴형태 변하지 않음

