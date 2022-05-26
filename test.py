#!/usr/bin/env python3
from markdown import markdown as md
def main():
    with open('blogs.md', 'r') as m:
        myblogs = m.read()
        myblogs = md(myblogs)
    with open('templates/earth/template.html', 'r') as f:
        myfile = f.read().replace("{ List of Blogpages }", myblogs)

    print(myfile)

if __name__ == "__main__":
    main()
