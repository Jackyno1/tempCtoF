#攝氏華氏轉換
temp = input('你輸入的是攝氏或華氏:')
if temp == '攝氏':
	c = input('輸入攝氏溫度:')
	c = float(c)
	print('轉換成華氏溫度為', c*9/5+32)

if temp == '華氏':
	f = input('輸入華氏溫度:')
	f = float(f)
	print('轉換成攝氏溫度為', (f-32)/9*5)