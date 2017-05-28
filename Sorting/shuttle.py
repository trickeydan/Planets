# shuttle.py
# Trickeydan/PythonScience/Sorting
# D.Trickey 2017
#
# My implementation of shuttle sort.
# Ascending Order

print("Shuttle Sort - Ascending Order")

data = [33,36,64,23,61,87,2,5,234,65,3,56,34]

total_comp = 0
total_swap = 0

n = len(data)

for pass_number in range(1,n):

    print("Pass " + str(pass_number))
    swap = 0
    comp = 0
    for i in range(pass_number,0,-1):
        if(data[i] > data[i+1]):
            data[i], data[i+1] = data[i+1], data[i] #Swap positions
            swap += 1
        comp += 1
        print(data)

    total_comp += comp
    total_swap += swap
print("Total Comparisons: " + str(total_comp))
print("Total Swaps: " + str(total_swap))
