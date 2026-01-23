#!/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line(readin):
    # Parses a string of a VCF file (one variant). Tests if the variant is rare, and returns the names of associated diseases as a list.
    # Params: string
    # Returns: list
    print("parse_line: Entering parse_line")

    # Initialize an empty list to add the diseases
    to_add = []

    # Split data into list
    #vcf_list = readin.split(";")
    vcf_list = readin.replace("\t", ";").split(";")
    print(vcf_list)

    for n in range(1,8):
        vcf_list.pop(0)
        

    # Create dict from list
    my_dict = {item.split('=')[0]: item.split('=')[1] for item in vcf_list}

    # Just prints out the dictionary entries for easy viewing
    #print("parse_line: Viewing dictionary entries")
    for key, value in my_dict.items():
        print(key, "-", value)

    # Checks if allele frequency is at threshold
    if "AF_EXAC" in my_dict:
        if float(my_dict["AF_EXAC"]) < 0.0001:
            print(my_dict["AF_EXAC"] + " is under 0.0001")
        else:
            print(my_dict["AF_EXAC"] + " is over 0.0001, excluding")
            return(to_add)
    else:
        print("We didn't find an AF_EXAC")
        return(to_add)

    # Split the diseases into its own string
    if "CLNDN" in my_dict:
        diseases = my_dict["CLNDN"]
        print("Diseases found: " + diseases)
    else:
        print("We didn't find any CLNDN")
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
def read_file():
    pass


if __name__ == "__main__":

    #pprint(read_file("clinvar_20190923_short.vcf"))

    # Initialize string with sample data for temporary testing
    
    # not rare, but contains one disease
    one_line1 = str("1	1041648	263158	G	T	.	.	AF_ESP=0.00500;AF_EXAC=0.00488;AF_TGP=0.00240;ALLELEID=249308;CLNDISDB=MedGen:C3808739,OMIM:615120|MedGen:CN169374|MedGen:CN517202;CLNDN=Myasthenic_syndrome,_congenital,_8|not_specified|not_provided;CLNHGVS=NC_000001.11:g.1041648G>T;CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts;CLNSIG=Benign/Likely_benign;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=AGRN:375790;MC=SO:0001583|missense_variant;ORIGIN=1;RS=138031468")

    # no frequency data, contains diseases
    one_line2 = str("1	1232514	568475	C	G	.	.	ALLELEID=556915;CLNDISDB=MedGen:C0432243,OMIM:271640,Orphanet:ORPHA93359,SNOMED_CT:254100000|MedGen:C3809210,OMIM:615349;CLNDN=Spondyloepimetaphyseal_dysplasia_with_joint_laxity|Ehlers-Danlos_syndrome,_progeroid_type,_2;CLNHGVS=NC_000001.11:g.1232514C>G;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=B3GALT6:126792;MC=SO:0001583|missense_variant;ORIGIN=1;RS=1409554936")

    # not rare but contains multiple diseases
    one_line3 = str("1	1232666	582960	G	A	.	.	AF_EXAC=0.00027;ALLELEID=556627;CLNDISDB=MedGen:C0432243,OMIM:271640,Orphanet:ORPHA93359,SNOMED_CT:254100000|MedGen:C3809210,OMIM:615349;CLNDN=Spondyloepimetaphyseal_dysplasia_with_joint_laxity|Ehlers-Danlos_syndrome,_progeroid_type,_2;CLNHGVS=NC_000001.11:g.1232666G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=B3GALT6:126792;MC=SO:0001583|missense_variant;ORIGIN=1")

    # rare, contains one disease and one not specified
    one_line4 = ("1	2229406	213685	A	G	.	.	AF_ESP=0.00039;AF_EXAC=0.00014;ALLELEID=209452;CLNDISDB=MedGen:C1321551,OMIM:182212,Orphanet:ORPHA2462,SNOMED_CT:83092002|MedGen:CN169374;CLNDN=Shprintzen-Goldberg_syndrome|not_specified;CLNHGVS=NC_000001.11:g.2229406A>G;CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=SKI:6497;MC=SO:0001583|missense_variant;ORIGIN=1;RS=139179843")

        # rare, multiple diseases and not specified
    one_line5 = ("1	2229610	264492	C	A	.	.	AF_EXAC=0.00001;ALLELEID=257944;CLNDISDB=MedGen:C1321551,OMIM:182212,Orphanet:ORPHA2462,SNOMED_CT:83092002|MedGen:CN169374|MedGen:CN230736;CLNDN=Shprintzen-Goldberg_syndrome|not_specified|Cardiovascular_phenotype;CLNHGVS=NC_000001.11:g.2229610C>A;CLNREVSTAT=criteria_provided,_multiple_submitters,_no_conflicts;CLNSIG=Likely_benign;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=SKI:6497;MC=SO:0001819|synonymous_variant;ORIGIN=1;RS=753783431")

    
    found = parse_line(one_line5)
    print("main: We finished reading one line")
    print("We found:")
    print(found)
    print("------------")
