# Assignment 2

This assignment has two parts:

- Two exercises on data structures.
- A larger part where you write code to analyze a file.

For each part, edit the scaffolding file in the repository till it does what is requested.

Submit your files on GitHub before breakfast time of Friday October 12th, late submissions are accepted till about noon, but may result in deductions. Submission means you have pushed up your files to your repository in the classroom. Note that you may push up changes many times.


### 1. Exercises

For this part of the assignment we give you two empty functions in the file `exercises.py`, you will have to add the code that makes them work as specified:

- Finish the function `sort_input()` that takes a list of objects and returns a tuple of three lists, one with all the strings ordered alphabetically, one with all integers sorted with the highest integer first, and one with all other objects. Hint: look at the built in `isinstance()` function.

- Finish the function `count_characters()` which returns a dictionary of all characters in a string with as the value for each character the number of occurrences in the string.

For extra credit you can write unit tests for the two functions above (at least four for each function, include boundary conditions or weird input).


### 2. File analysis

Write a program that takes a file as input and outputs the following to a file named `results.txt`:

- The total number of sentences, word types and word tokens.
- The list of all word types and their frequency.
- The list of all word lengths and their frequency, this is a count of counts, that is, a list of frequencies and how many words occur at each frequency. What you should be counting here is the tokens, not the types.

The difference between types and tokens was mentioned in class a while ago, but could use a reminder. In general, a type is a concept whereas a token is an instance of that concept. In corpus linguistics this works out as the difference  between the concept of the word "cat" versus the instances of the that word. Take the sentence

```
I see a black cat and a white cat.
```

Not counting the period, there are seven types ("I", "see", "a", "black", "cat" and "white") and nine tokens (because there are two instances of both "a" and "cat").

The scaffolding of the program is given in `analyze_file.py`. You may completely change the content at your desire. The one thing that may not change is the name of the file and the name of the file that it creates. That is, we will have to be able to run

```
$ python3 analyze_file.py INPUT_FILE
```

and the result of that should be a file named `results.txt`. An example input file is given in `grail.txt`. We will compare your results on that file with results we get and we will expect your results to be similar to ours (but not completely).

To simplify the task, make the following assumptions:

- The number of sentences equals the number of periods, question marks and exclamation marks.
- Words with different inflections are different words, so "cat" and "cats" are two different words.

Hint: convert a word to its lower case for word count purposes (both for types and tokens).
