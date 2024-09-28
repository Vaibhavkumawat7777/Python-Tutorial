import os
def start(name):
    print()
    print()
    print(f'Welcom to {name}'.center(os.get_terminal_size().columns))
    print('Author: Mr. Vaibhav Kumawat'.center(os.get_terminal_size().columns))
    print()
    print()

def end():
    print()
    print()
    print('---------Thank You---------'.center(os.get_terminal_size().columns))
    print('Author: Mr. Vaibhav Kumawat'.center(os.get_terminal_size().columns))