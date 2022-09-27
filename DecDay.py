# Decimal day Calculator

input_str_raw = '23 10 31 42' # Input string, enter in format dd hh mm ss. Example string is provided

input_str_split = input_str_raw.split()

input_str = [ele.lstrip('0') for ele in input_str_split] # Removes leading zero's if any are present
        
input_int = [eval(i) for i in input_str]

dec_date = input_int[0] + ((input_int[1]+12)/24) + (input_int[2]/(24*60)) + (input_int[3]/(24*3600))

print(dec_date)
