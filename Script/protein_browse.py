#! /home/cofia/miniconda3/bin/python

"""
This script analyses a pdb file looking at its title, information, making a histogram, secondary structure
and exporting the file. Note that you have to load the file first to input the other options of analysis
Python Version: 3.7.2 

"""

file_name = '  None  ' 

import modules #modules created that have all the functions in the options 

def menu(file_name):
    """
    This function returns menu
    """
    print (80 * '*')
    print ('*' + 1*' ' + 'PDB FILE ANALYZER' + 60*' ' + '*')
    print (80 * '*')
    print ('*'+ 1*' ' + 'Select an option from below:' + 49*' ' + '*')
    print ('*' + 78*' ' + '*')
    print ('*' + 6*' ' + '1) Open a PDB File' + 23*' ' + '(O)' + 28*' ' + '*')
    print ('*' + 6*' ' + '2) Information'+ 27*' ' + '(I)' + 28*' ' + '*')
    print ('*' + 6*' ' + '3) Show histogram of amino acids '+ 8*' ' + '(H)' + 28*' ' + '*')
    print ('*' + 6*' ' + '4) Display Secondary Structure'+ 11*' ' + '(S)' + 28*' ' + '*')
    print ('*' + 6*' ' + '5) Export PDB File '+ 22*' ' + '(X)' + 28*' ' + '*')
    print ('*' + 6*' ' + '6) Exit '+ 33*' ' + '(Q)' + 28*' ' + '*')
    print ('*' + 55*' ' + 'Current PDB: %s  ' %file_name + '*')
    print (80 * '*')
    
menu(file_name)

def input_options():
    """
    This functions returns options that you want to choose for protein file analysis"""
    global file_input
    option = input (""" 
    From the Menu, below are the options for you to input. 
    Kindly provide input from the options provided 
                        O: Open a PDB file
                        I: Information 
                        H: Show histogram of amino acids
                        S: Display Secondary structure 
                        X: Export PDB File
                        Q: Exit
                        
                        Please Enter your choice: """)
    if option.lower() == 'o':
        #file_name = modules.option_O() #overwriting name variable returned from the function
        file_name = modules.option_O()
        menu(file_name)
        input_options()    
    elif option.lower() == 'i':
        modules.option_I()
        input_options()  
    elif option.lower() == 'h':
        modules.option_H()
        input_options()
    elif option.lower() == 's':
        modules.option_S()
        input_options()
    elif option.lower() == 'x':
        modules.option_X()
        input_options()
    elif option.lower() == 'q':
        exit2()
    else:
        print("Enter correct option as per MENU above....Try again!!!")
        input_options()

def exit2():
    """
    This function is for an exit option 
    """
    exit_plan = input('Do you want to exit (E) or Do you want to go back to menu (M)')
    exit_plan = exit_plan.upper()
    if exit_plan == 'E':
        print ('Awesome!!! Thank you for using this script to browse your PDB file.')
    elif exit_plan == 'M':
        print ('Okay....Taking you back to the menu.')
        input_options()
    else:
        print("Enter correct option either E or M ....Try again!!!")
        exit2()     

input_options()