from database.base import Books
from database.base import CustomColumn2
from douban.search import get_book_url, get_douban_rate

def clear_input(title):
    if '(' in title:
        title = title.split('(')[0]
    if '（' in title:
        title = title.split('（')[0]
    return title.strip()

for book in Books.select():
    rate_column_result = CustomColumn2.select().where(CustomColumn2.book == book.id)
    if len(rate_column_result) > 0:
        continue
    title = clear_input(book.title)
    print("%s is processing..." % title)
    try:
        url = get_book_url(title)
        if url:
            rate = get_douban_rate(url)
            rate_column = CustomColumn2(book = book.id, value = rate)
            rate_column.save()
            print("%s has rate [%s]" %(title, rate))
    except:
        print("error, jump to next.")
        pass
