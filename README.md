# Python TM-score Library

A Python wrapper around the original TM-score C++ code available at [Zhang Lab](https://zhanggroup.org/TM-score/), which has been modified to be callable as a library within Python scripts.


## Installation

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/veghen/TMscore4Python.git
   cd TMscore4Python
   ```
2. Install using pip:
   ```
   pip install .
   ```

## Usage
```Python
from TMscore import TMscore

lengths, results = TMscore(pdb_file_path_to_structure_1, pdb_file_path_to_structure_2)
print(f"length of structure 1: {lengths[0]}, length of structure 2: {lengths[1]}")
print(f"TMscore: {results[0]}, RMSD: {results[1]}")
```
