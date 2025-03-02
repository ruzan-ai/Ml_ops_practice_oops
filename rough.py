lst = [1,3,5]
my_str = "python"
my_int = 155

#print(type(my_str))

my_lst = my_str.capitalize()

#print(my_lst)


from opps_proj import chatbook
user1 = chatbook()
print (user1.name)
#user1 = chatbook()
# Function vs Method below
# Function call
lst = [1,3,5]
a1 = len(lst)
#print(a1)

# Method Call   
user1 = chatbook()
user1.sendmsg()

print(user1.get_name())
print(user1.set_name("Ruzan"))
#print (user1._chatbook__name)
