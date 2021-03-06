from random import *
import string


### If length of string is not provided then by default we will generate a string from range of 5-10 length of string
### If size i.e., number of records is not mentioned we will throw an error
### If requested for a unique column value with size > max_generations, then we will throw an error

def string_generator(length=None, size=None, unique=False):
    ele_array= []
    len_not_provided = False
    
    if (length!=None and unique and 52**length < size) or size==None:
        print("error")
        return []
    
    if length==None:
        len_not_provided=True
    
    chars = string.ascii_uppercase + string.ascii_lowercase
    i=0
    while i<size:
        if len_not_provided:
            length = randint(5,10)
        val = ''.join(choice(chars) for _ in range(length))
        if not(unique==True and val in ele_array):
            ele_array.append(val)
            i = i+1
    return ele_array


### If length of string is not provided then by default we will generate a string from range of 5-10 length of string
### If size i.e., number of records is not mentioned we will throw an error
### If requested for a unique column value with size > max_generations, then we will throw an error

def integer_generator(min_num, max_num, size, is_unique, is_nullable):
    ele_array= []
    i=0
    if is_unique and is_nullable:
        ele_array.append(None)
    while i<size:
        if not(is_unique) and is_nullable:
            if "5"==choice("1234567890"):
                ele_array.append(None)
                continue
        val = randint(min_num, max_num)
        if not(is_unique and val in ele_array):
            ele_array.append(val)
            i = i+1
    return ele_array

#BigInt value range (8 Bytes) is -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
def dt_bigint_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = -9223372036854775808
    max_num = 9223372036854775807
    #checking if given length fits in min and max numbers
    if length != -1:
        new_min_num = -1*((10**length)-1)
        new_max_num = (10**length)-1
        if max_num < new_max_num:
            print("error - length exceeds")
            return []
        else:
            min_num = new_min_num
            max_num = new_max_num
    #Checking if given size fits in length range
    if is_unique and not(is_nullable) and size>(-min_num)+max_num:
        print("error - size exceeds for unique values")
        return []
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)    

#Integer value range (4 Bytes) is -2,147,483,648 to 2,147,483,647
def dt_int_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = -2147483648
    max_num = 2147483647
    #checking if given length fits in min and max numbers
    if length != -1:
        new_min_num = -1*((10**length)-1)
        new_max_num = (10**length)-1
        if max_num < new_max_num:
            print("error - length exceeds")
            return []
        else:
            min_num = new_min_num
            max_num = new_max_num
    #Checking if given size fits in length range
    if is_unique and not(is_nullable) and size>(-min_num)+max_num:
        print("error - size exceeds for unique values")
        return []
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)

#SmallInt value range (2 Bytes) is -32,768 to 32,767
def dt_smallint_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = -32768
    max_num = 32767
    #checking if given length fits in min and max numbers
    if length != -1:
        new_min_num = -1*((10**length)-1)
        new_max_num = (10**length)-1
        if max_num < new_max_num:
            print("error - length exceeds")
            return []
        else:
            min_num = new_min_num
            max_num = new_max_num
    #Checking if given size fits in length range
    if is_unique and not(is_nullable) and size>(-min_num)+max_num:
        print("error - size exceeds for unique values")
        return []
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)    

#TinyInt value range (1 Bytes) is 0 to 255
def dt_tinyint_gene(size, length=-1, is_unique=False, is_nullable=True):
    min_num = 0
    max_num = 255
    #checking if given length fits in min and max numbers
    if length != -1:
        new_min_num = 10**(length-1)
        new_max_num = (10**length)-1
        if max_num < new_max_num and size > max_num-(10**(length-1))-1:
            print("error - length exceeds")
            return []
        else:
            min_num = min_num if min_num>new_min_num else new_min_num
            max_num = max_num if max_num<new_max_num else new_max_num
    #Checking if given size fits in length range
    if is_unique and size>2*(max_num-min_num)+1:
        print("error - size exceeds for unique values")
        return []
    
    list_of_vals = list(range(-1*max_num, -1*min_num)) + list(range(min_num, max_num))
    return integer_generator(min_num, max_num, size, is_unique, is_nullable)    

print(dt_bigint_gene(size=50, length=4, is_unique=False, is_nullable=False))
print()
print(dt_int_gene(size=50, length=4, is_unique=True, is_nullable=True))
print()
print(dt_smallint_gene(size=50, length=4, is_unique=True, is_nullable=False))
print()
print(dt_tinyint_gene(size=50, length=3, is_unique=False, is_nullable=True))
#print(integer_generator(None, 10, True))
#print(string_generator(None, 10, True))

#Nullable or NotNullable
#Negative numbers
#Int BigInt SmallInt TinyInt
#Char VarChar Text
#Binary Boolean
#Float Double Decimal
#Date Time TimeStamp DateTime
#Serial