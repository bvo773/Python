pi = 3.14159246

nums = [1,2,3,4]

# objects are passed as a reference(address)
def modifynums(n):
	n.append(5)
	n.extend([6,7,8])
	print(n)

modifynums(nums)
print(nums)