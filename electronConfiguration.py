n = int(input("electron configuration: "))
electron = ["--------    ", "1s2", ["2s2", "2p6"], ["3s2", "3p6"], ["4s2", "3d10", "4p6"], ["5s2", "4d10", "5p6"], ["6s2", "4f14", "5d10", "6p6"], ["7s2", "5f14", "6p10", "7p6"],"---"]
electron2 = ["----- ", "1s2", ["2s2", "2p6"], ["3s2", "3p6"], ["3d10", "4s2", "4p6"], ["4d10", "5s2","5p6"], ["4f14", "5d10", "6s2", "6p6"], ["5f14","6p10","7s2","7p6"]]
results_electron = []
loop = 0
def check(n):
    global loop
    totalnumber = [2, 8, 8, 18, 18, 32, 32]
    i = 0
    while n > totalnumber[i]:
        n -= totalnumber[i]
        i += 1
        loop += 1
    return(n)


def checkagain(n):
	global loop 
	if loop == 1:
		return ((electron[2][0],electron[2][1].replace("6",str(n-2))) if n > 2 else electron[2][0].replace("b2","b" + str(n)))
	if loop == 2:
		return ((electron[3][0],electron[3][1].replace("6",str(n-2))) if n > 2 else electron[3][0].replace("2", str(n)))
	if loop == 3:
		if n < 2:
			return (electron[4][0].replace("2", str(n)))
		if n < 12:
			return (electron[4][1].replace("10", str(n-2)),electron[4][0])
		return(electron[4][1],electron[4][0],electron[4][2].replace("6", str(n-12)))
	if loop == 4:
		if n < 2:
			return (electron[5][0].replace("2", str(n)))
		if n < 12:
			return (electron[5][1].replace("10", str(n-2)),electron[5][0])
		return ((electron[5][1],electron[5][0],electron[5][2].replace("6",str(n-12))))
	if loop == 5:
		if n < 2:
			return (electron[6][0].replace("2", str(n)))
		if n < 16:
			return (electron[6][1].replace("14", str(n-2)),electron[6][0])
		if n < 26:
			return (electron[6][1],electron[6][2].replace("10", str(n-16)),electron[6][1])
		return(electron[6][1],electron[6][2],electron[6][0],electron[6][3].replace("p6", "p"+str(n-26)))
	if loop == 6:
		if n < 2:
			return (electron[7][0].replace("2", str(n)))
		if n < 16:
			return (electron[7][1].replace("14", str(n-2)),electron[7][0])
		if n < 26:
			return (electron[7][1],electron[7][2].replace("10", str(n-16)),electron[7][0])
		return (electron[7][1], electron[7][2],electron[7][0],electron[7][3].replace("6",str(n-26)))


"""
Guide 

1s2
2s2 2p6
3s2 3p6 3d10
4s2 4p6 4p10 4f14
5s2 5p6 5d10 5f14
6s2 6p6 6d10
7s2 7p6

"""

d = check(n)

for i in range(0, loop+1):
	results_electron.append(electron2[i])

results_electron.pop(0)
c = " ".join(str(v) for v in results_electron)

print(c,checkagain(d))