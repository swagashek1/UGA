def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    import O2mymodule
    O2mymodule.print_name_number('PyCharm Green', 33)

    import O2mymodule as g
    g.print_name_number('PyCharm Eggs', 44)

    from O2mymodule import print_name_number
    print_name_number('PyCharm And', 55)

    # python can get modules in your System PATH,
    # and in python you can import the path via sys.path.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/