
def main():
    module = __import__("MyModule")
    clazz = getattr(module, "MyClass")
    clazzInstance = clazz("King Arthur")
    method = getattr(clazzInstance, "myMethod")
    method()
        
main()