from parsing.grammar import *

def get_sample_1():
    
    return Grammar([
        NonTerminal('S', [
            "'(' S ')' S",""
        ])
    ])


def get_sample_2():
    
    return Grammar([
    NonTerminal('S', ['A B']),
    NonTerminal('A', ['A "a"', "'a'"]),
    NonTerminal('B', ['B "b"', "'b'"])
])



