# File management not important to this course.
# But you may find it useful in the future?

#%% Write file - will be deleted at the end of this file.
with open("squares", "w") as f:
    for i in range(11):
        f.write(f"{i**2}\n")

#%%
# invalid - must be in the with block.
f.write("abc")

#%% Read file - readline
with open("squares", "r") as f:
    line = f.readline().strip()
    while line:
        print(line)
        line = f.readline().strip() # remove additional \n

#%% Append to file - does not overwrite.
# mode is 'a' - append.
# 'w' would overwrite
with open("squares", "a") as f:
    for i in range(11, 21):
        f.write(f"{i**2}\n")

#%% Read file - readlines
with open("squares", "r") as f:
    lines = f.readlines()
    print(lines)
    print("".join(lines))

#%% Delete example file
import os
os.remove('squares')