alcohol = input('請問你有喝過酒嗎？')
age = input('請問今年你幾歲？')
age = int(age)
if alcohol == '有':
	if age >= 18:
		print('你喜歡喝哪一種酒？')
	else:
		print('為甚麼可以喝酒？你還未成年誒')
elif alcohol == '沒有':
	if age >= 18:
		print('怎麼還沒有喝過呢？')
	else:
		print('記得未成年請勿飲酒喔')
else:
	print('請輸入有或沒有')

