# =================================================================
#   Vishwas Sastry
#   CS361 | Summer 2022
#   Microservice - String Validator
#   CLIENT EXAMPLE
#   References:
#       - https://rpyc.readthedocs.io/en/latest/tutorial/tut3.html
# =================================================================
import rpyc

PORT = 3776

connection = rpyc.connect("localhost", PORT)

noDigits = "HelloWorld!!!"
noLower = "HELLOWORLD123!"
noUpper = "helloworld123_"
tooShort = "hello1!"
correct = "HelloWorld123!@#"

print("\n")
print("noDigits", connection.root.digitExists(noDigits)) # print False | no digits in string
print("HasDigits", connection.root.digitExists(noLower)) # print True | string has digits
print("noLower", connection.root.lowerExists(noLower)) # print False | no lowercase in string
print("HasLower", connection.root.lowerExists(noUpper)) # print True | string has lowercase
print("noUpper", connection.root.upperExists(noUpper)) # print False | no uppercase in string
print("HasUpper", connection.root.upperExists(noLower)) # print True | string has uppercase
print("tooShort", connection.root.lenValid(tooShort, 12)) # print False | string not >= 12
print("CorrectLength", connection.root.lenValid(noDigits, 12)) # print True | string >= 12

# passChecker() returns True if input: length >= 12, has digits, has lowercase, has uppercase, has symbol from !@#$%^&*()-_=+
print("correct", connection.root.passChecker(correct)) # print True
print("direct_correct", connection.root.passChecker("He11()W()r1d")) # print True
print("\n")
