'''
Use a stack to check whether or not a string has balanced usage of parenthesis.

Example:
    (), ()(), (({[]}))   <- Balanced
    ((), {{{)}}], [][]]] <- Not Balanced.

Balanced Example: {[]}


())
Non-Balanced Example: (()

Non-Balanced Example: ))  # Edge case

Methods:
is_paren_balanced(string) : bool
is_match() : bool

'''
from stack import Stack


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
