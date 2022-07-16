print("Question 1")

# import all functions/classes from the tkinter
from tkinter import *

# Function for finding GST rate
def findGst() :

	# take a value from the respective entry boxes
	# get method returns current text as string
	org_cost= int(org_priceField.get())
	
	N_price = int(net_priceField.get())

	# calculate GST rate
	gst_rate = ((N_price - org_cost) * 100) / org_cost;

	# insert method inserting the
	# value in the text entry box.
	gst_rateField.insert(10, str(gst_rate) + " % ")
	
	
# Function for clearing the
# contents of all text entry boxes
def clearAll():
	
	
	# deleting the content from the entry box
	org_priceField.delete(0, END)
	
	net_priceField.delete(0, END)
	
	gst_rateField.delete(0, END)
	

# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()
	
	# Set the background colour of GUI window
	gui.configure(background = "light green")
	
	# set the name of tkinter GUI window
	gui.title("GST Rate Finder")
	
	# Set the configuration of GUI window
	gui.geometry("300x300")

	# Create a Original Price: label
	org_price = Label(gui, text = "Original Price",
					bg = "blue")
	
	# Create a Net Price : label
	net_price = Label(gui, text = "Net Price",
					bg = "blue")

	# Create a Find Button and attached to
	# findGst function
	find = Button(gui, text = "Find", fg = "Black",
				bg = "Red",
				command = findGst)
	
	# Create a Gst Rate : label
	gst_rate = Label(gui, text = "Gst Rate", bg = "blue")

	# Create a Clear Button and attached to
	# clearAll function
	clear = Button(gui, text = "Clear", fg = "Black",
				bg = "Red",
				command = clearAll)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .

	# padx attributed provide x-axis margin
	# from the root window to the widget.

	# pady attributed provide y-axis
	# margin from the widget.
	org_price.grid(row = 1, column = 1,padx = 10,pady = 10)
				
	net_price.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	find.grid(row = 3, column = 2,padx = 10,pady = 10)
	
	gst_rate.grid(row = 4, column = 1,padx = 10, pady = 10)
	
	clear.grid(row = 5, column = 2, padx = 10, pady = 10)

	# Create a text entry box for filling or typing the information.
	org_priceField = Entry(gui)
	
	net_priceField = Entry(gui)
	
	gst_rateField = Entry(gui)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	org_priceField.grid(row = 1, column = 2 ,padx = 10,pady = 10)
	
	net_priceField.grid(row = 2, column = 2, padx = 10,pady = 10)
	
	gst_rateField.grid(row = 4, column = 2, padx = 10,pady = 10)
	
	# Start the GUI
	gui.mainloop()

###########################################################################################

print("Question 2")

# import all methods and classes from the tkinter
from tkinter import *

# import calendar module
import calendar

# Function for showing the calendar of the given year
def showCal() :

	# Create a GUI window
	new_gui = Tk()
	
	# Set the background colour of GUI window
	new_gui.config(background = "white")

	# set the name of tkinter GUI window
	new_gui.title("CALENDAR")

	# Set the configuration of GUI window
	new_gui.geometry("550x600")

	# get method returns current text as string
	fetch_year = int(year_field.get())

	# calendar method of calendar module return
	# the calendar of the given year .
	cal_content = calendar.calendar(fetch_year)

	# Create a label for showing the content of the calendar
	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	cal_year.grid(row = 5, column = 1, padx = 20)
	
	# start the GUI
	new_gui.mainloop()

	
# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()
	
	# Set the background colour of GUI window
	gui.config(background = "white")

	# set the name of tkinter GUI window
	gui.title("CALENDAR")

	# Set the configuration of GUI window
	gui.geometry("250x140")

	# Create a CALENDAR : label with specified font and size
	cal = Label(gui, text = "CALENDAR", bg = "dark gray",
							font = ("times", 28, 'bold'))

	# Create a Enter Year : label
	year = Label(gui, text = "Enter Year", bg = "light green")
	
	# Create a text entry box for filling or typing the information.
	year_field = Entry(gui)

	# Create a Show Calendar Button and attached to showCal function
	Show = Button(gui, text = "Show Calendar", fg = "Black",
							bg = "Red", command = showCal)

	# Create a Exit Button and attached to exit function
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
	
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	cal.grid(row = 1, column = 1)

	year.grid(row = 2, column = 1)

	year_field.grid(row = 3, column = 1)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)
	
	# start the GUI
	gui.mainloop()
	
###########################################################################################


print("Question 3")

# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
	# point out the global expression variable
	global expression

	# concatenation of string
	expression = expression + str(num)

	# update the expression by using set method
	equation.set(expression)


# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.

	# Put that code inside the try block
	# which may generate the error
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = Tk()

	# set the background colour of GUI window
	gui.configure(background="light green")

	# set the title of GUI window
	gui.title("Simple Calculator")

	# set the configuration of GUI window
	gui.geometry("270x150")

	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

	# create the text entry box for
	# showing the expression .
	expression_field = Entry(gui, textvariable=equation)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=4, ipadx=70)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, text=' 1 ', fg='black', bg='red',
					command=lambda: press(1), height=1, width=7)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg='black', bg='red',
					command=lambda: press(2), height=1, width=7)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg='black', bg='red',
					command=lambda: press(3), height=1, width=7)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg='black', bg='red',
					command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg='black', bg='red',
					command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg='black', bg='red',
					command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg='black', bg='red',
					command=lambda: press(7), height=1, width=7)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg='black', bg='red',
					command=lambda: press(8), height=1, width=7)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg='black', bg='red',
					command=lambda: press(9), height=1, width=7)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg='black', bg='red',
					command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg='black', bg='red',
				command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg='black', bg='red',
				command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg='black', bg='red',
					command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg='black', bg='red',
					command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg='black', bg='red',
				command=equalpress, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg='black', bg='red',
				command=clear, height=1, width=7)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg='black', bg='red',
					command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=6, column=0)
	# start the GUI
	gui.mainloop()

###########################################################################################

print("Question 4")

# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

###########################################################################################

print("Question:5 ")
	#5a
	
def selectionsort(arr):
    n= len(arr)
    for i in range(n):
        minimum=i
        for j in range(i+1,n):
            if(arr[j]<arr[minimum]):
                minimum=j
        (arr[i],arr[minimum])= (arr[minimum],arr[i])
            
    return arr

def binarySearch(nums, target, searchFirst):
    (left, right) = (0, len(nums) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid         
            if searchFirst:
                right = mid - 1
            else:
                left = mid + 1
 
        elif target < nums[mid]:
            right = mid - 1
       
        else:
            left = mid + 1
    return result
 
nums = [4,5,2,4,5,6,2,3,4,5,7]
target = 5
z= selectionsort(nums)
print(z)
first = binarySearch(z, target, True)        # pass true for the first occurrence
last = binarySearch(z, target, False)        # pass false for the last occurrence
 
count = last - first + 1
if first != -1:
    print(f'Element {target} occurs {count} times')
else:
    print('Element found not in the list')
 
 

 

###########################################################################################

	
print("Question:6 ")
	
# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
def selectionsort(arr):
    n= len(arr)
    for i in range(n):
        minimum=i
        for j in range(i+1,n):
            if(arr[j]<arr[minimum]):
                minimum=j
        (arr[i],arr[minimum])= (arr[minimum],arr[i])
            
    return arr


def bubble_sort(arr):
    n=len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped:
            return arr

arr=[4,5,2,4,5,2,6,3,6,4,5,7]
x=Remove(arr)
print(x)
y= selectionsort(x)
print(y)

z = bubble_sort(x)
print(z)

