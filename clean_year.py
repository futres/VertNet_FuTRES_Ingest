"""
Functions for cleaning the yearCollected data in the VertNet dataset

"""

date_filter = """IV|0000|September|<|NW|latter|unknown|(MCZ)|(MSU)|present|
                 and|;|&|mainly|between|Between|BETWEEN|OR|Unknown|UNKNOWN|
                 #|TO|\?|\'|----|19--|No Date|\,|\d{4}-\d{4}|(/n) /d|\d{4}[s]|
                 \d{4}\'[S]|1075-07-29|975-07-17|2088|9999|0201|1197|
                 1260|4560|1024|1119|1192|1072|1186|2364"""

def year_search(year):
    """
    Search string for 4 digit number and pass to correct function

    """
    if (re.search(r'\d{4}$', year)):
        return year_cleaner_front(year)
    elif (re.search(r'^\d{4}', year)):
        return year_cleaner_back(year)

def year_cleaner_front(year):
    """
    Isolate the year at the beginning of the string

    """
    cleaned_year = year[len(year)-4:len(year)]
    return cleaned_year

def year_cleaner_back(year):
    """
    Isolate the year at the end of the string

    """
    cleaned_year = year[0:4]
    return cleaned_year

def clean_year_collected(data):
    """
    Clean yearCollected column

    """

    # Filling N/As with "Unknown"
    data["eventdate"] = data["eventdate"].fillna("Unknown")

    # Create yearCollected Column
    data = data.assign(yearCollected = '')

    # Creating event date variable
    verbatim_date = data['eventdate']

    # Establishing vertnet filter
    vertnet_date_filter = verbatim_date.str.contains(date_filter)

    # Grabbing clean data
    verbatim_date_clean= verbatim_date[vertnet_date_filter==False]

    # Cleaning year data
    data["yearCollected"] = verbatim_date_clean.apply(year_search)
    data["yearCollected"] = data["yearCollected"].fillna("Unknown")

    return data