import os
for dirpath, dirnames, filenames in os.walk(path):
    for filename in [f for f in filenames]:
        name = os.path.join(dirpath, filename)
        print(name)
        image_resize(name)
