# Remove an existing blog
from os import walk, remove

def remove_blog():
    path = "./blogpages/"
    filenames = next(walk(path), (None, None, []))[2]
    for index, f in enumerate(filenames):
        print("{}: {}".format(index, f))

    file = input("Delete which file?: ")
    remove("blogpages/{}.md".format(file))


def main():
    list_items()

if __name__ == "__main__":
    main()
