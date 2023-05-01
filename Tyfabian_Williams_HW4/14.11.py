#Tyfabian Williams
#2142655

def selection_sort_descend_trace(arrays):
    for i in range(len(arrays) - 1):
        t = i
        for j in range(i + 1, len(arrays)):
            if arrays[t] < arrays[j]:
                t = j
        arrays[i], arrays[t] = arrays[t], arrays[i]
        for value in arrays:
            print(value, end=" ")
        print()
    return arrays

if __name__ == "__main__":

    array = [int(x) for x in input("").split()]
    selection_sort_descend_trace(array)
