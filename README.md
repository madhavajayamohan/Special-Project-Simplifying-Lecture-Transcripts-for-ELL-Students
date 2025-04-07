# Special Project: Simplifying Lecture Transcripts for ELL Students

The goal of this assignment is to make you consider solutions for how to help ELL students, and help you practice how to combine concepts you have learned over the entirety of CSC108 such as:

Manipulating Strings
Reading and Writing to Files
For Loops
Utilizing Dictionaries
Conditionals

## Context:

In order to help ELL students, Professor Ajaya wants to make transcripts of his lectures available for students to review concepts after class. However, when he reviews the transcripts, he realizes that he used idioms and expressions that ELL students may not be able to understand.

In order to make the transcripts more accessible for ELL students, Professor Ajaya tasks you with writing a script that can create lecture transcripts with appropriate definitions.

## Example

Consider that the original transcript consists of one line:

*Learning to code can feel like finding a needle in a haystack sometimes.*

However, the ELL students may not understand the idiom finding a needle in a haystack.  So, you need to produce a new transcript like so:

*Learning to code can feel like finding a needle in a haystack sometimes.*

*When someone says that finding something is like trying to find a 'needle in a haystack,' it means that its very hard or near impossible to find it.*

In essence, you need to insert the definition of the term in the new file

## Tools Given to You

In order to complete this task, you have been given:

A dictionary called IDIOM_TO_DEFINITION that maps vocabulary terms to their definition. From the above example, "control flow" would be a key, while its definition is the value
A function called test_file_equality that tells you whether two files have the same content or not
Five files that will help you get started with testing, along what they are supposed to look like

## Your Task

For this project, you must:

1. Complete the function simplify_line. simplify_line, given a string, checks whether or not the string contains any vocabulary we need to provide definitions for. If there is vocabulary we need to provide a definition for, it returns a new string with the original line, and the definitions. In order to complete this task, consider:
   i. All the expressions you need definitions for is given by the keys of the IDIOM_TO_DEFINITION dictionary
   ii. You need to go through each word in the given line, and detect whether or not the word is a key in  IDIOM_TO_DEFINITION.
   iii. You must also consider the fact that IDIOM_TO_DEFINITION has keys that contain for multiple words– when going through the line, you must take into account how it has multiple words
   iv. You should be able to detect an idiom in the list, even if it in a different case from the key in the dictionary
   v. If you detect a vocabulary word, you need to insert the definition after the line– specifically there must be one empty line in-between the original line and the definition, and one empty line after the definition
   vi. If you detect multiple vocabulary words in the same sentence, then you must insert the definitions for each word in order of appearance. For example, if "piece of cake" comes before "half the battle" then the definition for "piece of cake" must be added before the definition of "half the battle". Both definitions comes after the original line.
   vii. There should be an empty line in-between the original line and each definition. There should be an empty line after the definition
2. Complete the function simplify_transcript. simplify_transcript, given the file name to a txt file (the lecture transcript) writes a new txt file that represents the simplified transcript with additional definitions.
   i. Every single line on the given txt file represents a sentence of the lecture transcript.
   ii. Make sure to utilize simplify_line in order to complete this task.
   iii. Make sure to test whether your function works with test_file_equality to compare the new file you produce and the solution files.

# Testing

Consider what kind of additional testing you need to do for this assignment. What might be potential edge cases? Which function is the easiest to test? What type of testing do you need for both functions?
