import json
import pymongo
from mitmproxy import ctx


def response(flow):
    client = pymongo.MongoClient('localhost')
    db = client['dedao']
    collection = db['books']
    url = 'https://dedao.igetget.com/v3//discover/bookList'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            title = book.get('operating_title')
            author = book.get('book_author')
            data = {
                '书名': title,
                '作者': author,
                '封面': book.get('cover'),
                '简介': book.get('other_share_summary'),
                '价格': book.get('price')
            }
            ctx.log.info(str(data))
            collection.update({'书名': title, '作者': author}, {'$set': data}, True)




