import doctest

VOCAB_TO_DEFINITION = {
    "control flow":"Control flow refers to the order in which individual statements, instructions, or function calls are executed in a program.\nIt determines how a program progresses based on conditions, loops, and function calls.",
    "conditionals":"Conditionals are control flow statements that execute different blocks of code based on conditions. E.g \n if condition:\n\t# Code executes if condition is true\nelif another_condition:\n\t# Runs if previous condition was false\nelse:\n\t# Runs if none of the conditions are true",
    "refactoring":"Code Refactoring is when we improve code readability, efficiency, or maintainability without changing its behavior.",
    "doctests":"Doctests are inline tests written in the docstring of a function that demonstrate expected behavior.\nA docstring is a special multiline string inside a function that describes its purpose, parameters, return value, and other details.",
    "lists":"Lists are mutable ordered collections of values, created with square brackets. E.g.\nlst = [1, 2, 3]",
    "dictionaries":"Dictionaries are key-value pairs stored in curly braces {}. E.g\nd = {'name': 'Alice', 'age': 25}",
    "for loops":"For loops are loops that iterate over iterable objects like lists, tuples, and strings. E.g\nfor i in range(5):\n\tprint(i)",
    "while loops":"While loops are loops that run as long as a condition is True. E.g.\nx = 0\nwhile x < 5:\n\t print(x)\n\tx += 1",
    "complexity":"The complexity of an algorithim refers to the efficiency of an algorithm in terms of time and space, often analyzed using Big-O notation.",
    "OOP":"Object Oriented Programming (OOP) is a parogramming paradigm that models problems using classes and objects.",
    "Sorting":"Sorting refers to a common concept in programming where we want to arrange elements according to a certain order.\nCommon sorting algorithms include merge sort and quick sort."
}

def test_file_equality(file1name: str, file2name: str) -> str:
    """
    Given the name of two .txt files (file1name, file2name), returns
    "Both are equal!" if both txt files have the same content. Otherwise
    returns infromation on which line both are different on.
    """
    s = "Both are equal"
    with open(file1name, 'r') as f1, open(file2name, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        max_len = max(len(lines1), len(lines2))
        for i in range(max_len):
            line1 = lines1[i] if i < len(lines1) else '<no line>'
            line2 = lines2[i] if i < len(lines2) else '<no line>'
            if line1 != line2:
                s = "Files differ!\n"
                s += f"Difference at line {i+1}:\n"
                s += f"File1: {line1.strip()}\n"
                s += f"File2: {line2.strip()}\n"
                return s
        return s


def simplify_line(line: str) -> str:
    """
    Given a line from a CS1 lecture (line), returns the simplified version of 
    the line based on the VOCAB_TO_DEFINITION dictionary.

    >>> simplify_line("Alright, let’s start today by reviewing control flow.")
    'Alright, let’s start today by reviewing control flow.\\n\\nControl flow refers to the order in which individual statements, instructions, or function calls are executed in a program.\\nIt determines how a program progresses based on conditions, loops, and function calls.\\n\\n'

    >>> simplify_line("Today we’ll discuss iteration with lists and dictionaries.")
    'Today we’ll discuss iteration with lists and dictionaries.\\n\\nLists are mutable ordered collections of values, created with square brackets. E.g.\\nlst = [1, 2, 3]\\n\\nDictionaries are key-value pairs stored in curly braces {}. E.g\\nd = {\'name\': \'Alice\', \'age\': 25}\\n\\n'
    """


def simplify_transcript(filename: str) -> None:
    """
    Given the name a sample CS1 lecture transcript as a txt (filename), creates a new
    file with the name "[filename]_simplified.txt". The new file
    is a simplified version of "[filename].txt" based on the 
    VOCAB_TO_DEFINITION dictionary.
    """
