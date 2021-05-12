# Python data structure to create an immutable dataset using the collections package.
import collections

# Creating a class called Scientists and declaring the attributes using the collections package.
Scientists = collections.namedtuple('Scientists',[
    'name', 'field', 'born', 'nobel'])

# Create a Scientists object and assign the values
Ada = Scientists('Ada Lovelace', 'math', 1815, False)

# Using Pretty Print package
from pprint import pprint
# pprint(Scientists)


# print(f"Name {Ada.name} Field {Ada.field}")

# Dummy data
scientists = (Scientists('Ada Lovelace', 'math', 1815, False),
              Scientists('Drus', 'science', 1835, True),
              Scientists('Telsa', 'chem', 1825, True),
              Scientists('Lovelace', 'phy', 1875, False))

# pprint(scientists)              
if __name__=='__main__':
    # Filter the data based on the Nobel winners
    Nobel_winners = filter(lambda x: x.nobel is True, scientists)

    try: 
        print('Nobel winners')
        for i in range(len(scientists)):
            # Nobel_winners will print the iterable filter object hence we use next
            pprint( next(Nobel_winners).name )
    except StopIteration:         
        print("Filter completed")

    Nobel_winners_tuple = tuple(filter(lambda x: x.nobel is True, scientists))
    pprint(Nobel_winners_tuple)


