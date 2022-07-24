# =================================================================
#   Vishwas Sastry
#   CS361 | Summer 2022
#   Microservice - String Validator
#   Remote Procedure Call: Initiate Server
#   References:
#       - https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html
# =================================================================
import rpyc
import re

PORT = 3776

class PatternValidator(rpyc.Service):
    def on_connect(self, conn):
        print("Thread Initiated")

    def on_disconnect(self, conn):
        print("Thread Closed")

    def exposed_digitExists(self, input):
        compile = re.compile('\d')
        return bool(compile.search(input))

    def exposed_lowerExists(self, input):
        compile = re.compile('[a-z]')
        return bool(compile.search(input))

    def exposed_upperExists(self, input):
        compile = re.compile('[A-Z]')
        return bool(compile.search(input))

    def exposed_symbolExists(self, input):
        compile = re.compile('!@#$%^&*()-_=+')
        return bool(compile.search(input))

    def exposed_lenValid(self, input, length):
        return bool(len(input) >= length)

    # Reference: https://uibakery.io/regex-library/password-regex-python
    # Method checks input requirements according to Mark Jordan's specific password requirements
    # Built for simplicity -- exposed_passParameters() can be used for variable requirements
    def exposed_passChecker(self, input):
        pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*()-_=+]).{12,}$"
        return bool(re.match(pattern, input))


if __name__ == "__main__":
    print("\nServer Live. Waiting for Requests. Press Ctrl + C to cancel")
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PatternValidator, port=PORT)
    t.start()
