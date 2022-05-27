#!/usr/bin/env python3
from markdown import markdown as md
def main():
    with open('bloglist.md', 'r') as m:
        myblogs = m.read()
        myblogs = md(myblogs)
        m.close()

    with open('templates/earth/template.html', 'r') as f:
        myfile = f.read().replace("{ List of Blogpages }", myblogs)
        f.close()
    print(myfile)

if __name__ == "__main__":
    main()
