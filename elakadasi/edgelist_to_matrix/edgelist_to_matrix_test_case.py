# https://stackoverflow.com/questions/19151734/python-convert-edge-list-to-adjacency-matrix
import csv

# read original edge list with tags, convert them to a list of tuples to meet input criteria of the matrix creator
with open('halo_tag_edgelist_to_test.csv') as f:
    next(f) # Skip header
    mycsv = csv.reader(f, delimiter = "\t")
    tuple_list = []
    tags_list = []
    for row in mycsv:
        for tag in row:
            if "0" in tag: # remove weight values from tags
                pass
            else:
                if tag not in tags_list:
                    tags_list.append(tag)
                else:
                    pass
        tuple_list.append(tuple(row))
    data = tuple_list

# reindexing of tags
mydict = dict()
counter = 0
for t in tags_list:
    mydict[counter] = t
    counter += 1

data_copy = data # just in case

# replace word tags to numbers, ie reindexing
new_data = []
temp_tuple = tuple()

for i,j,k in data_copy:
    if i in mydict.values():
        number = mydict.keys()[mydict.values().index(i)]
        temp_tuple += (number,)
    else:
        pass
    if j in mydict.values():
        number = mydict.keys()[mydict.values().index(i)]
        temp_tuple += (number,)
    else:
        pass
    temp_tuple += (k,)
    new_data.append(temp_tuple)
    temp_tuple = tuple()

"""
# check dictionary 
lst = list()
for key, val in mydict.items():
    lst.append( (val, key) )

for key, val in lst:
    print key, val
    # word: index number
"""
# creating the matrix

n = max(max(vertex0, vertex1) for vertex0, vertex1, weight in new_data) # Get size of matrix
matrix = [[0] * n for i in range(n)]

for vertex0, vertex1, weight in new_data:
    print vertex0, vertex1, weight    
    matrix[vertex0-1][vertex1-1] = weight

print(matrix) # :(

"""
outF = open("my_matrix.txt", "w")
for row in matrix:
    outF.write("%s," % row) # this was working
    outF.write("\n")

outF.close()


"""
