class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('This email has been updated.')

    def __repr__(self):
        return 'User: {}, email: {}, books read: {}.'.format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.email == other_user.email):
            print('Identical users!')
            return True
        else:
            print('These are different users!')
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        books_count = 0
        rtg_summ = 0
        for rtg in self.books.values():
            if rtg:
                books_count += 1
                rtg_summ += rtg
                avgrtg = rtg_summ / books_count
        return avgrtg


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print('This book ISBN has been updated.')

    def add_rating(self, rating):
        if rating:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
        else:
            print('Invalid Rating')

    def get_average_rating(self):
        add = 0
        for rating in self.ratings:
            add += rating
            average = add / len(self.ratings)
        return average

    def __eq__(self, other_user):
        if (self.title == other_user.title) and (self.isbn == other_user.isbn):
            print('Identical books!')
            return True

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '{} by {}.'.format(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return '{}, a {} manual on {}.'.format(self.title, self.level, self. subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        print('New book added.')
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        print('New novel added.')
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        print('New non-fiction book added.')
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users.keys():
            print('No user with email: {email}.'.format(email=email))
        else:
            user = self.users.get(email)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        most_read_book = None
        num_times = 0
        for key, value in self.books.items():
            if value > num_times:
                num_times = value
                most_read_book = key
        return most_read_book

    def highest_rated_book(self):
        high_rate_book = None
        high_rate = 0
        for book in self.books:
            highest_average = book.get_average_rating()
            if highest_average > high_rate:
                high_rate = highest_average
                high_rate_book = book
        return high_rate_book

    def most_positive_user(self):
        positive_user = None
        highest_rating = 0
        for user in self.users.values():
            avg_user_rating = user.get_average_rating()
            if avg_user_rating > highest_rating:
                avg_user_rating = highest_rating
                positive_user = user
        return positive_user


Tome_Rater = TomeRater()

# Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel(
    "Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction(
    "Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction(
    "Computing Machinery and Intelligence", "AI", "advanced", 1111193)
novel2 = Tome_Rater.create_novel(
    "The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel(
    "There Will Come Soft Rains", "Ray Bradbury", 10001000)

# Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

# Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu",
                    user_books=[book1, novel1, nonfiction1])

# Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)

# Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

# print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
