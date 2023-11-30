#!/usr/bin/python3.8
def print_hidden():
    for name in (dir(hidden_4)):
        if not name.startswith('__'):
            print('{}'.format(name))


if __name__ == '__main__':
    import hidden_4
    print_hidden()
