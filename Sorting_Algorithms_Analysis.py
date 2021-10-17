#Project 1
#Name: Lavanya Velagala
#UTA ID: 1001908911

import random
from time import perf_counter
import matplotlib.pyplot as plt

#implementation of merge sort
def merge(left, right):
    a = []
    l_index = r_index = 0
    left_len, right_len = len(left), len(right)
    for _ in range(left_len + right_len):
        if l_index < left_len and r_index < right_len:
            # check from the start of each array for which value is smaller
            # If the item at the beginning of the left array is smaller, add it to the sorted array
            if left[l_index] <= right[r_index]:
                a.append(left[l_index])
                l_index = l_index + 1
            # If the item at the beginning of the right array is smaller, add it to the sorted array
            else:
                a.append(right[r_index])
                r_index = r_index + 1
        # If we've reached the end of the of the left array, add the elements from the right array
        elif l_index == left_len:
            a.append(right[r_index])
            r_index = r_index + 1
        # If we've reached the end of the of the right array, add the elements from the left array
        elif r_index == right_len:
            a.append(left[l_index])
            l_index = l_index + 1
    return a

def merge_sort(number):
    # If the array has a single element, return it
    n = len(number)
    if n <= 1:
        return number
    # Use floor division to get midpoint, indices must be integers
    mid = n // 2
    # Sort and merge each half
    left = merge_sort(number[:mid])
    right = merge_sort(number[mid:])
    # Merge the sorted arrays into a new one
    return merge(left, right)
    
