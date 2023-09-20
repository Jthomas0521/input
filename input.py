import os, time

dir_folder = os.path.dirname(os.path.abspath(__file__))

input_folder = os.path.join(dir_folder, 'text')


for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
    
        if os.path.isfile(input_path):
            print("Lines from '{}':".format(file_name))
            with open(input_path, "r") as file:
                for line in file:
                    print(line.strip())
                    time.sleep(1)
            print("\n")