"""
Data Wrangling Script for VertNet Mammal Data

Neeka Sewnath
nsewnath@ufl.edu

"""

#===========================================================================================================================================

import pandas as pd
import argparse

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
                        default = "./../fovt-data-mapping/Original_Data/all_mammals_2021-11-09a/all_mammals_2021-11-09a.csv")

    return parser.parse_args()

#===========================================================================================================================================

def main():

    # Fetch arguments 
    args = get_args()
    file = args.file

    # Read input file 
    print("\nReading in data...")
    data = pd.read_csv(file)

    # Data Processing Steps
    print("\nAssigning individualID...")
    data = id_assign.assign_indivdual_ID(data)

    print("\nCleaning yearCollected column...")
    data = clean_year.clean_year_collected(data)

    print("\nCleaning lifeStage column...")
    data = clean_lifestage.clean_lifestage_column(data)

    print("\nCleaning sex column...")
    data = clean_sex.clean_sex_column(data)

    print("\nCleaning scientificName column...")
    data = process_na.fill_unknown(data)

    print("\nAdding GEOME required column...")
    data = add_cols.add_req_cols(data)

    print("\nAdding verbatimEventDate column...")
    data = add_cols.adding_verbatim_date(data)

    print("\nCleaning country column...")
    data = clean_country.clean_country(data)

    print("\nCreating verbatimElevation columns...")
    data = add_cols.verbatim_elev(data)

    print("\nMatching column names with template names...")
    data = rename.match_cols(data)

    print("\nCreating materialSampleID...")
    data = id_assign.create_id(data)

    print("\nCreating unique measurementMethod column...")
    data = m_method_process.create_uni_mm(data)

    print("\nCreating long version...")
    data = rearrange.long_vers(data)

    print("\nProcessing measurement method...")
    data = m_method_process.mm_processing(data)

    print("\nMatching trait and ontology terms...")
    data = rename.match_traits(data)

    print("\nCreate verbatimMeasurementUnit column...")
    data = add_cols.verbatim_mu(data)

    print("\nCreating diagnosticID column...")
    data = id_assign.diagnostic_id(data)

    print("\nDrop blank measurements...")
    data = process_na.drop_na(data)

    # Saving files
    print("\n Saving files...")
    save_file.save_file(data)
    
#===========================================================================================================================================

if __name__ == '__main__':
    main()