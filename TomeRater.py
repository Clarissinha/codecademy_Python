class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        pass

    def change_email(self, address):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other_user):
        pass
