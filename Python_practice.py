type(73.81)
type(True)
#print(type('True'))
value = 5 + (9 * 3 / (2 - 4))

counties = ["Arapahoe","Denver","Jefferson"]

#INDEX: Starts at 0; first item is always 0
#   Last item index expressed as: 1 less than the # of items in the list
#print(counties [-1])
#LEN: To get the total number of items in a list, we use the len() function and 
# then add the list inside the parentheses,like this: len(counties). 
#print (len(counties))

#Slide Lists: Slicing list is used to get specific items from a list
# Official is  list[start : end]; 
#   "Start": refers to the index of the first item in the slice 
#   "End": The index marking the end of the slice
#   Returns a list containing items from the list from starting index value up to BUT NOT INCLUDING THE ENDING VALUE 
#print(counties[1:3])

#ADDING ITEMS TO A LIST: Items (int, floats, str, or any other datatype/structure)
#can be added by using the append() function and the syntax list.append()
#   function will always list the new item at the end of list
#   to specify where in the list to add the new item, select the location with an index
#    by using the syntax, list.insert(index, obj).
#counties.append("El Paso")
#counties.insert(2,"El Paso")
#counties.remove("El Paso") * pop() method also removes the item at a given index
#counties.pop(-1)
#counties.pop(3)

#CHANGE an element in a List 
# syntax to change an item in a list: list[index] = "New Value"
#counties[2] = "El Paso"

#counties.insert(1,"El Paso")
#counties.pop(0)
#counties[2] = "Denver"
#counties[1] = "Jefferson"
#counties.append("Arapahoe")

#Tuple: A "list" that can't be manupulated/changed 
#    Syntax: my_tuple = () or also as a method my_tuple = tuple()

#counties_tuple = ("Arapahoe","Denver","Jefferson")

#DICTIONATY = During the data analysis process, you may be given a dictionary and have to 
# retrieve data from the dictionary.
#   syntax:my_dictionary = {}; 
#   Or create a dictionary with the built-in Python dict() method, my_dictionary = dict().
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
#len(counties_dict) #similar to lists and tuples
#se the items() method return a list of tuples where the first element in each tuple is 
#the key of the dictionary, and the second element in each tuple is the value corresponding to that key.
#   sample syntax = counties_dict.items()
#   sample sintax for Keys = counties_dict.keys()
#   sample sintax for values = counties_dict.values() or counties_dict.get() for a specific value
#       counties_dict['Arapahoe']
#       counties_dict[('Arapahoe')]
#       counties_dict.get('Arapahoe')

#LIST OF DICTIONARIES
#   syntax: [{key1:value1, key2:value2}, {key1:value3, key2:value4}]
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})

#print(voting_data)

#voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
#voting_data.remove({"county":"Arapahoe","registered_voters":422829})
#voting_data[2] = ({"county":"Denver","registered_voters":463353})
#voting_data[1] = ({"county":"Jefferson","registered_voters":432438})
#voting_data.append({"county":"Arapahoe","registered_voters":422829})

#DECISION/IF Statements 
#   general format for "if" statements 
#   if condition:
#       statement 1
#       statement 2

#IF STATEMENT SAMPLES

#if "Arapahoe" in counties: 
#    print("True")
#else:
#    print("False")

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#Checking for BOTH items to be there 
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#Checking for either item to be in the list
#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")

#Checking for items and using "NOT IN"
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#LOOPS 

# For loops
#for county in counties:# When we execute this code, 
                       # the county variable is declared and set equal to the first item in the list of counties
#    print(county)

#Indexing can also be used to iterate through a list. 
#If the list contains strings, we’ll need to get the length of the list as an integer for the range() function.
#   for i in range(len(counties)): #" i " indicates index
#       print(counties[i])

#Using the dictionary declared above to get the KEYS 
#for county in counties_dict:
#    print(county)

#Using the "key" method will always print keys in order 
#for county in counties_dict.keys():
#    print(county)

#Get the Values of a Dictionary
#for voters in counties_dict.values():
#    print(voters)
#  can also use the format dictionary_name[key] to get the value for the key.
#for county in counties_dict:
#    print(counties_dict[county])
# Can also use the "get" value 
#for county in counties_dict:
#    print(counties_dict.get(county))

#Get the Key-Value Pairs of a Dictionary
#for key, value in dictionary_name.items():
#    print(key, value)
#for county, voters in counties_dict.items():
#    print(county, voters)

#To get items in a dictionary (keys or values)
#for county_dict in voting_data:
#     print(county_dict['registered_voters'])

#for county_dict in voting_data:
#    print(county_dict['county'])

#Using a nested loop to retrieve only the values from each dictionary
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

#F-strings: Formatted String Literals
#   From this 
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#   To This 
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")


#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")

for county_dict in voting_data:
    for county, voters in county_dict.items():
        print(f'{county_dict[county]} county has {county_dict["registered_voters"]} registered voters.')












