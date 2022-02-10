"""
Functions to clean country column for VertNet Mammal data 

"""
import pandas as pd

# TODO: Turn into mapping file 
country_dictionary = {"United States":"USA", "U S A":"USA", 
                      "Philippine Islands":"Philippines",
                      "Indonesia; Borneo":"Indonesia",
                      "Malaysia; Malaya":"Malaysia",
                      "U.S. Virgin Islands":"Virgin Islands",
                      "Republic of South Africa":"South Africa",
                      "Ivory Coast":"Cote d'Ivoire",
                      "Federated States of Micronesia":"Micronesia",
                      "Lesser Antilles; Grenada":"Grenada",
                      "Indonesia; Java":"Indonesia",
                      "Lesser Antilles; Saint Vincent":"Saint Vincent and the Grenadines",
                      "Lesser Antilles; Barbados":"Barbados",
                      "ST VINCENT":"Saint Vincent and the Grenadines",
                      "Lesser Antilles; Montserrat": "Montserrat",
                      "Indonesia; Sumatra":"Indonesia",
                      "Virgin Islands, US":"Virgin Islands",
                      "Lesser Antilles; Antigua":"Antigua and Barbuda",
                      "England":"United Kingdom",
                      "Republic of Trinidad and Tobago":"Trinidad and Tobago",
                      "Trinidad And Tobago; Trinidad":"Trinidad and Tobago",
                      "COMMONWEALTH OF THE NORTHERN MARIANA ISLANDS":"Northern Mariana Islands",
                      "Congo":"Democratic Republic of the Congo",
                      "Malaysia; Sabah":"Malaysia",
                      "Lesser Antilles; Martinique":"Martinique",
                      "Republic of the Marshall Islands":"Marshall Islands",
                      "Commonwealth of the Bahamas":"Bahamas",
                      "Trinidad & Tabago":"Trinidad and Tobago",
                      "United Kingdom; England":"United Kingdom",
                      "United Kingdom; Scotland":"United Kingdom",
                      "United Kingdom; Wales":"United Kingdom",
                      "Lesser Antilles; Dominica":"Dominica",
                      "Papua, New Guinea":"Papua New Guinea",
                      "People's Republic of China":"China",
                      "SCOTLAND":"United Kingdom"}


def country_correction(country): 
    """Corrects country column to geome specific country list"""

    # Read GEOME country list
    geome_countries = pd.read_csv("./../Mapping Files/geome_country_list.csv")

    if country in geome_countries.values:
        return country
    elif country in country_dictionary.keys():
        return country_dictionary[country]
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