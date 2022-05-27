import sys

def create_file(filename):
    with open(("blogpages/{}.md".format(filename)), 'w') as f:
        filename = filename.capitalize()
        f.write("# {}".format(filename))
        f.close()

def link_bloglist(filename):
    with open("bloglist.md", 'a+') as f:
        f.seek(0)
        f.write("+ [{}](blogpages/{}.md)\n".format(filename, filename))
        f.close()


def main():
    if len(sys.argv) < 2:
        raise Exception("No filename provided")
    else:
        filename = sys.argv[1]
        create_file(filename)
        link_bloglist(filename)
    

if __name__ == "__main__":
    main()

