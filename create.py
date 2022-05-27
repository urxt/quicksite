import sys

def create_file(filename):
    with open(("blogpages/{}.md".format(filename)), 'w') as f:
        f.write("# Heading")
        f.close()


def main():
    filename = sys.argv[1]
    create_file(filename)
    

if __name__ == "__main__":
    main()

