#Merge_sort
def mergesort(a):
	
	if len(a) == 1:
		return a
		
	
	mid = len(a)//2
	lef = a[:mid]
	rig = a[mid:]
	l1 = mergesort(lef)
	r1 = mergesort(rig)
	
	
	return Merge(l1,r1)


def Merge(lef,rig):
	result = []
	while len(lef) > 0 and len(rig) > 0:
		if lef[0] <= rig[0]:
			result.append(lef.pop(0))
		else:
			result.append(rig.pop(0))
	result += lef
	result += rig
	return result

lis = [80, 53, 62, 3, 120, 185, 72, 49, 79, 15, 27]

f = mergesort(lis)
print(f)

