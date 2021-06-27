#!/usr/bin/python3

notes = [
    'Need to have \033[1mTERM\033[0m set to \033[1mxterm-256color\033[0m',
    'Usage (formatting code): \033[38;5;93m\033[1m\\033[38;5;<index>m\033[0m',
    'Prepend string with code for desired color/formatting and append endchar code (\\033[0m])',
    'Can be used along with formatting codes from \033[1mshell_colors.py\033[0m',
    'If using along with python string formatting (ljust, rjust, or center), these characters are counted',
    '    To fix this, add increase character count for \\033, [, char length of <index>, and m',
    '    Example: \\033[0m is 4 characters and \\033[100m is 5 characters'
]
msg = 'extended shell colors'.upper()
l = [len(msg)]
temp = []
for i, c in enumerate(msg, start=200):
    temp.append(f'\033[38;5;{i}m')
    temp.append(c)
temp.append('\033[0m')
msg = ''.join(temp)
l.append(len(msg))

print(f' {msg} '.center(148 + (l[1]-l[0]), '-'))
print(''.ljust(148, '-'))
print('\n'.join([f'* {n}' for n in notes]))
print(''.ljust(148, '-'))
for i in range(256):
    print(f'{i:4d}: \033[38;5;{i}mexample\033[0m', end='  ')
    if (i+1)%10 == 0:
        print()
print()
print(''.ljust(148, '-'))