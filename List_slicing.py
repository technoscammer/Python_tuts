# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area=areas[3]+areas[7]

# Print the variable eat_sleep_area
print(eat_sleep_area)


# Create the areas list
areas1 = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs=areas1[:6]

# Use slicing to create upstairs
upstairs=areas1[6:]

# Print out downstairs and upstairs

print(downstairs)
print(upstairs)



x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]

x[2][0]
print(x,"\n")


x2 = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x2[2][:2]
print(x2,"\n")

x3 = [["a", "b", "c"],["d", "e", "f"],["g", "h", "i"]]
x3[-1][1]

print(x3,"\n")
