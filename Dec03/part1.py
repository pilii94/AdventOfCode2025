## what is the total output joltage?
from pydantic import BaseModel
import numpy as np

class Bank(BaseModel):
    bank_row: list[int]

    @property
    def max_joltaje(self) -> int:
        """Get the two highest values while maintaining their original left-to-right order."""
        if len(self.bank_row) < 2:
            return 0
        
        max_joltage = 0
    
        for i in range(len(self.bank_row)):
            for j in range(i + 1, len(self.bank_row)):
                
                joltage = self.bank_row[i] * 10 + self.bank_row[j]
                
                if joltage > max_joltage:
                    max_joltage = joltage
        
        return max_joltage
        
    

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

    # test_banks = [
    #     "987654321111111",
    #     "811111111111119",
    #     "234234234234278",
    #     "818181911112111"
    # ]

    # print("\nTest cases:")
    # for bank_str in test_banks:
    #     bank = Bank(bank_row=[int(c) for c in bank_str])
    #     print(f"{bank_str} -> {bank.max_joltaje}")

    total = calculate_total_output_joltage(input_data)
    
    print(total)