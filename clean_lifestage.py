"""
Function to clean lifestage column in Vertnet Mammal Data

"""

def clean_lifestage_column(data):
    """
    Clean lifestage column 

    """
    # Fill in NA
    data["lifestage_cor"] = data['lifestage_cor'].fillna("Not Collected")

    # Create Filters
    adult = data['lifestage_cor'] == "Adult"
    juvenile = data['lifestage_cor'] == "Juvenile"
    ns = data['lifestage_cor'] == "NS"

    # Assign correct terms using filters
    data['lifestage_cor'][adult] = "adult"
    data['lifestage_cor'][juvenile] = "juvenile"
    data['lifestage_cor'][ns] = "Not Collected"

    return data 