"""
Functions for assigning IDs within VertNet processing Script

"""

def assign_indivdual_ID(data):
    """
    Add individualID and populate with UUID
    
    """
    data = data.assign(individualID = '')
    data['individualID'] = [uuid.uuid4().hex for _ in range(len(data.index))]

    return data

def create_id(data):
    """
    Create materialSampleID which is a UUID for each measurement, 
    Create eventID and populate it with materialSampleID
    
    """

    data['materialSampleID'] = [uuid.uuid4().hex for _ in range(len(data.index))]
    data["eventID"] = data['materialSampleID']

    return data

def diagnostic_id(data):
    """
    Create diagnosticID which is a unique number for each measurement
    """
    
    data['diagnosticID'] = np.arange(len(data))

    return data