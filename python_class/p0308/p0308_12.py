#split() #문자열 분리
hobby ='게임,골프,독서'

#리스트 타입 3개로 분리
print(hobby.split(','))


h_data = '2023-10-23,1,강원도 강릉시,강릉동인병원,383,21,033)651-6167,강릉대로419번길 42,종합'
print(h_data.split(','))
h_list = h_data.split(',')
print('병상수 :',h_list[4])

a_data='2023-10-23/577/충남 금산군/금산365의원/25/7/041)754-9365/금산읍 후곤천길 56/의원'
a_list = a_data.split('/')
print('병상수:',a_list[4])

#join
ss = '%'
print(ss.join('파이썬'))

s_data ='2023/03/08'
s_date_list = s_data.split('/')
print(s_date_list)
s_time = '2023:03:08:16:48:00'
s_time_list = s_time.split(':')
print(s_time_list)


today = '2024/03/08'
#10년 후 날짜를 출력해라 2034/03/18
today_list = today.split('/')
print(today_list)
today_list[0]=int(today_list[0])+10
# today2 = '{}/{}?{}'.format(today_list[0],today_list[1],today_list[2])
today2 = '{}/{}?{}'.format(*today_list)
print(today2)








