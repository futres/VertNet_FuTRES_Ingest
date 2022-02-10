"""
Various functions for renaming in Vertnet Mammal data

"""

rename_dict = {'catalognumber': 'catalogNumber',
               'collectioncode':'collectionCode',
               'decimallatitude':'decimalLatitude',
               'decimallongitude':'decimalLongitude',
               'institutioncode' :'institutionCode',
               'occurrenceremarks':'occurrenceRemarks',
               'maximumelevationinmeters':'maximumElevationInMeters',
               'minimumelevationinmeters':'minimumElevationInMeters',
               'occurrenceid':'occurrenceID',
               'verbatimlongitude':'verbatimLongitude',
               'verbatimlatitude':'verbatimLatitude',
               'lifestage_cor':'lifeStage',
               'binomial':'scientificName'}

# Create trait dictionary 
trait_dict = {'body_mass_temp':'body mass',
            'ear_length_temp': 'ear length to notch',
            'hind_foot_length_temp':'pes length',
            'tail_length_temp':'tail length',
            'total_length_temp':'body length'}

def match_cols(data):
    """
    Matching template and column terms

    """
    
    data = data.rename(rename_dict)

    return data


def trait_rename(trait): 
    """
    Renames trait names with trait dictionary
    """
    
    if trait in trait_dict.keys():
        return trait_dict[trait]

def match_traits(data):

    data['measurementType'] = data['measurementType'].apply(trait_rename)

    return data 
