"""
Dictionary in Python holds data items in key-value pairs.
Items in a dictionary are enclosed in curly brackets { }.
Dictionaries permit faster access to data. 
Every key is separated from its value using a colon (:) sign. 
The key : value pairs of a dictionary can be accessed using the key.
The keys are usually strings and their values can be any data type. 
In order to access any value in the dictionary, we have to specify its key in square brackets [ ].
"""
# Create a dictionary
Dict1 = {"Fruit" : "Apple", "Climate" : "Cold", "Price" : 48}
# Print dictionary
print(Dict1)
#Print Price of Apple using Price keys
print("Price of Apple is", Dict1["Price"])

months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
print(months)
print("September is months number", months["Sep"])

month_days = {"Jan" : 31, "Feb" : 28, "Mar" : 31, "Apr" : 30, "May" : 31, "Jun" : 30, "Jul" : 31, "Aug" : 31, "Sep" : 30, "Oct" : 31, "Nov" : 30, "Dec" : 31}
print(month_days)
print("Number of days in month of September is", month_days["Sep"] )