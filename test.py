import os
import random 


path = os.getcwd()

max_items=[64, 128, 256, 512, 1024, 2048]

max_elem = random.randint(0, (len(max_items)-1) )
average = random.randint(64, 1024)
min_item = random.randint(2, 64)
sum_items = average + max_items[max_elem] + min_item

s = f"max {max_items[max_elem]} min {min_item} average {average} sum {sum_items }"

f = open(f"{path}\\demo.txt","a")
f.write(f"{s}\n")
f.close