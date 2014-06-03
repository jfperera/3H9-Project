loc = '/Users/haochuhuang/Documents/Jason Perera/3H9 BCR HTS Sequencing/Prism and Excel/IMGT_combined.txt'
file1 = open(loc, 'r')

file1.readline()
l = []
for line in file1:
    e = (line.strip()).split('\t')
    for i in range(3, 23):
        e[i] = int(e[i])
    YS = sum(e[3:8])
    YT = sum(e[8:13])
    OS = sum(e[13:18])
    OT = sum(e[18:23])
    total = sum(e[3:23])
    e = e + [YS, YT, OS, OT, total]
    l.append(tuple(e))    

file1.close()
print(len(l))


def search(V, J, CDR3):
    return_list = []
    for item in l:
	if item[0] == V and item[1] == J and item[2] == CDR3:
            return_list.append(item)
    return return_list        
		
