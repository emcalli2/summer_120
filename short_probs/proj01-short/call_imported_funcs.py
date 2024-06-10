from short1_thing import *
def main():
    line = input()
    foo_line = foo(line)
    print(foo_line)
    line2 = input()
    line3 = input()
    bar_line = bar(line,line2,line3)
    print(bar_line)
    baz_line = baz(foo_line,bar_line)
    print(baz_line)
main()