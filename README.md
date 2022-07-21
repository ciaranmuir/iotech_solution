# iotech_solution
Solution to first iotech exercise by Ciaran Muir

To run the program, start by downloading the Solution folder.

Running solution.py in the terminal will create two new JSON files; 'new_devices.json' (unsorted) and 'new_devices_sorted.json' (sorted). 

'new_devices.json' is the first JSON file created in the newly specified schema which remains unsorted. 
This is created created by the create_new_devices_json(old, new) function in solution.py. 
This function takes the original devices.json file, extracts the needed information and creats a new JSON file in the new format at the file path specified in it's second argument. 

'new_devices_sorted.json' is the second JSON file which is the sorted version of the previous file in the new format. 
This is created by the sort_devices(old, new) function in solution.py. 
This function sorts the unsorted JSON file created by create_new_devices_json() - described above - and writes it to the location specified in the second argument.


