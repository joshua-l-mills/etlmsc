import json
import requests

#function for getting user inputs
def start():

    #get user input for start and end date
    #startdate = input("Enter start date(no earlier than 1763-03-01):")
    #enddate = input("Enter end date(no later than <placeholder>2022-12-15):")

    #base url for API endpoint
    URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"

    #header containing the token for accessing the data
    header = {"token" : "RhhaeJTRaRmdchTnEzMxvwwoLVqzqXtt"}
    #parameters for accessing data
    param = {
    "startdate":"2010-01-01",
    "enddate":"2010-01-31",
    "datatypeid":"PRCP",
    "datasetid":"GHCND",
    "limit":"10",
    "units":"metric"
    }
    
    #make API request
    resp = requests.get(URL, headers = header,params=param)

    jsonResp = resp.json()

    count = jsonResp["metadata"]["resultset"]["count"]
    print("Selection contains {ct} records.".format(ct=count))
    


#the actual main function
if __name__ == "__main__":
    print("This program is for gathering daily precipitation data summaries.")
    start()
