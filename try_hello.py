from hello import hello

def  main():
    for name in  ["Alice", "Bob", "Charlie"]:
        assert hello(name)== f"hello,{name}"


