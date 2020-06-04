from datetime import datetime,timedelta

def solution(D):
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
