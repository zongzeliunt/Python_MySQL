
def do_foo_away(value):
    print ("foo away! " + str(value))



class Print():
    # normal method
    def do_foo(self):
        print ("foo!")

    # static method
    @staticmethod
    def static_foo():
        print ("static foo!")
