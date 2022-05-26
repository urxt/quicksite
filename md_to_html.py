#!/usr/bin/env python3
from markdown import markdown as md 

def main():
    with open('example.md', 'r') as f:
        text = f.read()
        html = md(text)

        print(html)

    with open('example.html', 'w') as f:
        f.write(html)

if __name__ == "__main__":
    main()
