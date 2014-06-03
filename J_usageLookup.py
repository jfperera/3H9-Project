import cPickle as pickle
name = '/Users/haochuhuang/Documents/Jason Perera/3H9 BCR HTS Sequencing/Prism and Excel/3H9_table.pkl'
file1 = open(name, 'r')
d = pickle.load(file1)
e = d.keys()
e.sort()

b = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for item in e:
	if item[0][:4] == 'IGKV':
		J = int(item[1][4]) - 1
		for i in range(26):
			b[i][J] += d[item][i]

name2 = '/Users/haochuhuang/Documents/Jason Perera/3H9 BCR HTS Sequencing/Prism and Excel/AllJusage.txt'
file1 = open(name2, 'w')
for i in range(26):
	for item in b[i]:
		file1.write(str(item) +' \t')
	file1.write('\n')
file1.close()
