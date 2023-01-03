from xkcd import Comic
import os
path = os.path.join(os.path.expanduser('~'), "Desktop", "Folder", "xkcd")
for i in range(1, 2711):
    x = Comic(i)
    path = os.path.join(path, f"{i}-{x.getTitle()}")
    os.mkdir(path)
    x.download(path)
    with open(os.path.join(path, f"alt-{i}.txt"), "w") as file:
        file.write(x.getAltText())