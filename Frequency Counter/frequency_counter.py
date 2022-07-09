# A FUNCTION THAT COUNTS HOW MANY TIMES AN ELEMENT IN THE LIST OCCURED IN THAT LIST
# This function accepts a list and returns a dictionary where the keys are the elements in the list
# and the values are the number of times each element occured.

def freq_table(freq_list):
    freq_dict = {}
    for item in freq_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
            
    return freq_dict

example_list = [1,4,6,3,"d", "a", 3, "d"]

print(freq_table(example_list))