## what is the total output joltage for 12?
from pydantic import BaseModel
from itertools import combinations

class Bank(BaseModel):
    bank_row: list[int]

    @property
    def max_joltaje(self) -> int:
        """Get the max.12 digit number using greedy approach"""
        if len(self.bank_row) < 12:
            return 0
        
        n = len(self.bank_row)
        result = []
        
        
        start = 0
        
        for position in range(12):
        
            remaining_needed = 12 - position - 1
            
            search_end = n - remaining_needed
            
            max_digit = max(self.bank_row[start:search_end])
            
            max_index = self.bank_row.index(max_digit, start, search_end)
            
            result.append(max_digit)
            
            start = max_index + 1
        
       
        return int(''.join(map(str, result)))
        
    

class Input(BaseModel):
    banks: list[Bank]

 
def read_input(filename: str) -> Input:
    """Read the input file and parse it into Banks."""
    banks = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  
                bank_row = [int(char) for char in line]
                banks.append(Bank(bank_row=bank_row))
    
    return Input(banks=banks)



def calculate_total_output_joltage(input_data: Input) -> int:

    return sum(bank.max_joltaje for bank in input_data.banks)



if __name__ == "__main__":
    input_data = read_input('Dec03/input.txt')

    test_banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]

    print("\nTest cases:")
    for bank_str in test_banks:
        bank = Bank(bank_row=[int(c) for c in bank_str])
        print(f"{bank_str} -> {bank.max_joltaje}")

    total = calculate_total_output_joltage(input_data)
    
    print(total)