"""
Function to chunk and write data subsets for Vertnet Mammal data specifically for ingestion

"""
import numpy as np

def save_file(data):
    # Create chunks list
    chunks = []

    # Separating files into chunks
    chunks = np.array_split(data, 13)

    for i in range(len(chunks)):
        new=i+1
        chunks[i].to_csv('../Mapped_Data/FuTRES_Mammals_VertNet_Global_Modern_'+ str(new) +'.csv', index=False)
        print("mapped_data",i, " done")

        