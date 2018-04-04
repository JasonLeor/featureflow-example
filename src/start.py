import os

if __name__ == '__main__':
    dir = "component"
    for (root, dirs, files) in os.walk(dir):
        for filename in files:
            if filename == '__init__.py':
                continue
            f = open(os.path.join(root,filename))
            print(f.read())
