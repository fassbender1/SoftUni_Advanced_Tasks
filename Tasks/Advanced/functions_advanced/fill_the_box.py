def fill_the_box(length, width, height, *args):
     v = length * width * height
     left = 0

     for cubes in args:
         if cubes == "Finish":
             break
         if v:
             v -= cubes

     if v < 0:
         return f"No more free space! You have {abs(v)} more cubes."
     return f"There is free space in the box. You could put {abs(v)} more cubes."


print(fill_the_box(2, 8,2, 2, 1, 7, 3, 1, 5, "Finish"))