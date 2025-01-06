from helpers import validate_attribute

class Article:

    all = []

    def __init__(self, author, magazine, title):
        validate_attribute(title, str, 5, 50)
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    def __repr__(self):
        return (
            f"<Article: title='{self.title}', author='{self.author.name}', "
            f"magazine='{self.magazine.name}'>"
        )

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        validate_attribute(author, Author)
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        validate_attribute(magazine, Magazine)
        self._magazine = magazine

class Author:
    def __init__(self, name):
        validate_attribute(name, str, 1)
        self._name = name   

    def __repr__(self):
        return f"<Author: name='{self.name}'>"

    @property
    def name(self):
        return self._name

    def articles(self):
        return [item for item in Article.all if item.author == self]

    def magazines(self):
        return list(set(item.magazine for item in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(item.category for item in self.magazines())) or None

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"<Magazine: name='{self.name}', category='{self.category}'>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        validate_attribute(name, str, 2, 16)
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        validate_attribute(category, str, 1)
        self._category = category

    def articles(self):
        return [item for item in Article.all if item.magazine == self]

    def articles_by_author(self, author):
        return [item for item in self.articles() if item.author == author]

    def contributors(self):
        return list(set(item.author for item in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        return list(set(
            item for item in self.contributors()
            if len(self.articles_by_author(item)) > 2
        )) or None