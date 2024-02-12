import os
import shutil

# files = os.walk(r"C:\Users\rajan\OneDrive\Desktop\Personal\Btech_Marksheet")

# for r,s,f in files:
#     print(f)

# print('files are on your screen')

items = []

files = os.walk(r"C:\Users\rajan\OneDrive\Desktop\Personal\Btech_Marksheet")
des = r"C:\Users\rajan\Music"
items.clear()

copied = 0

for r,s,f in files:
    for i in f:
        items.append(i)
        print(i)
        shutil.copy2(os.path.join(r,i),des)

else:
    print("items are copied start converting the data!!")
    
