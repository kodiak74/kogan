## Response to Coding Challenge

### The Challenge


Using the provided (paginated) API, find the average cubic weight for all products in the "Air Conditioners" category.

Cubic weight is calculated by multiplying the length, height and width of the parcel. The result is then multiplied by the industry standard cubic weight conversion factor of 250.

API Endpoint
http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com/api/products/1
Cubic Weight Example
A parcel measuring 40cm long (0.4m) x 20cm high (0.2m) x 30cm wide (0.3m) is equal to 0.024 cubic metres.
Multiplied by the conversion factor of 250 gives a cubic weight of 6kg.

0.4m x 0.2m x 0.3m = 0.024m3
0.024m3 x 250 = 6kg
Assume that
All dimensions are provided in centimetres.
All weights are provided in grams.


### Running

The solution is written in Python, targeting version 3.7.3. It should not require the installation of any modules as only the standard Python modules are used.



```
# To run solution with default category (Air Conditioners)
$ python3 main.py

# To run solution with custom category  
$ python3 main.py -c <category> 

# To perform simple test validation: 
$ python3 main.py -t 

# And to get the usuage:
$ python3 main.py -h

```