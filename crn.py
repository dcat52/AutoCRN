"""AutoCRN
dcat52 Software

Usage:
    crn.py [--import <file>]
    crn.py -h | --help
    crn.py --version

Options:
    -h, --help                      show this screen.
    -i <file>, --import <file>      use CRN's from a file [default: crn.txt]

"""
# The above docstring is used for arguments
### DO NOT MONDIFY ABOVE THIS COMMENT ####

import os
from _ast import arguments
from docopt import docopt
from writer import crnWriter

__author__ = 'dcat52 (Davis Catherman)'

def main(args):
    """Main Function
    Args:
        args (dictionary): The parameters dictionary. See above

    Returns:
    """
    
    input_file = args['--import']
    try:
        crns = [line.rstrip('\n') for line in open(input_file)]
    except:
        print 'Error opening file'
        sys.exit(0)

    crnWriter(crns)
    
    
if __name__ == '__main__':
    # Parse args
    arguments = docopt(__doc__, version="0.1.0")
    main(arguments)
