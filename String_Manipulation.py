

y=["a","b","c","d","e"]
y[1]="r"
y[2:]=["s","t"]


print(y,"\n")

######################################################

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1]=10.50

# Change "living room" to "chill zone"
areas[4]="chill zone"

print(areas,"\n")

########################################################

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1=areas+["poolhouse",24.5]

# Add garage data to areas_1, new list is areas_2
areas_2=areas_1+["garage",15.45]

print(areas_2,"\n\n"); print(areas_1)

#Pay attention here: as soon as you remove an element from a list, 
#the indexes of the elements that come after the deleted element all change!

#removing the poolhouse and float value here

del(areas[-4:-2])
#or
#del(areas[10:12])

print(areas)