#implementation of heap sort
def heapify(items, size_heap, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    lc = (2 * root_index) + 1
    rc = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if lc < size_heap and items[lc] > items[largest]:
        largest = lc

    # Do the same for the right child of the root
    if rc < size_heap and items[rc] > items[largest]:
        largest = rc

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        items[root_index], items[largest] = items[largest], items[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(items, size_heap, largest)

def heap_sort(items):
    n = len(items)
    # Create a Max Heap
    # The 2nd argument of range means we stop at the element before -1 i.e. the first element of the array
    # The 3rd argument of range means we iterate backwards, reducing the count of i by 1
    for i in range(n, -1, -1):
        heapify(items, n, i)
    for i in range(n - 1, 0, -1):
        items[i], items[0] = items[0], items[i]
        heapify(items, i, 0)
    print("Items after sorting using Heap Sort : ", items)
    
#implementation of quick sort 
def quick_sort(a, start , stop):
    if(start < stop):
        pivotindex = partition_random(a, start, stop)
        # The array is partially sorted around the pivot because we are separately sorting the left and the right halves of the array.
        quick_sort(a, start , pivotindex - 1)
        quick_sort(a, pivotindex + 1, stop)
 
# This function generates random pivot, swaps the first element with the pivot and calls the partition function.
def partition_random(a , start, stop):
    # Generating a random number between the starting index of the array and the ending index of the array.
    random_pivot = random.randrange(start, stop)
    # Swapping the starting element of the array and the pivot
    a[start], a[random_pivot] = a[random_pivot], a[start]
    return partition(a, start, stop)
 
def partition(a,start,stop):
    pivot = start 
    i = start + 1
    for j in range(start + 1, stop + 1):   
        # if the current element is smaller or equal to pivot, move it to the left side of the partition.
        if a[j] <= a[pivot]:
            a[i] , a[j] = a[j] , a[i]
            i = i + 1
    a[pivot] , a[i - 1] = a[i - 1] , a[pivot]
    pivot = i - 1
    return (pivot)

#implementation of quick sort using 3 medians
#function to find the median     
def median(a, i, j, k):
  if a[i] < a[j]:
    return i if a[k] < a[i] else k if a[k] < a[j] else j
  else:
    return j if a[k] < a[j] else k if a[k] < a[i] else i

def quick_sort_main(a):
    quick_sort_intermediate(a,0,len(a)-1)
    print("Items after sorting using Quick Sort 3 Medians : ", items)

#This function is an intermediate function between main function and quick sort algorithm.
def quick_sort_intermediate(a,first,last):
    if first < last:
        split = partition_median(a,first,last)
        quick_sort_intermediate(a,first,split-1)
        quick_sort_intermediate(a,split+1,last)

#This function helps to find the position of the pivot in the input array and arranges
#all the elements less than pivot to its left and all the elements greater than pivot to its right.
def partition_median(a,first,last):
    pivot = median(a, first, last, (first + last) // 2)
    a[first], a[pivot] = a[pivot], a[first]
    pivot_val = a[first]
    right = last
    left = first + 1
    done = False
    while not done:
       while left <= right and a[left] <= pivot_val:
           left = left + 1
       while a[right] >= pivot_val and right >= left:
           right = right -1
       if right < left:
           done = True
       else:
           temp = a[left]
           a[left] = a[right]
           a[right] = temp
    temp = a[first]
    a[first] = a[right]
    a[right] = temp
    return right

#implementation of insertion sort       
def insertion_sort(items):
    n = len(items)
    # Start on the second element as we assume the first element is sorted
    for i in range(1, n):
        insert_item = items[i]
        # reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than the item to insert
        while j >= 0 and items[j] > insert_item:
            items[j + 1] = items[j]
            j = j - 1
        # Insert the item
        items[j + 1] = insert_item
    print("Items after sorting using Insertion Sort : ", items)

#implementation of selection sort
def selection_sort(items):
    # This value of i corresponds to how many values were sorted
    n = len(items)
    for i in range(n):
        # We assume that the first item of the unsorted segment is the smallest
        l_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, n):
            if items[j] < items[l_index]:
                l_index = j
        # Swap values of the lowest unsorted element with the first unsorted element
        items[i], items[l_index] = items[l_index], items[i]
    print("Items after sorting using Selection Sort : ", items)
    
#implementation of bubble sort
def bubble_sort(items):
    n = len(items)
    # Traverse through all the elements
    for i in range(n-1):
        # traverse elements from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap elements if the element found is greater than the next element
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]
    print("Items after sorting using Bubble Sort : ", items)


#array used in sorting all the items
items = []
choice = int(input("Enter the mode of input data : \n 1. Manual Mode \n 2. Random Mode \n "))
number = int(input("Enter the Total Number of Elements : "))
#checks if the entered number is greater than 0
if number <= 0:
    print("Enter a number which is greater than 0\n")
else:
    #condition for manual input
    if choice == 1:
        for i in range(number):
            value = int(input("Please enter the items of the array index %d : " %i))
            items.append(value)
    #condition for random input
    elif choice == 2:
        for i in range(number):
            value = random.randint(1,number)
            items.append(value)
print("\n 1. Merge Sort \n 2. Heap Sort \n 3. Quick Sort \n 4. Quick Sort using 3 Median \n 5. Insertion Sort \n 6. Selection Sort \n 7. Bubble Sort\n")
alg_list = []
#dictionary to assign each number to a particular algorithm
alg_list_defn = {1:"Merge Sort", 2:"Heap Sort", 3:"Quick Sort", 4:"Quick using 3 Median Sort", 5:"Insertion Sort", 6:"Selection Sort", 7:"Bubble sort"}
time_taken_list = []
#to select a user given algorithm
while(True):
    try:
        alg_selection = int(input("Select an algorithm\n"))
        if alg_selection >= 1 and alg_selection <= 7:
            alg_list.append(alg_selection)
        else:
            print("Enter an integer within the range of 1 to 7\n")
            continue
    except:
        #prompts user to select an integer which is within the range of 1 to 7 only
        print("Enter an integer within the range of 1 to 7\n")
        continue
    #to make sure user enters either y or n
    while(True):
        yes_no = input("Do you want to continue (y/n):")
        if yes_no == 'n':
            break
        elif yes_no == 'y':
            break
        #prompts user to enter either y or n of the user enters any random input
        else:
            print("Enter a valid input y or n")
    if yes_no == 'n':
        break 
for alg_choice in alg_list:
    if alg_choice == 1:
        merge_start = perf_counter() 
        items = merge_sort(items)
        print("Items after sorting using Merge Sort : ", items)
        merge_stop = perf_counter() 
        print("Time taken for Merge Sort:", merge_stop - merge_start)
        time_taken_list.append(merge_stop - merge_start)
        
    elif alg_choice == 2:
        heap_start = perf_counter() 
        heap_sort(items)
        heap_stop = perf_counter() 
        print("Time taken for Heap Sort:", heap_stop - heap_start)
        time_taken_list.append(heap_stop - heap_start)
        
    elif alg_choice == 3:
        quick_start = perf_counter() 
        quick_sort(items, 0, len(items) - 1)
        print("Items after sorting using Quick Sort random element as pivot: ", items)
        quick_stop = perf_counter()
        print("Time taken for Quick Sort:", quick_stop - quick_start)
        time_taken_list.append(quick_stop - quick_start)
            
    elif alg_choice == 4:
        quick_median_start = perf_counter() 
        quick_sort_main(items)
        quick_median_stop = perf_counter()
        print("Time taken for Quick Sort 3 Medians:", quick_median_stop - quick_median_start)
        time_taken_list.append(quick_median_stop - quick_median_start)
            
    elif alg_choice == 5:
        insertion_start = perf_counter() 
        insertion_sort(items)
        insertion_stop = perf_counter()
        print("Time taken for Insertion Sort:", insertion_stop - insertion_start)
        time_taken_list.append(insertion_stop - insertion_start)
            
    elif alg_choice == 6:
        selection_start = perf_counter() 
        selection_sort(items)
        selection_stop = perf_counter()
        print("Time taken for Selection Sort:", selection_stop - selection_start)
        time_taken_list.append(selection_stop - selection_start)
            
    else:
        bubble_start = perf_counter() 
        bubble_sort(items)
        bubble_stop = perf_counter()
        print("Time taken for Bubble Sort:", bubble_stop - bubble_start)
        time_taken_list.append(bubble_stop - bubble_start)
x = []   
for i in alg_list:
    x.append(alg_list_defn[i])
#plots graph between x which is the user selected algorithm and y which is the time taken for the given algorithm
plt.plot(x,time_taken_list)
# naming the x axis
plt.xlabel('Sorting Algorithms')
# naming the y axis
plt.ylabel('Time Taken to run for the given user input')
plt.title('Comparison of Sorting Algorithms')
#to display the graph
plt.show()
