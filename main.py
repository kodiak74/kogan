import urllib.request
import json
import sys, getopt
 
import random

BASE_URL = "http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com"
INITIAL_PATH = "/api/products/1"
DEFAULT_CATEGORY = "Air Conditioners"

def fetchData(path=None):
    if (path is None): 
        return None
    try:
        url = BASE_URL + path
        response = urllib.request.urlopen(url = url ).read() 
    except (urllib.error.URLError) as ex:
        #Dont care about the type of error - at this point
        print("Oops!",ex,"occured.")
        return None
    return json.loads(response) 


def calcCubic(record):
    size = record["size"]
    return (size["width"] * size["length"] * size["height"]) * 250


# Validate calculation function
def testCubicCalc():
    record = {
        "size": {
            "width": 5,
            "length": 4,
            "height": 3
            }
    }
    expected = 15000
    result = calcCubic(record)
    print ("Calculating cubic for:")
    print(record)
    print("Expecting %s - calculated: %s" % (expected, result))
    if (result != expected):
        print ("Failed")
    print ("Passed")  
    


def main(argv):

   try:
      opts, args = getopt.getopt(argv,"ct")
   except getopt.GetoptError:
      print ('Usuage: ')
      print ('Runs with default category (Air Conditioners): python3 main.py  ')
      print ('Runs with custom category: python3 main.py -c <category> ')
      print ('Perform simple test validation: python3 main.py -t ')
      sys.exit(2)

   category = DEFAULT_CATEGORY
   for opt, arg in opts:
        if (opt == '-c' ):
                category = arg 
        elif (opt  == '-t' ):
            testCubicCalc()
            return

  

   print("Retrieving data...")

  
   category_data = []

   path = INITIAL_PATH
   while path is not None:
       response = fetchData(path)
       if (response is None):
           print("There appears to be a problem fetching %s" % path)
       print("  - processing results for %s" % path)    
       path = response["next"]
       # print("  next path: %s" % path)
      
       for record in response["objects"]:
           if (record["category"] == category):
               category_data.append(record)

    
  

   count = 0
   tally = 0
   for record in category_data:
       tally = tally + calcCubic(record)
       count += 1

   if (count > 0): 
        avg = tally / count 
   
   print("Found %s items for the category: %s" % (count, category))
   print("Average cubic weight: %s" % avg)  


if __name__ == "__main__":
    main(sys.argv[1:])