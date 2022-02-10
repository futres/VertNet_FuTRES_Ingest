"""
Functions for adding basic (required and nonrequired) columns in Vertnet Mammal data

"""

def add_req_cols(data):
    """
    Add required GEOME columns
    
    """

    data["samplingProtocol"] = "Unknown"
    data["basisOfRecord"] = "PreservedSpecimen"
    data["locality"] = "Unknown"

    return data 

def adding_verbatim_date(data):
    """
    Adding verbatimEventDate column to dataframe

    """

    data['verbatimEventDate'] = data['verbatimeventdate']

    return data

def verbatim_elev(data):
    """
    Create verbatimElevation columns

    """
    string_max = data["maximumelevationinmeters"].astype(str)
    string_min = data["minimumelevationinmeters"].astype(str)
    data['verbatimElevation'] = string_max + "," + string_min

    return data

def verbatim_mu(data):
    data = data.assign(verbatimMeasurementUnit = "")
    data[['measurementValue', 'verbatimMeasurementUnit']] = data['measurementValue'].str.split(';', expand=True)

    return data
