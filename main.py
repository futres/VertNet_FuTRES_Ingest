"""
Data Wrangling Script for VertNet Mammal Data

Neeka Sewnath
nsewnath@ufl.edu

"""

#===========================================================================================================================================

import pandas as pd
import argparse 
import numpy as np
import multiprocessing
import re
import uuid 

import id_assign
import clean_year
import clean_country
import process_na
import m_method_process
import rename
import rearrange
import clean_lifestage
import clean_sex
import add_cols
import save_file

#===========================================================================================================================================

try:
    import warnings
    warnings.filterwarnings('ignore')
except:
    pass

#===========================================================================================================================================

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='API data scrape and reformat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help = 'File input',
                        metavar = 'url',
                        type = str,
                        default = "./../Original_Data/all_mammals_2021-11-09a/all_mammals_2021-11-09a.csv")

    parser.add_argument('-o',
                        '--output',
                        help = 'Output file name',
                        metavar = 'output',
                        type = str)

    return parser.parse_args()

#===========================================================================================================================================

def main():

    # Fetch arguments 
    args = get_args()
    file = args.file

    # Read input file 
    print("\n Reading in data...")
    data = pd.read_csv(file)

    # Data Processing Steps
    print("\n Assigning individualID...")
    data = id_assign.assign_indivdual_ID(data)

    print("\n Cleaning yearCollected column...")
    data = clean_year.clean_year_collected(data)

    print("\n Cleaning lifeStage column...")
    data = clean_lifestage.clean_lifestage_column(data)

    print("\n Cleaning sex column...")
    data = clean_sex.clean_sex_column(data)

    print("\n Cleaning scientificName column...")
    data = process_na.fill_unknown(data)

    print("\n Adding GEOME required column...")
    data = add_cols.add_req_cols(data)

    print("\n Adding verbatimEventDate column...")
    data = add_cols.adding_verbatim_date(data)

    print("\n Cleaning country column...")
    data = clean_country.clean_country(data)

    print("\n Creating verbatimElevation columns...")
    data = add_cols.verbatim_elev(data)

    print("\n Matching column names with template names...")
    data = rename.match_cols(data)

    print("\n Creating materialSampleID...")
    data = id_assign.create_id(data)

    print("\n Creating unique measurementMethod column...")
    data = m_method_process.create_uni_mm(data)

    print("\n Creating long version...")
    data = rearrange.long_vers(data)

    print("\n Processing measurement method...")
    data = m_method_process.mm_processing(data)

    print("\n Matching trait and ontology terms...")
    data = rename.match_traits(data)

    print("\n Create verbatimMeasurementUnit column...")
    data = add_cols.verbatim_mu(data)

    print("\n Creating diagnosticID column...")
    data = id_assign.diagnostic_id(data)

    print("\n Drop blank measurements...")
    data = process_na.drop_na(data)

    # Saving files
    print("\n Saving files...")
    data = save_file.save_file(data)
    
#===========================================================================================================================================

if __name__ == '__main__':
    main()