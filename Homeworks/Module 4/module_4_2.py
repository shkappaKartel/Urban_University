def test_function():
    def inner_function():
        print('я в обл видмости test_function')

    inner_function()


test_function()
# inner_function() --> NameError: ...
