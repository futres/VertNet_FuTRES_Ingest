"""
Function to clean sex column in VertNet Mammal data

"""

def clean_sex_column(data):
    """
    Clean sex column
    
    """

    female = data['sex'] == "female"
    male = data['sex'] == "male"
    data['sex'][(female == False) & (male == False)] = ""

    return data