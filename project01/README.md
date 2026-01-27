# Introduction

This is the first assignment for the Algorithms in Bioinformatics course
at Northeastern University for Spring 2026, entitled “Functional File
Parsing”. The purpose of the assignment is to demonstrate the ability to
parse data from a specialized form of a Variant Call Format (VCF),
derived from NIH’s ClinVar database. ClinVar is a public archive of
reports of human variations classified for diseases and drug responses
(NIH, 2024). The expected output of the program is a dictionary of all
the diseases associated with rare variants of the gene in question as
the key, and the number of times each disease is observed as the value.

The VCF is a dense text file designed to store gene sequence variants in
an organized, tabular format (GA4GH, 2024). At the top of the file
exists metadata denoted by double hashtags (##) that contains
information about the experiment, formatting notations within the file,
and important details about the data included about the variants of the
gene. This segment is followed by the header, marked with a single
hashtag (#), which presents the titles of eight fixed, mandatory columns
of data, each separated by a tab delimiter:

- CHROMOSOME- An identifier from the reference genome pointing to a
  contig in the assembly file and represented as a contiguous block in
  the file

- POS- the reference position, with the first base starting at position
  1

- ID- a semicolon-separated list of unique identifiers if available

- REF- reference base(s), can be A, C, T, G, N, with multiple bases
  permitted and the position field referring to the first base in the
  string

- ALT: comma-separated list of alternate non-reference alleles made up
  of the same base designations as the reference field

- QUAL: the PHRED quality score for the call made in the alternate field

- FILTER: the filter status of the position in the contig, with PASS
  meaning the position has passed all filters, meaning a call is made at
  the position. If the site has not passed all filters, a
  semicolon-separated list of codes is present for the failed filters

- INFO: a semicolon-separated set of additional information, with each
  subfield formatted as key=value. If a key has more than one value,
  they are comma-separated. Several resserved keys exist, but arbitrary
  keys can also be created and must be noted in the meta-information

Within clinvar\_20190923\_short.vcf are two additional keys crucial for
selecting the data in this assignment:

- AF\_EXAC: allele frequencies from the Exome Aggregation Consortium
  database, with the data represented as floating point numbers
- CLNDN: disease(s) associated with the specified variant, represented
  as strings, and if more than one present, pipe-separated (|)

To determine an allele variant as rare for this assignment, the AF\_EXAC
threshold value is designated as less than 0.0001, or 0.01%. In the
context of severe disease, this threshold is a common filter and
constitutes an extraordinarily rare variant, as such variants are
generally not expected to exist in the general population at significant
frequencies (Harrison et al., 2019). Variants with greater rarity are
more likely to have functional consequences, and if associated with a
phenotype, are more likely to be pathogenic. On the other hand, common
variants are frequently classified as benign.

# Pseudocode

Put pseudocode in this box:

    parse_line function pseudocode
    *   Initialize an empty disease list 
    *   Take string as argument input – this will be one row of the file
    *   Create an inner dictionary parsing by “;” where key fields are title: value
    *   Check if AF_EXAC is in the line 
        +   if not in line, return empty list
        +   Check if AF_EXAC is < 0.0001
            -   If rare: 
                    > May be multiple diseases separated by | (pipe)
                    > Skip diseases: not_specified, not_provided
                    > Return list of diseases in CLNDN
        +   If not rare or if AF_EXAC is not provided 
            - return empty list

    read_file pseudocode
    *   Takes string as argument input – this will be the file name
    *   Open the file
    *   Read the file line by line and strip the line of trailing and leading whitespaces
        +   Skip if line starts with #
        +   Pass this string to parse_file as an argument   
        + Receive results from parse_line as a list
    *   Tally results under a dictionary as they are received
        +   Return dictionary of diseases associated with rare variants, each with final tally of occurence

# Successes

During our initial meeting in class, we created a rough draft of the
psuedocode as a team. We then developed our own versions of the program
in the day before we reconvened. At our next meeting, each of us
presented the codes we had designed bassed on our pseudocode. We
compared approaches, sharing ideas and opinions, and asking for
clarification as needed- it was akin to an in-person peer review
session. Lastly, we made agreements as a team about what to include in
the final code. We all agreed that this approach was very productive. It
required everyone to contribute to the project, but in a way where
everyone’s individual approach could be considered, rather than one
person dictating the way the code is written. This was highly valuable
to us because everyone has their own coding style, and having three
versions to draw from when constructing our final script made our
program robust.

# Struggles

Working with the VCF file required a level of precision that made the
string‑parsing component one of the most challenging parts of the
assignment. The file was very dense and there were frequently multiple
diseases associated with each variant within the INFO column. Because
there are multiple valid ways to break the data apart, we had to be
intentional about choosing a parsing strategy that was both correct and
maintainable. The entire INFO field for each variant is stored as a
single semicolon‑delimited string, so even small mistakes in splitting
or interpreting key–value pairs could lead to incorrect filtering or
missed disease annotations.

Another challenge we encountered was designing test cases that
represented the full range of scenarios we might encounter in such an
information-dense file. The INFO field is not guaranteed to be
consistent across variants, particularly because key entries can be
arbitrary. Therefore, we had to account for:

- variants with no diseases specified

- variants with multiple diseases separated by pipes

- invalid or placeholder entries such as not\_specified or not\_provided

- missing keys, especially when AF\_EXAC or CLNDN were absent

- formatting inconsistencies such as empty INFO fields or non‑numeric
  AF\_EXAC values

Creating these test cases forced us to think carefully about edge
conditions and errors that could arise if they were not accounted for.
It also helped validate that our parsing logic ran appropriately across
all possible inputs, not only for the expectations defined in the VCF
documentation. Our assurance of careful string parsing and comprehensive
test coverage gave us confidence that the program would properly and
reliably parse the VCF data to return the dictionary containing diseases
associated with rare variants and their number of occurrences.

# Personal Reflections

## Group Leader:

### Chantera Lazard

This project provided me an opportunity to engage with Python after a year of primarily working in R. Most of the syntax and flow came back naturally although W3 schools was also helpful! 

Working with a VCF file was another aspect I quite enjoyed as these files show up in research and clinical contexts. Parsing VCF data through string manipulation and extraction of data strengthened my understanding of how to utilize the files and even to aid in preparation for downstream analysis. 

Working collaboratively with a team with varied technical backgrounds and learning styles proved a challenge as we spent most of our time working towards understanding the problem and its underlying assumptions. We had three meetings concerning the pseudocode before we actually wrote any code.  Yet our implementation benefited as the coding proccess was straightforward once all of us were aligned.


## Other member(s)

### Stefanie Moreno


While this assignment was not exceptionally challenging, it was an
important lesson in parsing and interpreting VCF files with Python, and
upon running our code with the VCF file and receiving the results we
were hoping to see, it was very rewarding. I learned how to identify the
rarity of a gene variant and how to extract the diseases associated with
variants having an AF\_EXAC frequency of less than 0.01% and calculate
how often these diseases occurred. It was interesting to see how small
formatting differences in genomic data can so significantly impact
parsing workflows. The highly structured format of a VCF file is
essential for accurate retrieval of information from such a dense
datasource. Upon learning about all the varieties of information that
can be held inside a VCF file and how the organization and formatting
structure can even allow for nonspecified entries and their proper
retrieval, I was actually amazed. Ultimately, this project reinforced
for me the critical importance of file structure- down to a single
keystroke, or where to input “MISSING” versus “.” or nothing at all- and
if not input properly, that data is completely worthless.

### Victoria Van Berlo

This project was excellent for getting back into Python, and an introduction to developing algorithms as a group. It also provided valuable experience with getting aquainted with Git. This project provided an excellent refresher for data types and data structures, as well as file parsing and collecting data of interest. Developing the pseudocode as a group allowed us to create code that followed the same general flow, yet allowed for each of us to put own our spin on things. When we met back together to finalize the code, we had several different methods for some of the steps that we were able to choose the best implementation and do a bit of peer review to gain insight into each other's thought processes.

The biggest challenge for this project was analyzing the input file to determine the best methods for parsing, as there were some tricky cases regarding delimiters, and proper order for narrowing down our search results. Our strengths in this project were our varied backgrounds and levels of experitise with both programming and biology, which allowed us many different ideas of how best to proceed at each step. Our internal peer review process really shined due to this aspect.

# Generative AI Appendix

Generative AI was not used for this assignment.

# References

GA4GH. (2024, 9 Oct). *The variant call format specification: VCFv4.3
and BCFv2.2*. Large Scale Genomics work stream of the Global Alliance
for Genomics & Health. Retrieved on Jan 23, 2026, from
<https://samtools.github.io/hts-specs/VCFv4.3.pdf>

Harrison, S. M., Biesecker, L. G., Rehm, H. L. (2019). Overview of
specifications to the ACMG/AMP variant interpretation guidelines. *Curr
Protoc Hum Genet.*, 103(1):e93. <https://doi.org/10.1002/cphg.93>

NIH. (n.d.). *What is ClinVar?* NIH National Library of Medicine.
Retrieved on Jan 20, 2026, from
<https://www.ncbi.nlm.nih.gov/clinvar/intro/>
