#!/usr/bin/env python
from pprint import pprint
from collections import Counter


# Modify this function signature and fill in the details
def parse_line(line: str) -> list:
    """
    Provides a list of associated diseases for rare variant in a vcf file
    :param line: String representing a VCF variant line
    :return: List of associated diseases for rare variant
    """

    # Initialize variables
    variant_info_dict = {}      # Info dictionary
    associated_diseases = []    # Associated Diseases List
    rare_threshold = 0.0001     # Rare disease threshold based on allele frequency

    # VCF variants lines are made up of tab-separated columns
    # As we are interested in the INFO column (last column)
    # split line into columns and then grab info column
    variant_cols = line.split("\t")
    variant_info = variant_cols[-1]

    # key-value pairs in the info column are separated by ";"
    # Create a list object that holds key-value pairs
    variant_info_pairs = variant_info.split(";")

    # Create a dictionary from list
    for pair in variant_info_pairs:
        variant_info_dict[pair.split("=")[0]] = pair.split("=")[1]

    # Check if dictionary has allele frequency key
    if "AF_EXAC" in variant_info_dict:
        # Convert allele frequency value into float
        AF_EXAC = float(variant_info_dict["AF_EXAC"])
        # Check if variant is rare using allele frequency
        if(AF_EXAC < rare_threshold):
            # Get all diseases for rare variant
            diseases = variant_info_dict["CLNDN"].split("|")

            # Append to associated diseases list excluding not_provided and not_specified
            for disease in diseases:
                if disease not in ("not_provided","not_specified"):
                    associated_diseases.append(disease)
            # Return Associated Diseases
            return associated_diseases
    else:
        # If allele frequencies does not indicate variant rareness or if not provided, return empty list
        return []

# Modify this function signature and fill in the details
def read_file(filename: str) -> Counter:
    """
    Reads a file and returns disease counts
    :param filename: String representing File path
    :return: Dictionary mapping diseases to their counts in VCF file
    """
    # Initialize Counter dictionary
    disease_counter = Counter()
    # Try to open file, or catch exception
    try:
        with open(filename, "r") as infile:
            # Read file line by line (not using readlines() as vcf files can be large)
            for line in infile:
                # Strip line of leading and trailing whitespace characters
                line = line.strip()
                # Skip lines that start with #
                if line.startswith("#"):
                    continue
                # Pass line to parse_line
                disease_list = parse_line(line)
                # Count the results in disease list:
                if disease_list:
                    disease_counter.update(disease_list)
        # Return dictionary
        return(disease_counter)
    except Exception as e:
        print(f"An error occurred while reading file: {e}")


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
