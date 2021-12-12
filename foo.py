from cubed4th import FORTH

if __name__ == "__main__":
    code = """

```

: hello-world dup . 'World! ;

"""

    e = FORTH.Engine(run=code)

    print(getattr(e, "hello-world")('Scott'))

    print(e.root.stack)


