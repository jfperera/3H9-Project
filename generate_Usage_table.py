import cPickle as pickle
usage_table = {}




sample_list = ['Y1-SP', 'Y2-SP', 'Y3-SP', 'Y4-SP', 'Y5-SP', 'O1-SP', 'O2-SP', 'O3-SP', 'O4-SP', 'O5-SP', 'Y1-THY', 'Y2-THY', 'Y3-THY', 'Y4-THY', 'Y5-THY', 'O1-THY', 'O2-THY', 'O3-THY', 'O4-THY', 'O5-THY','3H9NS1', '3H9NS2', '3H9NS3', '3H9SW1', '3H9SW2', '3H9SW3']


directory = '/Users/haochuhuang/Documents/Jason Perera/3H9 BCR HTS Sequencing/compile IMGT Summary/'



def add_usage(file1, i, dict1):
    '''file open for reading + the index of that item in the list, and usage dict -> none
    takes an IMGT file open for reading, and adds the unique TCR usage data to the dictionary at the index given'''
    
    file1.readline()                               #header
    for line in file1:                                      
        a = line.split('\t')
        if a[2] == 'productive':
            V = a[3].split()[1].split('*')[0]
            J = a[9].split()[1].split('*')[0]
            CDR3 = a[20]
            count = int(a[1].split('-')[1])
            if (V,J,CDR3) in dict1:
                dict1[(V,J,CDR3)][i] += count
            else:
                dict1[(V,J,CDR3)] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
                dict1[(V,J,CDR3)][i] += count           
    file1.close()            

def add_usage2(file1, i, dict1):
    '''file open for reading + the index of that item in the list, and usage dict -> none
    takes an IMGT file open for reading, and adds the unique TCR usage data to the dictionary at the index given'''
    
    file1.readline()                               #header
    for line in file1:                                      
        a = line.split('\t')
        if a[2] == 'productive':
            V = a[3].split()[1].split('*')[0]
            J = a[7].split()[1].split('*')[0]
            CDR3 = a[18]
            count = int(a[1].split('-')[1])
            if (V,J,CDR3) in dict1:
                dict1[(V,J,CDR3)][i] += count
            else:
                dict1[(V,J,CDR3)] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  
                dict1[(V,J,CDR3)][i] += count           
    file1.close() 

def make_table(list1, dict1):
    ''' list of sample names, dict to add usage to-->none
        takes a list of samples which point to IMGT files and appends their
        usage to a dictionary where each key is a tuple of V, J, CDR3'''
    for i in range(len(list1)):
        name = directory + sample_list[i] + '.txt'
        file1 = open(name, 'r')
        if i < 20:
            add_usage(file1, i, dict1)
        if i >= 20:
            add_usage2(file1, i, dict1)
        print list1[i] + ' is complete'




make_table(sample_list, usage_table)

#TO WRITE TO TXT FILE
header = ['V-gene', 'J-gene', 'CDR3', 'Y1-SP', 'Y2-SP', 'Y3-SP', 'Y4-SP', 'Y5-SP', 'O1-SP', 'O2-SP', 'O3-SP', 'O4-SP', 'O5-SP', 'Y1-THY', 'Y2-THY', 'Y3-THY', 'Y4-THY', 'Y5-THY', 'O1-THY', 'O2-THY', 'O3-THY', 'O4-THY', 'O5-THY','3H9NS1', '3H9NS2', '3H9NS3', '3H9SW1', '3H9SW2', '3H9SW3']
a= usage_table.keys()
a.sort()

name = '/Users/haochuhuang/Documents/Jason Perera/3H9 BCR HTS Sequencing/Prism and Excel/3H9_table.pkl'
file1 = open(name, 'w')


pickle.dump(usage_table, file1)
file1.close()
print "Pickled!"


name = '/Users/haochuhuang/Documents/Jason Perera/3H9 BCR HTS Sequencing/Prism and Excel/3H9_table.txt'
file1 = open(name, 'w')


for item in header:
    file1.write(item + '\t')
file1.write('\n')

for i in range(len(a)):
    for item in a[i]:
        file1.write(item + '\t')
    for item in usage_table[a[i]]:
        file1.write(str(item) + '\t')
    file1.write('\n')

file1.close()
                 

