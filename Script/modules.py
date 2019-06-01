#Below are functions for every analysis step per questions from the mini project. 

#..............................................................................................................................#
def option_O():
    """
    The function opens PDB file and loads it in the system"""
    import os
    import sys
    global file_input
    global file_name
    file_input = input("Enter a valid PATH for a PDB file: ")
    name = file_input.split("/")[-1] #get the name of the file loaded 
    if os.path.isfile(file_input):
        print("The File %s has been successfully loaded" %name)
        file_name = name
        return file_name 
    else:
        print ("File does not exists, provide a proper PATH!!!.")
        
        option_O()

 #-----------------------------------------------------------------------------------------------------------------------------#       
        
def option_I():
    """This function returns the file name of the pdb file and header
    of the file as well as displays chains and sequences of the file """
    global file_input
    title = []
    with open(file_input, "r") as file:
        print ("PDB File: %s"%file_name)
        for line in file:
            if line.startswith('TITLE'):
                line = line.rstrip()  #strip ending white spaces including newline 
                title.append(line[9:]) #index where the title is in the file 
                title_str = "".join(title)
        
                
    chains = [] #empty list to append all chains 
    #creating a dictonary for amino acid three letter code to be used to substitute with a single code 
    amino_acid_dic = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
                     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

    with open (file_input, "r") as file:
        for line in file:
            if line.startswith('SEQRES'):
                line = line.rstrip()

                for chain in line[11]: #position where there are all list 
                    chains.append(chain)
                    chain_list = list(set(chains)) #unique chain type put in a list 


        print ('Title:'+"".join( title_str.strip('TITLE')) ,end = " ")
        
        title_chain = '\nCHAINS: ' + " and ".join(sorted(chain_list)) #There are two main chains alpha (A) and Beta(B)
        print(title_chain)

    for a in sorted(chain_list): #iterating between the chains so that you can then open the file based on the chain and print the sequence step by step 
        print(" - Chain %s" %a)

        amino_acid = []
        length_helix = []
        length_sheet = []
        with open (file_input, "r") as file: 
            for line in file:
                if line.startswith('SEQRES'):
                    line = line.rstrip()
                    if a == line[11]:
                        for item in line[19:].split():
                            amino_acid.append(amino_acid_dic[item])  #substituting three letter code with single letter a.a code

                if line.startswith('HELIX'):
                    line = line.rstrip()
                    if a == line[19]:
                        length_helix.append(line[71:75]) #length of the helix in a pdb file 


                if line.startswith('SHEET'):
                    line = line.rstrip()
                    if a == line[21]:
                        length_sheet.append(line[21]) # chain identifier 

            print("    Number of amino acids:   %d " %len(amino_acid))  
            print("    Number of Helix:         %d"  %len(length_helix))      
            print("    Number of Sheet:         %d"  %len(length_sheet))


        amino_lines_list = []
        for i in range (len(amino_acid)//50+1): 
            amino_lines_list.append("".join(amino_acid[i*50:(i+1)*50]))  #printing amnio acid length of 50 per line 
            
        print ("    Sequence:  %s"%amino_lines_list[0]) #print first item of the list with 50characters 
        for a in amino_lines_list[1:]: 
            print('               '+a) #print the rest of the items remaining in the list 

#-----------------------------------------------------------------------------------------------------------------------------#

            
def option_H():
    """This function returns histogram having stars as indication of the 
    frequencies of the amino acid characters"""
    choice_input = input("""
            Choose an option to order by:
               number of amino acids - ascending    (an)
               number of amino acids - descending   (dn)
               alphabetically - ascending           (aa)
               alphabetically - descending          (da)
            order by: """)
    print ("\n")
    if choice_input == 'an':
        amino_acid = []
        with open(file_input, "r") as file:
            for line in file:
                if line.startswith('SEQRES'):
                    line = line.rstrip()
                    amino_acid.append(line[19:])
                    amino_acid_str = " ".join(amino_acid)
                    amino_acid_str = amino_acid_str.title()
                    amino_acid_list = amino_acid_str.split()

            amino_acid_count = {} #create a dictonary having key as amino acid and value is the total count of the amino acid
            for char in amino_acid_list:
                amino_acid_count.setdefault(char, 0)
                amino_acid_count[char] = amino_acid_count[char] + 1

            count_sorted_keys = sorted(amino_acid_count , key = amino_acid_count.get)

            for key_amino in count_sorted_keys:
                value_amino = amino_acid_count[key_amino]
                print ("            " + key_amino, "( %2d)" %value_amino, ":", value_amino * "*") #print key , value and (value * stars) 

    elif choice_input == "dn":
        amino_acid = []
        with open(file_input, "r") as file:
            for line in file:
                if line.startswith('SEQRES'):
                    line = line.rstrip()
                    amino_acid.append(line[19:])
                    amino_acid_str = " ".join(amino_acid)
                    amino_acid_str = amino_acid_str.title()
                    amino_acid_list = amino_acid_str.split()

            amino_acid_count = {}
            for char in amino_acid_list:
                amino_acid_count.setdefault(char, 0)
                amino_acid_count[char] = amino_acid_count[char] + 1


            #reverse of an option 
            count_sorted_keys = sorted(amino_acid_count , key = amino_acid_count.get, reverse = True)

            for key_amino in count_sorted_keys:
                value_amino = amino_acid_count[key_amino]
                print ("            " + key_amino, "( %2d)" %value_amino, ":", value_amino * "*")

    elif choice_input == 'aa' :
        amino_acid = []
        with open(file_input, "r") as file:
            for line in file:
                if line.startswith('SEQRES'):
                    line = line.rstrip()
                    amino_acid.append(line[19:])
                    amino_acid_str = " ".join(amino_acid)
                    amino_acid_str = amino_acid_str.title()
                    amino_acid_list = amino_acid_str.split()

            amino_acid_count = {}
            for char in amino_acid_list:
                amino_acid_count.setdefault(char, 0)
                amino_acid_count[char] = amino_acid_count[char] + 1

            for key, value in sorted(amino_acid_count.items()):
                print ("            " + key, "( %2d)" %value,":", value * '*')

    elif choice_input == 'da':
        amino_acid = []
        with open(file_input, "r") as file:
            for line in file:
                if line.startswith('SEQRES'):
                    line = line.rstrip()
                    amino_acid.append(line[19:])
                    amino_acid_str = " ".join(amino_acid)
                    amino_acid_str = amino_acid_str.title()
                    amino_acid_list = amino_acid_str.split()

            amino_acid_count = {}
            for char in amino_acid_list:
                amino_acid_count.setdefault(char, 0)
                amino_acid_count[char] = amino_acid_count[char] + 1

           # reverse option of aa
            for key, value in sorted(amino_acid_count.items(), reverse = True):
                print ("            " + key, "( %2d)" %value,":", value * '*')

    else: 
        print ("Wrong option, re-enter option as in menu")
        option_H()

#-----------------------------------------------------------------------------------------------------------------------------#        
        
def option_S():
    chains = []
    amino_acid_dic = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
                     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

    with open(file_input, "r") as file:
        for line in file:
            if line.startswith('SEQRES'):
                line = line.rstrip()

                for chain in line[11]:
                    chains.append(chain)
                    chain_list = list(set(chains))

    print("Secondary Structure of the PDB id %s:"%file_name)
    
    for a in sorted(chain_list):
        print("Chain %s:" %a)
        print ("(1)")

        amino_acid = []
        with open(file_input, "r") as file: 
            helix_intial = [] #empty list to append all positions of intial interger of helix
            helix_end = [] # empty list to append all positions of end interger of helix
            helix_id = [] #empty list to append helix identifier 
            position_helix_dict = {}
            sheet_intial = []
            sheet_end = []
            position_sheet_dict = {}
            position_id = [] #empty list of spaces having the same length with amino acid
            sheet_id_start = []
            sheet_id_end = []
            sheet_id = [] 
            for line in file:
                if a == line[11]:
                    if line.startswith('SEQRES'):
                        line = line.rstrip()
                        for item in line[19:].split():
                            amino_acid.append(amino_acid_dic[item])


                        amino_str = "".join(amino_acid) #convert amino acid list to a string to help in printing it out at the end 

                if line.startswith('HELIX') and a == line[19]:
                    line = line.rstrip()

                    helix_intial.append(line[21:25]) #intial interger
                    helix_end.append(line[33:37]) #end interger 
                    helix_id.append(line[13]) #helix identifier 

                    position_helix_dict = dict(zip(helix_intial, helix_end)) # a dictonary to have intial(key):end(value) as range of where the helix is 

                if line.startswith('SHEET') and a == line[21]:
                    line = line.strip()
                    sheet_intial.append(line[23:27]) #Sequence number of initial residue
                    sheet_end.append(line[34:38]) #Sequence number of terminal residue
                    #based on question sheet id has two letters i.e. strand number and sheet identifier 
                    sheet_id_start.append(line[9]) #Strand  number which starts at 1 for each and increases by 1
                    sheet_id_end.append(line[13]) # sheet identifier 

                    position_sheet_dict = dict(zip(sheet_intial, sheet_end)) 

            for d in range(len(amino_str)): 
                position_id.append(" ") #making a list with empty spaces same lenght as amino acid

            for idindex in range(0, len(helix_intial)):
                position_id[int(helix_intial[idindex])-1] = helix_id[idindex] #index position of where the helix starts 

            for x in range(0, len(sheet_id_start)):
                x = str(sheet_id_start[x])+str(sheet_id_end[x]) #combining the strand number and sheet identifier 
                sheet_id.append(x) # now we have sheet id for example '1A'

            #index where the sheet id position is in the amino acid
            for idsheet in range(0, len(sheet_intial)):
                position_id[int(sheet_intial[idsheet])-1:int(sheet_intial[idsheet])-1+len(sheet_id[idsheet])] = sheet_id[idsheet]

            for key, value in position_helix_dict.items():
                helix_amino = []
                for helix in range(int(key), int(value) + 1):
                    helix_amino += "/" #update file with '/' where there is helix, replacing alphabet with the sign
                amino_acid[int(key)-1:int(value)] = helix_amino

            for key, value in position_sheet_dict.items():
                sheet_amino = []
                for sheet in range(int(key), int(value) + 1):
                    sheet_amino += "|" #update file with '|' where there is sheet, replacing alphabet with the sign
                amino_acid[int(key)-1:int(value)] = sheet_amino  

            for aminoindex in range(0, len(amino_acid)):
                if amino_acid[aminoindex].isalnum(): #if character is an alphabet letter i.e. not replaced
                    amino_acid[aminoindex] = "-" 

        #print amino acid , character symbol ID , and  position ID where it starts 
        for i in range(len(amino_str)//80+1):
            print (amino_str[i*80:(i+1)*80] + "\n"+"".join(amino_acid[i*80:(i+1)*80]) + "\n" + "".join(position_id[i*80:(i+1)*80]))
            print("\n")
        
        print("(%d)"%len(amino_acid)) #lenght of amino acid 
        print("\n") 


#-----------------------------------------------------------------------------------------------------------------------------#

def option_X():

    """
    This function returns a file saved to results folders with content written to it from 
    file you want to export"""
    import os 
    import sys
    
    file_input = input("Enter a valid PATH for a PDB file you want to EXPORT: ")
    if os.path.isfile(file_input):
        print("The File %s has been successfully loaded" %file_input)
    else:
        print ("File does not exists, provide a proper PATH!!!.")
        option_X()
    
    file_output = input("Enter name of output file you want to export: ")

    path_output_file = os.path.join("../Results/" , file_output+".txt") #path where you want your created .txt file to be saved 
    
    f = open(path_output_file, "w+")   # creating a .txt file 

    f.close()

    with open(path_output_file, "w") as output: #open file to write 

        with open(file_input, "r") as file: 
            for line in file:

                output.write(line)
                
            print( "File %s has been exported to %s" %(file_input, file_output+".txt"))

#-----------------------------------------------------------------------------------------------------------------------------#
                






        



        


