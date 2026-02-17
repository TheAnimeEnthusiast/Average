# There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. 
# Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?

tree1 = float(input("What is the height of this tree?"))
tree2 = float(input("What is the height of this tree?"))
tree3 = float(input("What is the height of this tree?"))
tree4 = float(input("What is the height of this tree?"))
tree5 = float(input("What is the height of this tree?"))

totalHeight = tree1 + tree2 + tree3 + tree4 + tree5

print(totalHeight/5)