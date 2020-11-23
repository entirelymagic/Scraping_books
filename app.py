import requests

from pages.all_books_page import AllBooksPage
PAGE_URL = 'http://books.toscrape.com'

page_content = requests.get(PAGE_URL).content
page = AllBooksPage(page_content)

books = page.books
for book in books:
    print(book)

