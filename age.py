drive = input('請問你有沒有開過車？')
if drive != 'yes' and drive != 'no': 
	print('只能輸入 yes or no')
	raise SystemExit # 系統直接離開,不去問年齡

age = input ('請問你幾歲?')
age = int(age)

if drive == 'yes':
	if age >= 18:
		print('你通過驗證了！')
	else:
		print('why?')
elif drive == 'no':
	if age >= 18:
		print('to get a diver license')
	else:
		print('Wait to 18 and get a diver license')
else:
	print('只能輸入 yes or no')