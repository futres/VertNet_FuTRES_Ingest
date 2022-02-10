"""
Functions to process measurementMethod in VertNet Mammal data

"""

import numpy as np

def trait_method(trait, data):
    """
    Adds measurementMethod information based off of "True" values in inferred value
    and estimated value columns
    """
    
    column = "measurementMethod_" + trait
    
    inferred_column = trait + ".units_inferred"
    estimated_column = trait + ".estimated_value"
    
    inferred_filter = data[inferred_column].astype(str).str.contains("TRUE|True|true")
    estimated_filter = data[estimated_column].astype(str).str.contains("TRUE|True|true")
    
    data[column][inferred_filter] = "Extracted with Traiter ; inferred value"
    data[column][estimated_filter] = "Extracted with Traiter ; estimated value"
    data[column][estimated_filter & inferred_filter] = "Extracted with Traiter ; estimated value; inferred value"

def create_uni_mm(data):
    """
    Creates a unique measurementMethod column for each desired trait
    """
    # List of desired traits
    trait_name_list = ["body_mass","ear_length","hind_foot_length",
                    "tail_length","total_length"]

    method_list = ["measurementMethod_" + x for x in trait_name_list]
    data = data.join(pd.DataFrame(index = data.index, columns= method_list))

    [trait_method(x, data) for x in trait_name_list]

    data = data.drop(columns = ['body_mass.units_inferred',
                'ear_length.units_inferred',
                'hind_foot_length.units_inferred',
                'tail_length.units_inferred',
                'total_length.units_inferred',
                'body_mass.estimated_value',
                'ear_length.estimated_value',
                'hind_foot_length.estimated_value',
                'tail_length.estimated_value',
                'total_length.estimated_value'])

    # Add filler to units column
    data["body_mass.units"]= data["body_mass.units"].fillna("unknown")
    data["ear_length.units"] = data["ear_length.units"].fillna("unknown")
    data["hind_foot_length.units"] = data["hind_foot_length.units"].fillna("unknown")
    data["tail_length.units"] = data["tail_length.units"].fillna("unknown")
    data["total_length.units"] = data["total_length.units"].fillna("unknown")

    data["body_mass.value"] = data["body_mass.value"].fillna("unknown")
    data["ear_length.value"] = data["ear_length.value"].fillna("unknown")
    data["hind_foot_length.value"] = data["hind_foot_length.value"].fillna("unknown")
    data["tail_length.value"] =  data["tail_length.value"].fillna("unknown")
    data["total_length.value"] = data["total_length.value"].fillna("unknown")

    data["body_mass_temp"] = data["body_mass.value"].astype(str) +" ; "+ data["body_mass.units"]
    data["ear_length_temp"] = data["ear_length.value"].astype(str) + " ; "+data["ear_length.units"]
    data["hind_foot_length_temp"] = data["hind_foot_length.value"].astype(str) + " ; " + data["hind_foot_length.units"]
    data["tail_length_temp"] = data["tail_length.value"].astype(str) + " ; " + data["tail_length.units"]
    data["total_length_temp"] = data["total_length.value"].astype(str) + " ; " + data["total_length.units"]

    data = data.drop(columns = ['body_mass.value',
                    'ear_length.value',
                    'hind_foot_length.value',
                    'tail_length.value',
                    'total_length.value',
                    'body_mass.units',
                    'ear_length.units',
                    'hind_foot_length.units',
                    'tail_length.units',
                    'total_length.units'])


def method_add(trait,ind):
    if trait == "body_mass_temp":
        return longVers["measurementMethod_body_mass"][ind]
    elif trait == "ear_length_temp":
        return longVers["measurementMethod_ear_length"][ind]
    elif trait == "hind_foot_length_temp":
        return longVers["measurementMethod_hind_foot_length"][ind]
    elif trait == "tail_length_temp":
        return longVers["measurementMethod_tail_length"][ind]
    elif trait == "total_length_temp":
        return longVers["measurementMethod_total_length"][ind]

def mm_processing(data):
    """
    Pull corresponding column value in measurement_method etc and append it to offical measurementMethod
    
    """
    data = data.assign(measurementMethod = "")

    data['ind'] = np.arange(len(data))

    data['measurementMethod'] = data.apply(lambda x: method_add(x.measurementType, x.ind), axis=1)

    data['measurementMethod'] = data['measurementMethod'].fillna("Extracted with Traiter")

    data = data.drop(columns = method_list)
    data = data.drop(columns = 'ind')

    return data