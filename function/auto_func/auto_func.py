import func_def

#func_def.Print.do_foo()

def do_foo_local():
    print ("foo local!")



def main():
    obj = func_def.Print()

    func_name = "do_foo"
    func_name_local = "do_foo_local"
    func_name_away = "func_def.do_foo_away"
    static_name = "static_foo"

    # use eval() to get the string value from a variable
    eval(func_name_local)()
    eval(func_name_away)(123)

    # use getattr() to get method from a class or an instance
    # sometimes you have to use is_callable() to make sure that it is a method but not an attr
    class_attr_obj = getattr(obj, func_name)
    if hasattr(class_attr_obj, '__call__'):
        class_attr_obj()
    getattr(func_def.Print, static_name)()


if __name__ == '__main__':
    main()
