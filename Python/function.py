def function1 (function):
    def wrapper():
     print("hello")
     function()
    print("welcome everyone")
    return wrapper
    @function1
    def function2():
        print("python")

        function2=function1(function2)
        function2()