from datetime import datetime,timedelta

def solution(D):
	if len(D) == 2:
		list = []
		for key in D.keys():
			list.append(datetime.strptime(key, '%Y-%m-%d').date())

		date = list[1] - list[0]
		value = D[str(list[1])] - D[str(list[0])]
		inc = value/date.days

		min = D[str(list[0])]

		for n in range(date.days-1):
			min = min + inc
			D[str(list[0] + timedelta(n+1))] = min
			

	elif len(D) > 2:
		list = []
		for key in D.keys():
			list.append(datetime.strptime(key, '%Y-%m-%d').date())

		diff = []
		for i in range(len(list)-1):
			date = list[i+1]-list[i]
			if date.days > 1:
				value = D[str(list[i+1])] - D[str(list[i])]
				inc = value/date.days

				min = D[str(list[i])]
				for n in range(date.days-1):
					min = min + inc
					D[str(list[i] + timedelta(n+1))] = min


	return D

D = {'2019-01-01':100,'2019-01-04':115}
E = {'2019-01-10':10,'2019-01-11':20,'2019-01-13':10}
solution(E)
print(E)