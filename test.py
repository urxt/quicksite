#!/usr/bin/env python3
def main():
    with open('templates/earth/template.html', 'r') as f:
        myfile = f.read().replace("{ List of Blogpages }", "Stuff")

    print(myfile)

if __name__ == "__main__":
    main()
