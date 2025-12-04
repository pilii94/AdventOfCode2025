# What do you get if you add up all of the invalid IDs?


from pydantic import BaseModel
from itertools import combinations


class IDRange(BaseModel):
    idrange_row: str

    @property
    def full_range(self) -> list[int]:
        """Get the full integer range"""
        if len(self.idrange_row.split("-")) < 2:
            return 0

        full_range = list(range(int(self.idrange_row.split("-")[0]), int(self.idrange_row.split("-")[1])+1))
    
        return [str(num) for num in full_range]
    

def get_invalid_ids(subnum)-> list[int]:

    invalid_ids = []
    #if subnum has leading zeroes its invalid
    if subnum[0]=='0':
        return []
    elif len(subnum) <= 1:
        return []
    elif len(subnum) == 2:
        # if yes, check if the two digits are equal
        if subnum[0] == subnum[1]:
            invalid_ids.append(int(subnum))
            return invalid_ids
    #if its an odd number return invalid_ids as it wont be invalid
    elif len(subnum) % 2!= 0:
        return []
    # if its an even number check if the 2 numbers resulting are equal 
    else: 
        mid = len(subnum)//2
        first_half = subnum[:mid]
        second_half = subnum[mid:]
        if first_half == second_half:
            invalid_ids.append(int(subnum))
            return invalid_ids

    return invalid_ids


            

def read_input(filename: str) -> list[IDRange]:
    """Read the input file and parse it into Banks."""
    ranges = []
    
    with open(filename, 'r') as f:
        for line in f:
            lines = line.split(",")
            for line in lines:  
                idrange_row = IDRange(idrange_row=line)
                ranges.append(idrange_row)
    
    return ranges




def invalid_IDs_sum(invalid_ids: list[int]) -> int:

    return sum(invalid_ids)



if __name__ == "__main__":
    

    test_ranges = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862"
    ]

    input = [IDRange(idrange_row=range) for range in test_ranges]

    print("\nTest cases:")
    for range_ in input:
        full_range = range_.full_range
        invalid_ids_test = []
        for subnum in full_range:
            invalid_ids_test += get_invalid_ids(str(subnum))
        print(f"{range_} -> {invalid_ids_test}")

    print("=====")


    input_data = read_input('Dec02/input.txt')
    invalid_ids = []
    for range_ in input_data:
        full_range = range_.full_range
        for subnum in full_range:
            invalid_ids += get_invalid_ids(str(subnum))
   
  
    total = invalid_IDs_sum(invalid_ids)
    print(total)


