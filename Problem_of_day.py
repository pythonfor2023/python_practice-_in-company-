class employee:

    def kill(self):
        print("hello sir")

    def simple(self):
        self.kill()
        print("hello world")

    def simpl34(self):
        print("helool inside simple34")
        self.simple()

obj = employee()
obj.simpl34()


# understanding the how list and the tuple works 
# reffered the site for the better understanding :https://www.opensourceforu.com/2021/05/memory-management-in-lists-and-tuples/
# -basic ideas of the list an tuple
# -list
# the list is the spcial datatype used for strong and accessing the data 
# properties of the list is the its is growable in nature

# #### Cpython : https://github.com/python/cpython/blob/master/Objects/listobject.c
# ‘’’
# /* This over-allocates proportional to the list size, making room
# * for additional growth. The over-allocation is mild, but is
# * enough to give linear-time amortized behavior over a long
# * sequence of appends() in the presence of a poorly-performing
# * system realloc().
# * Add padding to make the allocated size multiple of 4.
# * The growth pattern is: 0, 4, 8, 16, 24, 32, 40, 52, 64, 76, 88, 120, 160 ...
# * Note: new_allocated won’t overflow because the largest possible value
# * is PY_SSIZE_T_MAX * (9 / 8) + 6 which always fits in a size_t.
# */
# Append – O(1)
# Extend – O(k)
# Pop last element – O(1)
# Pop anywhere else – O(n) worst case
# Insert – O(n) worst case
# Index – O(1)
# Slice – O(k)
# in Operator – O(n)
# Sort – O(nlogn) – tim sort is used
# # why ,how, applications?
# how 
# ex
import sys
list=["subbu","hegde",33,667,89,90]
print("the size of the list:",sys.getsizeof(list))
print("pinting the memory allowactions fo the list:",id(list))
#appeding the elementin tho the list
list.append("Hello hii")
print(list)
print("the size of the List after appending:",sys.getsizeof(list))
print("print the  or the location :",id(list))
list.append("sdsdsdsdsdsdsd")
print("the updated list:",list)
print("the size:",sys.getsizeof(list))
print("the  find memeory locations if list:",id(list))
list1=[2323232323,23232323232322323]
list.append(list1)
print(list)
print("size:",sys.getsizeof(list))
print("id:",id(list))
print("the empty lits checking:")
list=[]
list1=[]
print(type(list))
print(id(list1))
print(id(list))

# --------------------------------------:------------------------------------------------------------------
print("_________________________________tuple:________")
tuple=("simple","java","applications",23,23232,232,3232)
print("the size of the tuple:",sys.getsizeof(tuple))
print("the location",id(tuple))
tuple1=()
tuple=()
print(id(tuple1))
print(id(tuple))
tuple=("ssss")
tuple3=("44")
print(id(tuple))
print(id(tuple3))