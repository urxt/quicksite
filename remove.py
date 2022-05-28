# Remove an existing blog
from os import walk, remove

def remove_blog():
    path = "./blogpages/"
    filenames = next(walk(path), (None, None, []))[2]
    for index, f in enumerate(filenames):   
        print("{}: {}".format(index, f))

    file = input("Delete which file?: ").strip()
    if file in filenames:
        remove("blogpages/{}".format(file))
        with open("bloglist.md", "+a") as f:
            f.seek(0)
            if file in f.read()
                f.truncate()
                

        print("File: {} deleted".format(file))

    else:
        print("Invalid filename")



def main():
    remove_blog()

if __name__ == "__main__":
    main()
