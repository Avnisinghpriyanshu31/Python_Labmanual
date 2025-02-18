def convert_base(num, from_base, to_base):
    
    num_base_10 = int(num, from_base)
    
    
    if to_base == 10:
        return str(num_base_10)
    
   
    result = ""
    while num_base_10 > 0:
        result = str(num_base_10 % to_base) + result
        num_base_10 //= to_base
    return result or "0"


num = "1011" 
from_base = 2  
to_base = 16   

print(convert_base(num, from_base, to_base))
