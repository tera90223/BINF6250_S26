#!/usr/bin/env python
# Shebang line to execute script directly from command line

# Import necessary module
from pprint import pprint  # Pretty-printing for cleaner output


def parse_line(line):
    """
    Parse a single VCF data line and extract disease names for rare variants
    Parameters: line (str): A single line from VCF file
    Returns: list: A list of disease names associated with the variant ONLY if:
                    AF_EXAC exists
                    AF_EXAC < 0.0001 (rare variant)
                    CLNDN exists
                    Diseases are not 'not_specified' or 'not_provided'
        Returns empty list if the line does not meet criteria
    """

    # Skip meta-information (##...) and header line (#CHROM...)
    if line.startswith("#"):
        return []

    # Remove trailing newline and split the VCF row into its 8 tab-separated columns
    columns = line.strip().split("\t")

    # The INFO column is always the 8th column in a VCF (index 7)
    info_field = columns[7]

    # Split INFO field into key=value pairs separated by semicolons
    info_pairs = info_field.split(";")
    info_dict = {}  # Temporary dictionary to store parsed key=value pairs

    # Build dictionary of INFO key=value pairs
    for pair in info_pairs:
        # Only process entries that contain an '=' sign
        if "=" in pair:
            # Split into key=value at the FIRST '=' only
            # This prevents breaking values that might contain '='
            key, value = pair.split("=", 1)

            # Store in dictionary for easy access
            info_dict[key] = value

    # If AF_EXAC key missing, skip variant
    if "AF_EXAC" not in info_dict:
        return []  # Return empty list

    # Convert AF_EXAC value to float; skip if not possible
    try:
        af_exac = float(info_dict["AF_EXAC"])
    # If value error returned (ie, string entry input errors)
    except ValueError:
        return []  # Return empty list

    # Only keep if af_exac indicates rare variant (less than 0.01% of pop)
    if af_exac >= 0.0001:
        return []  # Return empty list

    # If CLNDN missing, skip
    if "CLNDN" not in info_dict:
        return []  # Return empty list

    # Extract diseases from CLNDN key, multiple diseases pipe-separated
    diseases = info_dict["CLNDN"].split("|")

    # Remove not_provided and not_specified entries with list comprehension
    cleaned_disease_data = [
        d for d in diseases
        if d not in ("not_specified", "not_provided")
    ]

    return cleaned_disease_data


def read_file(filename):
    """
    Read a VCF file line-by-line and count disease occurrences for rare variants
    Parameters: filename (str): Path to VCF file to be opened and processed
    Returns: dict: A dictionary in which:
                   keys = disease names
                   values = number of times each disease appears in rare variants
    """

    # Initialize dictionary to hold counts
    disease_counts = {}

    # Open file
    with open(filename, "r") as f:

        # Read file line by line
        for line in f:
            # parse_line returns list of diseases or empty list
            diseases = parse_line(line)

            # Count each disease returned
            for d in diseases:
                # If new disease, add to disease_counts
                if d not in disease_counts:
                    # Initialize count at 1 for new disease
                    disease_counts[d] = 1
                # If disease exists in disease_counts
                else:
                    # Increment tally for disease
                    disease_counts[d] += 1

    return disease_counts


if __name__ == "__main__":
    # Pretty print final dictionary of disease counts
    pprint(read_file("clinvar_20190923_short.vcf"))
