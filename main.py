from pyscript import document, window, when
import random
print("Hello, World!")


'''
Here are two ways of linking a button with a python function:

GOAL: 
    MAKE A FUNCTION THAT PRINTS A COMPOUND WORD FORMED BY THE
    TWO WORDS IN THE my_strings ARRAY

'''


#initializing my_strings array
my_strings = [None, None]

'''
**************************************1ST WAY*************************************************
->define BUTTON1 in html so that it appears in webpage (below)
    (in index.html - line 48):
         <button id="my_button1_id"> Print Message</button>
    
->link BUTTON1 with python function when button is clicked
'''
@when("click", "#my_button1_id")
async def way_1_print(event): 
    global my_strings #gets my my_strings array
    string1 = "FOOT"
    my_strings[0] = string1 #storing string 1 in array
    print('"',string1, '" loaded into my_strings array')

'''
**************************************2ND WAY*************************************************
->(same as before) define BUTTON2 in html
    (in index.html - line 49):
         <button id="my_button2_id" class = "button_style"> BUTTON2</button>
    
->link BUTTON2 with python function (shown below function)
'''
def way_2_print(event):
    global my_strings #gets my my_strings array
    string2 = "BALL"
    my_strings[1] = string2 #storing string 2 in array
    print('"',string2, '" loaded into my_strings array')

#linking
button_2_python = document.getElementById('my_button2_id') #gets button from html
button_2_python.onclick = way_2_print #calls function 'way_2_print' when button is clicked

'''
**************************************Your Function below (USE 2ND WAY)*************************************************

'''

def way_3(event):
    global my_strings
    reversed1 = ''.join(reversed(my_strings[0]))
    reversed2 = ''.join(reversed(my_strings[1]))
    print(reversed1+reversed2)

button_3_python = document.getElementById('my_button3_id')
button_3_python.onclick = way_3

@when("click", "#my_button4_id")
async def generate_data(event):
    # Generate a random amount of 1s and 0s with a minimum of 10
    num_elements = random.randint(10, 20)  # Adjust the upper limit as needed
    data = [random.choice([0, 1]) for _ in range(num_elements)]
    
    # Assign Messi to 1 and Ronaldo to 0
    messi_count = data.count(1)
    ronaldo_count = data.count(0)
    
    # Determine which footballer is better based on frequency
    if messi_count > ronaldo_count:
        result = "Messi is better"
    elif ronaldo_count > messi_count:
        result = "Ronaldo is better"
    else:
        result = "It's a tie"
    
    # Print the result in the terminal
    print(f"Generated data: {data}")
    print(result)
   





