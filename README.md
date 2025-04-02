# Special Project: Simplifying Lecture Transcripts for ELL Students

Prof. A has decided to provide transcripts of all of his CS1 lectures to allow ELL students to review them on their own time. However, when he looks at the transcripts, he realized that some concepts weren't appropriately explained in the transcript.

Prof. A tasks you with simplifying the transcripts by adding definitions to certain subject specific vocabulary. In order to simplify this task, Prof A has graciously given you the following information:

1. A dictionary called VOCAB_TO_DEFINITION that maps certain vocabulary terms to their definition
2. A starter file with two functions: simplify_line and simplify_definition
3. Some initial lecture transcript files that you can use for testing, along with solution txt files that describe what the simplified file looks like

Your goal is to complete the functions simplify_line and simplify_transcript (hint: simplify_line), and produce new, simplified lecture transcripts as txt files.


# Input Cases

## Case 1
Let's say a lecture transcript is:

*Alright, let’s start today by reviewing control flow.*

The word "control flow" is a term in the VOCAB_TO_DEFINITION dictionary. Therefore, your simplified lecture transcript should be 
(the text in closed brackets aren't part of the ouput; they just explain spacing):

*Alright, let’s start today by reviewing control flow.*

*[paragraph break]*

*Control flow refers to the order in which individual statements, instructions, or function calls are executed in a program. [line break]*
*It determines how a program progresses based on conditions, loops, and function calls.*

*[There should be two empty lines after the last line]*

## Case 2

Let's say a lecture transcript is:

*Today we’ll discuss iteration with lists and dictionaries.*

Both the terms 'lists' and 'dictionaries' are in in the VOCAB_TO_DEFINITION dictionary. Therefore, your simplified lecture transcript should be:

in the VOCAB_TO_DEFINITION dictionary. Therefore, your simplified lecture transcript should be:

*Today we’ll discuss iteration with lists and dictionaries.*

*[paragraph break]*

*Lists are mutable ordered collections of values, created with square brackets. E.g. [line break]
lst = [1, 2, 3]*

*[paragraph break]*

*Dictionaries are key-value pairs stored in curly braces {}. E.g [line break]*
*d = {'name': 'Alice', 'age': 25}*

*[There should be two empty lines after the last line]*

## Case 3

Let's say a lecture transcript is:

*Today we’ll discuss iteration with lists and dictionaries. [line break]*

*Are you excited?*

The simplified lecture transcript should be:

*Today we’ll discuss iteration with lists and dictionaries.*

*[paragraph break]*

*Lists are mutable ordered collections of values, created with square brackets. E.g. (line break)
*lst = [1, 2, 3]*

*[paragraph break]*

*Dictionaries are key-value pairs stored in curly braces {}. E.g [line break]*
*d = {'name': 'Alice', 'age': 25}*

*[paragraph break]*

*Are you excited?*

## Case 4

Let's say a lecture transcript is:

*Lists are a really useful tool in programming.*

Note that while 'lists' is a term contained in the VOCAB_TO_DEFINITION dictionary, Lists is not a term contained in the VOCAB_TO_DEFINITION dictionary. Despit this, the simplified lecture transcript should be:

*Lists are a really useful tool in programming.*

*[paragraph break]*

*Lists are mutable ordered collections of values, created with square brackets. E.g. [line break]*
*lst = [1, 2, 3]*

*[There should be two empty lines after the last line]*
