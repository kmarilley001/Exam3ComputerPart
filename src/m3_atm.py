#GOT HELP  to figure out .cget function  https://www.tutorialspoint.com/get-the-text-of-a-button-widget-in-tkinter and to figure out lambda function which was used to pass an argument which in this case was the number on button as a command :https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python 


import tkinter as tk

window = tk.Tk() 
window.title("ATM")

current_balance = 1000

# Create and display labels 
current_balance_label = tk.Label(window, text= "Current Balance ($):")
current_balance_label.pack()
current_balance_amount = tk.Label(window, text= current_balance)
current_balance_amount.pack() 

amount_label = tk.Label(window, text = "Amount ($):")
amount_label.pack() 
amount_display = tk.Label(window, text = "")
amount_display.pack() 


button_frame = tk.Frame(window)
button_frame.pack() 

# This function is responsible for updating amount display when number button has been pressed. 
def update_amount_display(number):
    current_text = amount_display.cget("text")
    amount_display.config(text=current_text + str(number))

#function clears amount display label 
def clear_amount():
    amount_display.config(text="")

# This function is responsible when user wants to withdraw funds from account which retrieves current balance that is displayed and would convert to a float so that the new balance can be calculated. After calculation the float is converted back to a string. 
def withdraw():
    current_balance = float(current_balance_amount.cget("text"))
    withdraw_amount = float(amount_display.cget("text"))
    new_balance = current_balance - withdraw_amount
    current_balance_amount.config(text=str(new_balance))
    clear_amount()
# Same as withdraw function
def deposit():
    current_balance = float(current_balance_amount.cget("text"))
    deposit_amount = float(amount_display.cget("text"))
    new_balance = current_balance + deposit_amount
    current_balance_amount.config(text=str(new_balance))
    clear_amount()

# handles button clicks corresponding to the digits on keypad
def number_button_handler(number):
    update_amount_display(number)

# is a loop for the nine buttons with the digits 1 to 9, configure the command to call the function above with digit as an arg and arranges them in the frame. 
buttons = [] 
for i in range(1,10): 
    button = tk.Button(button_frame, text= str(i), width = 5, height=2)
    button.config(command=lambda num= i: number_button_handler(num))
    button.grid(row= (i-1)//3, column = (i-1)%3)
    buttons.append(button)
    
# Same as above but for button 0
button_0 = tk.Button(button_frame, text = "0", width = 5, height = 2)
button_0.config(command=lambda: number_button_handler(0))
button_0.grid(row = 3, column =1)

#the two lines of code below create buttons for withdrawal and deposit actions
withdraw_button = tk.Button(button_frame, text="Withdrawal", width=10, height=2, command = withdraw)
withdraw_button.grid(row=3, column=0)

deposit_button = tk.Button(button_frame, text="Deposit", width=10, height=2, command = deposit )
deposit_button.grid(row=3, column=2)

#establishes a binding between function and keypress event. function checks if the pressed key is a digit and if it is it retrieves it. 
def key_press(event): 
    if event.charisdigit(): 
        current_text = amount_display.cget("text")
        amount_display.config(text=current_text + event.char)
window.bind("<Key>", key_press)        





window.mainloop()


###############################################################################
#DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
#DONE: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 6. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
