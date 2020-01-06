print('대학원생의 시급은 과연 얼마일까?')
hr=input('당신은 하루에 평균 몇시간 일하나요?')
hrr=int(hr)
if hrr==0:
    print('0을 입력하였으므로 뒤에 오류가 날것입니다. ㅎ_ㅎ 절대 코딩이 귀찮아서가 아닙니다.')
else:
    print('다음의 지시를 따라주세요.')
    
pay_month=input('당신의 월급은 얼마입니까? (단위: 만원)')
payy_month=int(pay_month)
pay_hour=(payy_month*10000)/(hrr*20)
if pay_hour<1000.0:
    print('당신은 개미와 같은 시급을 받습니다.')
elif 1000.0<pay_hour<5000.0:
    print('당신은 군인입니까??!??')
elif 5000.0<pay_hour<10000.0:
    print('당신은 평범한 대학원생입니다. 화이팅!')
else:
    print('Wow!! Burupda!!!')
