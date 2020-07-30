nums =['a','b','c','d','e','f','g','h','i','j','k','l','m','n']

start=0
srez=4

new_data= []
for _ in range(0,len(nums),4):
    new_data.append(nums[start:srez] )
    start =srez
    srez+=srez

print(new_data)

chunks = [nums[x:x+4] for x in range(0, len(nums), 4)]

