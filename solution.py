from typing import List

import pandas as pd
# optional for testing
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

import argparse


class Solution:
    def __init__(self, data_file_path: str, protocol_json_path: str):
        self.data_file_path = data_file_path
        self.protocol_json_path = protocol_json_path
        
        self.data_file = pd.read_csv(self.data_file_path)
        self.protocol = pd.read_json(self.protocol_json_path)

    # Question 1: What is the version name used in the communication session?

    # the first message is the version name in the communication sesson
    # need to identify the first line, then the protocol name and then
    # to get the version name from protocol json file. 
    def q1(self) -> str:
        protocol_identifier = self.data_file.keys()[2] # identifies the first header line and then took the protocol from the file.
        #print(protocol_identifier)
        #print(type(protocol_identifier))
        
        versions = self.protocol.iloc[:2,0] # first part that represents the versions+ details

        
        # Here i tried to extract the version name from protocol df according to the found value
        def find_version(df, search_value):
            for index, row in df.iterrows():
                if search_value in row['protocols']:
                    return row['protocols_by_version']
            return None
        found_ver = find_version(self.protocol, protocol_identifier)
        print(found_ver)
        

        

    # Question 2: Which protocols have wrong messages frequency in the session compared to their expected frequency based on FPS?
    def q2(self) -> List[str]:
        pass

    # Question 3: Which protocols are listed as relevant for the version but are missing in the data file?
    def q3(self) -> List[str]:
        pass

    # Question 4: Which protocols appear in the data file but are not listed as relevant for the version?
    def q4(self) -> List[str]:
        pass

    # Question 5: Which protocols have at least one message in the session with mismatch between the expected size integer and the actual message content size?
    def q5(self) -> List[str]:
        pass

    # Question 6: Which protocols are marked as non dynamic_size in protocol.json, but appear with inconsistent expected message sizes Integer in the data file?
    def q6(self) -> List[str]:
        pass

def main(data_file_path: str, protocol_json_path: str):
    solution = Solution(data_file_path, protocol_json_path)
    while True:
        print("\nAvailable functions:")
        print("1. q1")
        print("2. q2")
        print("3. q3")
        print("4. q4")
        print("5. q5")
        print("6. q6")
        print("x. Quit")

        choice = input("Enter function num to run or 'x' to quit :")
        if choice == '1':
            solution.q1()
            break
        elif choice == '2':
            solution.q2()
            break
        elif choice == '3':
            solution.q3()
            break
        elif choice == '4':
            solution.q4()
            break
        elif choice == '5':
            solution.q5()
            break
        elif choice == '6':
            solution.q6()
            break
        elif choice == 'x':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run functions with file path")
    parser.add_argument('data_file_path', type=str,help="Path to the fata file")
    parser.add_argument('protocol_json_path', type=str,help="Path to the protocol file")
    args = parser.parse_args()
    main(args.data_file_path, args.protocol_json_path)


"""
running :
python solution.py data.txt protocol.json
"""