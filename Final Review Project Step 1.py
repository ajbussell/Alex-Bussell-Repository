print("Alex Bussell's Code...")
import pandas

# Read in Raw Data from File Provided in Canvas:
rawRentalsDF = pandas.read_csv("rentalsYearEndLast5YearsUSE.csv")
print(rawRentalsDF)

# Clean this data by dropping any row with missing values:
rentalsCleanedDF = rawRentalsDF.dropna()
print("\nCleaned data:")
print(rentalsCleanedDF)

# Extract Needed Columns from Cleaned Data
print("\nExtract Needed Columns:")
rentalsCleanDF = rentalsCleanedDF.iloc[:, [5, 9, 10, 11, 12, 13]]
print(rentalsCleanDF)

# ========= Your FIRST Selected State (example: WI)
selectedState = "DE"

# Select the "State" column for use in selecting a state's data:
stateColumn = rentalsCleanDF["State"]
print(stateColumn)

# Create the criteria for selecting only the rows for the selected state:
stateCriteria = (rentalsCleanDF["State"] == selectedState)
print("\n", selectedState, "data:")
print(stateCriteria)

# Use this criteria for selecting only the rows for the selected state:
selectedStateDF = rentalsCleanDF[stateCriteria]
print("\nSelected State Data:")
print(selectedStateDF)

# Round Data to 2 decimal places:
print("\nRounded:")
selectedStateRoundedDF = selectedStateDF.round(2)
print(selectedStateRoundedDF)

# Write this state's data to its own file:
selectedStateRoundedDF.to_csv(selectedState + "data.csv", mode = "w")   # w = "write"

# Write this state's data also to a file combining the 4 states' data:
outputFileName = "rentalsSelectedStates.csv"
selectedStateDF.to_csv(outputFileName)   # w = "write"

# ========= Your SECOND Selected State (example: CA)
# ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐ 
# Select your SECOND state (e.g., CA) :  
selectedState = "NM"

# Select the "State" column for use in selecting a state's data:
stateColumn = rentalsCleanDF["State"]
print(stateColumn)

# Create the criteria for selecting only the rows for the selected state:
stateCriteria = (rentalsCleanDF["State"] == selectedState)
print("\n", selectedState, "data:")
print(stateCriteria)

# Use this criteria for selecting only the rows for the selected state:
selectedStateDF = rentalsCleanDF[stateCriteria]
print("\nSelected State Data:")
print(selectedStateDF)

# Round Data to 2 decimal places:
print("\nRounded:")
selectedStateRoundedDF = selectedStateDF.round(2)
print(selectedStateRoundedDF)

# Write this state's data to its own file:
selectedStateRoundedDF.to_csv(selectedState + "data.csv", mode = "w")   # w = "write"

# Write this state's data also to a file combining the 4 states' data:
# mode = "a"  will APPEND to the file,
# header = False leaves off the column headings for this state,
# since these headings were already written when the first state
# was written into this file.
selectedStateDF.to_csv(outputFileName, mode = "a", header = False)

# ========= Your THIRD Selected State (example: AL)
selectedState = "PA"

# Select the "State" column for use in selecting a state's data:
stateColumn = rentalsCleanDF["State"]
print(stateColumn)

# Create the criteria for selecting only the rows for the selected state:
stateCriteria = (rentalsCleanDF["State"] == selectedState)
print("\n", selectedState, "data:")
print(stateCriteria)

# Use this criteria for selecting only the rows for the selected state:
selectedStateDF = rentalsCleanDF[stateCriteria]
print("\nSelected State Data:")
print(selectedStateDF)

# Round Data to 2 decimal places:
print("\nRounded:")
selectedStateRoundedDF = selectedStateDF.round(2)
print(selectedStateRoundedDF)

# Write this state's data to its own file:
selectedStateRoundedDF.to_csv(selectedState + "data.csv", mode = "w")   # w = "write"

# Write this state's data also to a file combining the 4 states' data:
# mode = "a"  will APPEND to the file,
# header = False leaves off the column headings for this state,
# since these headings were already written when the first state
# was written into this file.
selectedStateDF.to_csv(outputFileName, mode = "a", header = False)

# ========= Your FOURTH Selected State (example: SC)
selectedState = "CA"

# Select the "State" column for use in selecting a state's data:
stateColumn = rentalsCleanDF["State"]
print(stateColumn)

# Create the criteria for selecting only the rows for the selected state:
stateCriteria = (rentalsCleanDF["State"] == selectedState)
print("\n", selectedState, "data:")
print(stateCriteria)

# Use this criteria for selecting only the rows for the selected state:
selectedStateDF = rentalsCleanDF[stateCriteria]
print("\nSelected State Data:")
print(selectedStateDF)

# Round Data to 2 decimal places:
print("\nRounded:")
selectedStateRoundedDF = selectedStateDF.round(2)
print(selectedStateRoundedDF)

# Write this state's data to its own file:
selectedStateRoundedDF.to_csv(selectedState + "data.csv", mode = "w")   # w = "write"

# Write this state's data also to a file combining the 4 states' data:
# mode = "a"  will APPEND to the file,
# header = False leaves off the column headings for this state,
# since these headings were already written when the first state
# was written into this file.
selectedStateDF.to_csv(outputFileName, mode = "a", header = False)

