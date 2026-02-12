#Course: COMP 2113 
#Assignment 1, Question 1
#Author: Catherine Nixon
#Student ID: 0311174
#Email address: 0311174n@acadiau.ca
#Date: 2026 - 01 - 26
#I certify that this code is my own.
#I have not broken any rules concerning Academic Dishonesty.


#Insertion Sorting of numbers
def insertion_sort(numbers):
    comparisons =0
    swaps = 0
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i -1
        while j>=0 and numbers[j] > key:
            comparisons +=1
            numbers[j + 1] = numbers[j]
            j -= 1
            swaps += 1
        numbers[j + 1] = key
        swaps +=1
    return numbers, comparisons, swaps


# Selection Sort of numbers
def selection_sort(numbers):
    comparisons = 0
    swaps = 0
    for i in range(len(numbers)):
        smallest = i
        
        for j in range(i+1, len(numbers)):
            comparisons +=1
            if numbers[j] < numbers[smallest]:
                smallest =j
                
        if smallest != i:
            numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
            swaps +=1
            
    return numbers, comparisons, swaps




#Main program code
def sort_numbers():
    print("Sorting program")
    input_file = input("Enter a file name to read the numbers from: ")
    output_file = input("Enter a file name to save the sorted numbers: ")
    
    #Prompt the user to select a sorting method
    method = input("Choose a sorting method (1 for Selection sort, 2 for Insertion sort): ").strip()
    
    #Reading the munbers from the file
    with open(input_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        
    #Sorting the numbers using the choosen method
    if method == "1":
        print("You have selected selection Sort.")
        sorted_numbers, comparisons, swaps = selection_sort(numbers)
    elif method == "2":
        print("You've selected the Insertion sort.")
        sorted_numbers, comparisons, swaps = insertion_sort(numbers)
    else:
        print("Invalid option Please choose 1 or 2 for sorting.")
        return
    
    #Save the sorted number to the output file
    with open(output_file, 'w') as file:
        for number in sorted_numbers:
            file.write(f"{numbers}\n")
            
    #Displaying the sorting statistics
    print(f"Sorted numbers are saved to {output_file}")
    print(f"Number of comparisons: {comparisons}")
    print(f"Number of swaps: {swaps}")
    
if __name__ == "__main__":
    sort_numbers()