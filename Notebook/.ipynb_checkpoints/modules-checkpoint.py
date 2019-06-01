def option_O():
    """
    The function opens PDB file and loads it in the system"""
    import os
    import sys
    global file_input
    global file_name
    file_input = input("Enter a valid PATH for a PDB file: ")
    name = file_input.split("/")[-1] #get the name of the file loaded 
    print(name)
    if os.path.isfile(file_input):
        print("The File %s has been successfully loaded" %name)
        file_name = name
        #return name  
    else:
        print ("File does not exists, provide a proper PATH!!!.")
        
        option_O()
        
        
def option_I():
    """This function for option I returns the file name of the pdb file and header
    of the file as well as displays chains requence of the file """
    global file_input
    title = []
    with open(file_input, "r") as file:
        print ("PDB File :%s"%file_input)
        for line in file:
            if line.startswith('TITLE'):
                line = line.rstrip()  #strip ending white spaces including newline 
                title.append(line[9:])
                title_str = "".join(title)
        
                
    chains = []
    amino_acid_dic = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
                     'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N', 
                     'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
                     'ALA': 'A', 'VAL':'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

    with open ("./a.pdb", "r") as file:
        for line in file:
            if line.startswith('SEQRES'):
                line = line.rstrip()

                for chain in line[11]:
                    chains.append(chain)
                    chain_list = list(set(chains))


        print ('Title:'+"".join( title_str.strip('TITLE')) ,end = " ")
        
        if len(chain_list) <= 2 :
            title_chain = '\nCHAINS: ' + " and ".join(chain_list)
        print(title_chain)
    for a in sorted(chain_list):
        
        
        print("-Chain %s" %a)

        amino_acid = []
        length_helix = []
        length_sheet = []
        with open ("./a.pdb", "r") as file: 
            for line in file:
                if line.startswith('SEQRES'):
                    line = line.rstrip()
                    if a == line[11]:
                        for item in line[19:].split():
                            amino_acid.append(amino_acid_dic[item])  

                if line.startswith('HELIX'):
                    line = line.rstrip()
                    if a == line[19]:
                        length_helix.append(line[71:75])


                if line.startswith('SHEET'):
                    line = line.rstrip()
                    if a == line[21]:
                        length_sheet.append(line[21])


            print("Number of amino acids:%d " %len(amino_acid))  
            print("Number of Helix:      %d"  %len(length_helix))      
            print("Number os Sheet:      %d"  %len(length_sheet))


        for i in range (len(amino_acid)//50+1):
            print ('            '+"".join(amino_acid[i*50:(i+1)*50]))  




            
def option_H():
    choice_input = input("""
            Choose an option to order by:
                number of amino acids - ascending    (an)
                number of amino acids - descending   (dn)
                alphabetically - ascending           (aa)
                alphabetically - descending          (da)
            order by:""")

    if choice_input == 'an':
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

            count_sorted_keys = sorted(amino_acid_count , key = amino_acid_count.get)

            for key_amino in count_sorted_keys:
                value_amino = amino_acid_count[key_amino]
                print (key_amino, "( %2d)" %value_amino, ":", value_amino * "*")

    elif choice_input == "dn":
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



            count_sorted_keys = sorted(amino_acid_count , key = amino_acid_count.get, reverse = True)

            for key_amino in count_sorted_keys:
                value_amino = amino_acid_count[key_amino]
                print (key_amino, "( %2d)" %value_amino, ":", value_amino * "*")

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

           # print(count)
            for key, value in sorted(amino_acid_count.items()):
                print (key, "( %2d)" %value,":", value * '*')

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

           # print(count)
            for key, value in sorted(amino_acid_count.items(), reverse = True):
                print (key, "( %2d)" %value,":", value * '*')

    else: 
        print ("Wrong option, re-enter option as in menu")
        option_S()

        
        
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
            #amino = []
            helix_intial = []
            helix_end = []
            helix_id = []
            position_helix_dict = {}
            sheet_intial = []
            sheet_end = []
            position_sheet_dict = {}
            position_id = []#empty list of spaces having the same length with amino acid
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

                    helix_intial.append(line[21:25])
                    helix_end.append(line[33:37])
                    helix_id.append(line[13])

                    position_helix_dict = dict(zip(helix_intial, helix_end))

                if line.startswith('SHEET') and a == line[21]:
                    line = line.strip()
                    sheet_intial.append(line[23:27])
                    sheet_end.append(line[34:38])
                    sheet_id_start.append(line[9])
                    sheet_id_end.append(line[13])

                    position_sheet_dict = dict(zip(sheet_intial, sheet_end))


            for d in range(len(amino_str)):
                position_id.append(" ")


            for idindex in range(0, len(helix_intial)):
                position_id[int(helix_intial[idindex])-1] = helix_id[idindex]


            for x in range(0, len(sheet_id_start)):
                x = str(sheet_id_start[x])+str(sheet_id_end[x])
                sheet_id.append(x)

            for idsheet in range(0, len(sheet_intial)):
                position_id[int(sheet_intial[idsheet])-1:int(sheet_intial[idsheet])-1+len(sheet_id[idsheet])] = sheet_id[idsheet]



            for key, value in position_helix_dict.items():
                helix_amino = []
                for helix in range(int(key), int(value) + 1):
                    helix_amino += "/"
                amino_acid[int(key)-1:int(value)] = helix_amino


            for key, value in position_sheet_dict.items():
                sheet_amino = []
                for sheet in range(int(key), int(value) + 1):
                    sheet_amino += "|"
                amino_acid[int(key)-1:int(value)] = sheet_amino  

            for aminoindex in range(0, len(amino_acid)):
                if amino_acid[aminoindex].isalnum(): #if character is an alphabet letter 
                    amino_acid[aminoindex] = "-"


        for i in range(len(amino_str)//80+1):
            print (amino_str[i*80:(i+1)*80] + "\n"+"".join(amino_acid[i*80:(i+1)*80]) + "\n" + "".join(position_id[i*80:(i+1)*80]))
        
        print("(%d)"%len(amino_acid))
        print("\n")
            
            




        



        


