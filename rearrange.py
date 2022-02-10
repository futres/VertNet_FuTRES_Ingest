"""
Various functions for rearranging data in VertNet Mammal data

"""

desired_columns = ['catalognumber','collectioncode','decimallatitude','individualID',
                  'decimallongitude', 'verbatimElevation', 'maximumelevationinmeters',
                  'minimumelevationinmeters','institutioncode','verbatimEventDate',
                  'occurrenceremarks','occurrenceid','verbatimlongitude',
                  'verbatimlatitude', 'verbatimLocality', 'samplingProtocol',
                  'sex', 'country', 'lifestage_cor', 'binomial', 'basisOfRecord',
                  'yearCollected', 'body_mass.value','body_mass.units',
                  'ear_length.value', 'ear_length.units','hind_foot_length.value',
                  'hind_foot_length.units', 'tail_length.value','tail_length.units',
                  'total_length.value', 'total_length.units','body_mass.units_inferred',
                  'ear_length.units_inferred', 'hind_foot_length.units_inferred',
                  'tail_length.units_inferred','total_length.units_inferred',
                  'body_mass.estimated_value','ear_length.estimated_value',
                  'hind_foot_length.estimated_value','tail_length.estimated_value',
                  'total_length.estimated_value']

def col_rearrange(data):
    """
    Rearrange columns so that template columns are first, followed by measurement values

    """

    # Create column list
    cols = data.columns.tolist()

    # Specify desired columns
    cols = desired_columns

    # Subset dataframe
    data = data[cols]

    return data 

def long_vers(data):
    """
    Creating long version, first specifiying keep variables, then naming type and value
    
    """

    melt_cols = ['catalogNumber', 'collectionCode', 'decimalLatitude','decimalLongitude',
                'verbatimElevation','yearCollected','basisOfRecord','verbatimEventDate',
                'institutionCode','lifeStage','verbatimLocality','locality', 'individualID',
                'samplingProtocol','sex','scientificName', 'occurrenceRemarks','country',
                'occurrenceID', 'verbatimLongitude', 'verbatimLatitude','materialSampleID','eventID',
                'maximumElevationInMeters', 'minimumElevationInMeters',]

    melt_cols = melt_cols + method_list

    longVers  = pd.melt(data,id_vars = melt_cols, var_name = 'measurementType', value_name = 'measurementValue')

    return longVers