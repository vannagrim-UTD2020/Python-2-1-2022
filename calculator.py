# import all classes / functions from the tkinter
from tkinter import *
def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    payment_field.delete(0, END)
    principal_field.focus_set()
    

def calculate_ci():
    principal = int(principal_field.get())
    
    rate = float(rate_field.get())
    
    time = int(time_field.get())

	# Calculates compound interest
    monthly_interest_rate = rate/1200
    amount_of_months = time * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))
    CI = principal * (pow((1 + rate / 100), time))
    
    
	# insert method inserting the
	# value in the text entry box.
    payment_field.insert(10, monthly_payment)



# Driver code
if __name__ == "__main__":

	# GUI window details
	root = Tk()

	
	root.configure(background='light green')

	
	root.geometry("400x250")

	
	root.title("Monthly Loan Payment Calculator")

	# Make all the labels
	label1 = Label(root, text="Principal Amount(Rs) : ",
                fg='black')

	
	label2 = Label(root, text="Rate(%) : ",
                fg='black')

	
	label3 = Label(root, text="Time(years) : ",
                fg='black')

	# Create a Compound Interest : label
	label4 = Label(root, text="Monthly Payment: ",
                fg='black')


	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	label1.grid(row=1, column=0, padx=10, pady=10)
	label2.grid(row=2, column=0, padx=10, pady=10)
	label3.grid(row=3, column=0, padx=10, pady=10)
	label4.grid(row=5, column=0, padx=10, pady=10)

	# Create a entry box
	# for filling or typing the information.
	principal_field = Entry(root)
	rate_field = Entry(root)
	time_field = Entry(root)
	payment_field = Entry(root)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .

	# padx keyword argument used to set padding along x-axis .
	# pady keyword argument used to set padding along y-axis .
	principal_field.grid(row=1, column=1, padx=10, pady=10)
	rate_field.grid(row=2, column=1, padx=10, pady=10)
	time_field.grid(row=3, column=1, padx=10, pady=10)
	payment_field.grid(row=5, column=1, padx=10, pady=10)

	# Create a Submit Button and attached
	# to calculate_ci function
	button1 = Button(root, text="Submit", 
                  fg="black", command=calculate_ci)

	# Create a Clear Button and attached
	# to clear_all function
	button2 = Button(root, text="Clear", 
                  fg="black", command=clear_all)

	button1.grid(row=4, column=1, pady=10)
	button2.grid(row=6, column=1, pady=10)

	# Start the GUI
	root.mainloop()
