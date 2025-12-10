
# Math problem
from pydantic import BaseModel
from typing import List, Dict, Tuple
import numpy as np
import pandas as pd

class ProblemMatrix(BaseModel):
    model_config = {"arbitrary_types_allowed": True}
    problem_matrix: pd.DataFrame


def read_input(filename: str) -> Tuple[ProblemMatrix, list[str]]:
    matrix = []
    symbols = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip()
            if row: 
                if "+" in row:
                    symbols = row.split()
                else:
                    matrix.append(row.split())
    

    df = pd.DataFrame(matrix)
    return ProblemMatrix(problem_matrix=df), symbols

if __name__ == "__main__":
 


    problem_matrix, symbols = read_input('Dec06/input.txt')

    print(problem_matrix.problem_matrix)
  
    res_total = []
    
    for i, symbol in enumerate(symbols):

        j=0

        if symbol == '*':
         
            res_col = 1
            for j in range(0,problem_matrix.problem_matrix.shape[0]):
                print(int(problem_matrix.problem_matrix.iloc[j][i]))
                res_col *= int(problem_matrix.problem_matrix.iloc[j][i])
        elif symbol == '+':

            res_col = 0
            for j in range(0,problem_matrix.problem_matrix.shape[0]):
                print(int(problem_matrix.problem_matrix.iloc[j][i]))
                res_col += int(problem_matrix.problem_matrix.iloc[j][i])
         


        res_total.append(res_col)
        
    print(sum(res_total)) #4277556

