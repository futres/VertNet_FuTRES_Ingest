"""
Functions to clean country column for VertNet Mammal data 

"""
#===========================================================================================================================================

import pandas as pd

#===========================================================================================================================================

# Common country names that need to be mapped in VertNet data

country_mapping_file = pd.read_csv("files/country_mapping_file.csv")

country_dict = country_mapping_file.set_index('country_old').to_dict()

#===========================================================================================================================================

def country_correction(country): 
    """Corrects country column to geome specific country list"""

    # Read GEOME country list
    geome_countries = pd.read_csv("./../fovt-data-mapping/Mapping Files/geome_country_list.csv")

    if country in geome_countries.values:
        return country
    elif country in country_dict.keys():
        return country_dict[country]
    else:
        country = "Unknown"
        return country 

def clean_country(data):
    """
    Cleaning country column 
    
    """
    # Append countries to verbatim locality column
    data["verbatimLocality"] = data["locality"] + "," + data["country"]

    # Clean country names
    data['country'] = data['country'].apply(country_correction)

    return data