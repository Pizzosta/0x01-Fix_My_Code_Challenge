#!/usr/bin/python3
"""
User class Module
"""


class User():
    """ User class  """

    def __init__(self):
        """ Initializes a new instance of the User class """
        self.__email = None

    @property
    def email(self):
        """ Getter method for the email address """
        return self.__email

    @email.setter
    def email(self, value):
        """ Setter method for the email address """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
