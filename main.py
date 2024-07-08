import create_subclips as create
import re


def main():
    create.run(re.compile(r'^(.*)?(it\'s|it\'s a|quite|how|very|really) (cute).*?$', re.I),
               True)


main()

