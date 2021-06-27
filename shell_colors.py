#!/usr/bin/python3

notes = [
    'Usage (formatting code): \033[1m\\033[\033[91m<index>\033[0mm',
    'Prepend string with code for desired color/formatting and append endchar code (index 0)',
    'Multiple color/formatting codes can be used; only need to be closed with one endchar code (index 0)',
    'Use something like neofetch to see predefined colors easily',
    'If using along with python string formatting (ljust, rjust, or center), these characters are counted',
    '    To fix this, add increase character count for \\033, [, char length of <index>, and m',
    '    Example: \\033[0m is 4 characters and \\033[100m is 5 characters',
    'Note that most indices do nothing -- I believe they\'re placeholders with other uses within the OS.'
]
print(' \033[1m\033[92mSHELL COLORS AND FORMATTING\033[0m '.center(161, '-'))
print(''.ljust(148, '-'))
print('\n'.join([f'* {n}' for n in notes]))
print(''.ljust(148, '-'))
for i in range(256):
    if i == 0:
        print(f'{i:4d}: endchar', end='  ')
    else:
        print(f'{i:4d}: \033[{i}mexample\033[0m', end='  ')
    if (i+1)%10 == 0:
        print()
print()
print(''.ljust(148, '-'))
