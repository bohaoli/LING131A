#!/usr/local/bin/python3

"""

Script that anaylzes a file. 

You can run this from the command line as follows:

   $ python analyze_file.py INPUT_FILE

where INPUT_FILE is expected to exist and to contain text only.

"""

# Import statements, immediately after the docstring.
import sys


# This is a good place to define variables so that those definitions are not hidden
# deep inside the code.
RESULTS_FILE = 'results.txt'


def analyze_file(filename):
    """The main function, you may define other functions that can then be called by
    this function."""

    # Open the input file
    infile = open(filename, 'r')
    
    # Open the output file results.txt for writing the results
    # (this will overwrite existing files with the same name).
    outfile = open(RESULTS_FILE, 'w')
    
    # Some code that  reads everything from infile
    # ...

    # Some code that analyses the contents of the input file
    # ...
    
    # Some code that writes results to the output file
    # We did not analyze anything, just copying the input to the results file.
    for line in infile:
        outfile.write(line)

    # Close your files
    infile.close()
    outfile.close()
    

if __name__ == '__main__':
    
    # Only run the code in this block if the current file is not used as a
    # module.  To do this, you can use the special variable __name__ which is
    # defined for modules (but also classes and functions). A Python code file
    # is either the main script, in which case__name__ is set to '__main__' or a
    # module, in which case __name__ holds the namespace of the module.

    # Read the name of the file to process from the command line.
    infile = sys.argv[1]

    # Call the main function.
    analyze_file(infile)
