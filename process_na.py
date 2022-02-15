"""
Functions to handle various NA columns in VertNet Mammal data processing

"""

#===========================================================================================================================================

def fill_unknown(data):
    """
    Fill scientificName data with "unknown"

    """
    data["binomial"] = data["binomial"].fillna("Unknown")

    return data 

def drop_na(data):

    #Drop N/A
    data["verbatimMeasurementUnit"] = data["verbatimMeasurementUnit"].replace({"unknown":""})

    #Drop Range Values and unknowns
    range_value_filter=data['measurementValue'].str.contains(",|one|unknown", na=False)
    data['measurementValue'][range_value_filter] = float("nan")
    data = data.dropna(subset=['measurementValue'])

    return data