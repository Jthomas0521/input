import os

input_folder = '/Users/jahquanthomas/Documents/GitHub/input/text'

for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
    
        if os.path.isfile(input_path):
            print(f"Lines from '{file_name}':")
            with open(input_path, "r") as file:
                for line in file:
                    print(line.strip())
            print("\n")