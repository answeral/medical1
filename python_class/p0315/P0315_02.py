import random
def idpw():
    eng = "abcdefghijklmnopqrstuvwxyz"
    pw = "1234567890"
    member = [['aaa','1111']]
    for i in range(10):
        temp1 = random.choice(eng)
        temp2 = random.choice(eng)
        temp3 = random.choice(eng)
        tt1 = temp1+temp2+temp3
        temp4 = random.choice(pw)
        temp5 = random.choice(pw)
        temp6 = random.choice(pw)
        temp7 = random.choice(pw)
        tt2 = temp4+temp5+temp6+temp7
        
        member.append([tt1,tt2])
    return member

# p_list = []    
# for i in range(10):
#      temp1 = random.choice(eng,k=3)
#      temp2 = random.choice(eng,k=3)
#      temp3 = random.choice(eng,k=3)    
#      temp4 = random.choice(eng,k=3)  
#      p_list.append(temp1+temp2+temp3+temp4)
# print(p_list)



# 4자리 패스워드를 10개 생성해서 p_list에 추가  
# p_list = []
# for i in range(10):
#      p = random.randint(1000,9999)
#      p_list.append(p)
# print(p_list)   