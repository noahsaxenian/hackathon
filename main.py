from pyscript import document, window, when
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
    for s in my_strings:
        print(s[::-1])

button_3_python = document.getElementById('my_button3_id')
button_3_python.onclick = way_3
   





