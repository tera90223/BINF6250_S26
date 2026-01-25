#!/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line(readin):
    '''
    Parses a string of a VCF file (one variant). Tests if the variant is rare, and returns the names of associated diseases as a list.
    Params: string
    Returns: list
    '''
    
    #print("parse_line: Entering parse_line")

    # Initialize an empty list to add the diseases
    to_add = []
    # Set threshold for rare diseases
    threshold = 0.0001

    # Split data into list
    #vcf_list = readin.split(";")
    vcf_list = readin.replace("\t", ";").split(";")
    #print(vcf_list)

    for n in range(1,8):
        vcf_list.pop(0)

    # Create dict from list
    my_dict = {item.split('=')[0]: item.split('=')[1] for item in vcf_list}

    # Just prints out the dictionary entries for easy viewing
    #print("parse_line: Viewing dictionary entries")
    #for key, value in my_dict.items():
    #    print(key, "-", value)

    # Checks if allele frequency is at threshold
    if "AF_EXAC" in my_dict:
        if float(my_dict["AF_EXAC"]) < threshold:
            pass
            #print(my_dict["AF_EXAC"] + " is under 0.0001")
        else:
            #print(my_dict["AF_EXAC"] + " is over 0.0001, excluding")
            return(to_add)
    else:
        #print("We didn't find an AF_EXAC")
        return(to_add)

    # Split the diseases into its own string
    if "CLNDN" in my_dict:
        diseases = my_dict["CLNDN"]
        #print("Diseases found: " + diseases)
    else:
        #print("We didn't find any CLNDN")
        return(to_add)

    # Pipe delimiter separates into list entries
    disease_list = diseases.split("|")
    #print(disease_list)

    # Add items to our list to pass back to calling function, removing not specified and not provided 
    for item in disease_list:
        if item != "not_specified" and item != "not_provided":
            to_add.append(item)
    #print(to_add)

    return(to_add)



# Modify this function signature and fill in the details
def read_file(filename):
    '''
    Reads a filename passed in as argument, opens the file, passes one line at a time to parse_line, and tallies returned results
    Params: string
    Returns: dictionary
    '''
    print("Reading: " + filename)

    # Initialize dictionary
    disease_list = []
    disease_dict = {}
    
    # Not quite finished
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                #print("Skipping metadata")
                pass
            else:
                #print("We found a line to try")
                disease_list = parse_line(line)
                for item in disease_list:
                    if item not in disease_dict:
                        #print(item + " not yet in dict, adding.")
                        disease_dict[item] = 1
                    elif item in disease_dict:
                        #print(item + " found " + disease_dict[item] + times)
                        disease_dict[item] = disease_dict[item] + 1

    return disease_dict


if __name__ == "__main__":

    pprint(read_file("clinvar_20190923_short.vcf"))

