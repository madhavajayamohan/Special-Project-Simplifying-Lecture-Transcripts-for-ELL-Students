import doctest

IDIOM_TO_DEFINITION = {
    "wrap your head around":"The phrase 'wrap your head around' means to understand something complex.",
    "a piece of cake":"To say a task is 'a piece of cake' means that it is very easy to do.",
    "barking up the wrong tree":"The phrase 'barking up the wrong tree' means you are trying something that won’t work or is not the right solution.",
    "bread and butter":"The 'bread and butter' of a subject is the basic and most fundeamental concept of the subject.",
    "wildcard":"The phrase 'wildcard' refers to something that can change or is hard to predict.",
    "up in the air":"When something is 'up in the air' it means that it is not decided or known yet.",
    "shoot yourself in the foot":"When you 'shoot yourslef in the foot,' that means you accidently make your own problem.",
    "rookie mistake":"A 'rookie' mistake refers to an error commonly made by beginners.",
    "save yourself a world of hurt": "The phrase 'save yourself a world of hurt' means you can avoid a lot problems or pain.",
    "get the hang of it": "When someone says you will 'get the hang of it', they are telling you that you will learn how to do soemthing after some practice.",
    "needle in a haystack": "When someone says that finding something is like trying to find a 'needle in a haystack,' it means that its very hard or near impossible to find it.",
    "playing hide and seek": "The phrase 'playing hide and seek' means that something appears and disappears, making it hard to find.",
    "reinvent the wheel": "The phrase to 'reinvent the wheel' refers to making something from scratch even though it already exists.",
    "treasure map": "A 'treasure map' can refer to  set of clues that lead to a solution.",
    "banging your head against the wall":"The phrase 'banging your head against the wall' means trying hard and failing again and again.",
    "roll up your sleeves": "The phrase 'roll up your sleeves' means that you should get ready to do hard work.",
    "nip it in the bud": "The phrase 'nip it in the bud' refers to stopping something before it becomes a big problem.",
    "bite off more than you can chew": "The phrase 'bite off more than you can chew' means you try to do too much.",
    "worth their weight in gold": "When something is 'worth their weight in gold', it is very valuable or useful.",
    "up the creek without a paddle": "If you are 'up the creek without a paddle' means you are in trouble with no way to get help.",
    "half the battle": "The phrase 'half the battle' means you have made a big step toward solving a problem, but not the whole solution."
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
    Given a line from a CS1 lecture, return the simplified version 
    that explains the idiom based on the IDIOM_TO_DEFINITION dictionary.

    >>> simplify_line("Learning to code can feel like finding a needle in a haystack sometimes.")
    'Learning to code can feel like finding a needle in a haystack sometimes.\\n\\nWhen someone says that finding something is like trying to find a 'needle in a haystack,' it means that its very hard or near impossible to find it.\\n\\n'

    >>> simplify_line("Once you wrap your head around how for loops work, the rest of the assignment should be a piece of cake.")
    'Once you wrap your head around how for loops work, the rest of the assignment should be a piece of cake.\\n\\nThe phrase 'wrap your head around' means to understand something complex.\\n\\nTo say a task is 'a piece of cake' means that it is very easy to do.\\n\\n'
    """


def simplify_transcript(filename: str) -> None:
    """
    Given the name a sample CS1 lecture transcript as a txt (filename), creates a new
    file with the name "[filename]_simplified.txt". The new file
    is a simplified version of "[filename].txt" based on the 
    VOCAB_TO_DEFINITION dictionary.
    """
