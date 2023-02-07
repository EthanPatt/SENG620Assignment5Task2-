# Task 2, Use a dictionary to build a program to retrieve the State information

# Create State Class that can hold State, Capital, Area, population, and abbreviation
class State:

    def __init__(self, state, capital, area, population, abbreviation):
        self.state = state
        self.capital = capital
        self.area = area
        self.population = population
        self.abbreviation = abbreviation

# Create a function to print the information for the state the user picks
    def GetData(self):
        str = f"{self.state} has a capital of {self.capital}, area of {self.area}, population of {self.population} and is abbreviated as {self.abbreviation}"
        return str

# Create empty dictionary
dict = {}

# Enter in dictionary keys and information in order of the state class
dict['Michigan'] = State('Michigan', 'Lansing', '96,713.51', '10,050,811', 'MI')
dict['Alaska'] = State('Alaska', 'Juneau', '665,384.04', '732,673', 'AK')
dict['Texas'] = State('Texas', 'Austin', '268,596.46', '29,527,941', 'TX')
dict['California'] = State('California', 'Sacramento', '163,694.74', '39,237,836', 'CA')
dict['Idaho'] = State('Idaho', 'Boise', '83,568.95', '1,900,923', 'ID')
dict['Florida'] = State('Florida', 'Tallahassee', '65,757.70', '21,781,128', 'FL')
dict['New York'] = State('New York', 'Albany', '54,554.98', '19,835,913', 'NY')
dict['Alabama'] = State('Alabama', 'Montgomery', '52,420.07', '5,039,877', 'AL')
dict['Ohio'] = State('Ohio', 'Columbus', '44,825.58', '11,780,017', 'OH')
dict['Hawaii'] = State('Hawaii', 'Honolulu', '10,931.72', '1,441,553', 'HI')

# Create loop to ask user for the state to look up, for each input from user print the states information
while True:
    User = input('Which state would you like to look up?: ')
    print(dict[User].GetData())
    Again = input('Would you like to look up another state?: (yes or no)')
    if Again == "no":
        print("\nI hope you found the information you were looking for!")
        break