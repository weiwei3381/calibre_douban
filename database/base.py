# coding:utf-8
from peewee import *

database = SqliteDatabase('D:\\Calire_书库\\metadata.db', **{})
database.connect()



class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Authors(BaseModel):
    link = TextField(constraints=[SQL("DEFAULT '""'")])
    name = TextField(unique=True)
    sort = TextField(null=True)

    class Meta:
        table_name = 'authors'


class Books(BaseModel):
    author_sort = TextField(index=True, null=True)
    flags = IntegerField(constraints=[SQL("DEFAULT 1")])
    has_cover = BooleanField(constraints=[SQL("DEFAULT 0")], null=True)
    isbn = TextField(constraints=[SQL("DEFAULT '""'")], null=True)
    last_modified = UnknownField(constraints=[SQL("DEFAULT '2000-01-01 00:00:00+00:00'")])  # TIMESTAMP
    lccn = TextField(constraints=[SQL("DEFAULT '""'")], null=True)
    path = TextField(constraints=[SQL("DEFAULT '""'")])
    pubdate = UnknownField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)  # TIMESTAMP
    series_index = FloatField(constraints=[SQL("DEFAULT 1.0")])
    sort = TextField(index=True, null=True)
    timestamp = UnknownField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)  # TIMESTAMP
    title = TextField(constraints=[SQL("DEFAULT 'Unknown'")])
    uuid = TextField(null=True)

    class Meta:
        table_name = 'books'


class BooksAuthorsLink(BaseModel):
    author = IntegerField(index=True)
    book = IntegerField(index=True)

    class Meta:
        table_name = 'books_authors_link'
        indexes = (
            (('book', 'author'), True),
        )


class BooksLanguagesLink(BaseModel):
    book = IntegerField(index=True)
    item_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    lang_code = IntegerField(index=True)

    class Meta:
        table_name = 'books_languages_link'
        indexes = (
            (('book', 'lang_code'), True),
        )


class BooksPluginData(BaseModel):
    book = IntegerField()
    name = TextField()
    val = TextField()

    class Meta:
        table_name = 'books_plugin_data'
        indexes = (
            (('book', 'name'), True),
        )


class BooksPublishersLink(BaseModel):
    book = IntegerField(unique=True)
    publisher = IntegerField(index=True)

    class Meta:
        table_name = 'books_publishers_link'


class BooksRatingsLink(BaseModel):
    book = IntegerField(index=True)
    rating = IntegerField(index=True)

    class Meta:
        table_name = 'books_ratings_link'
        indexes = (
            (('book', 'rating'), True),
        )


class BooksSeriesLink(BaseModel):
    book = IntegerField(unique=True)
    series = IntegerField(index=True)

    class Meta:
        table_name = 'books_series_link'


class BooksTagsLink(BaseModel):
    book = IntegerField(index=True)
    tag = IntegerField(index=True)

    class Meta:
        table_name = 'books_tags_link'
        indexes = (
            (('book', 'tag'), True),
        )


class Comments(BaseModel):
    book = IntegerField(unique=True)
    text = TextField()

    class Meta:
        table_name = 'comments'


class ConversionOptions(BaseModel):
    book = IntegerField(index=True, null=True)
    data = BlobField()
    format = TextField(index=True)

    class Meta:
        table_name = 'conversion_options'
        indexes = (
            (('format', 'book'), True),
        )


class CustomColumn1(BaseModel):
    book = IntegerField(null=True, unique=True)
    value = BooleanField()

    class Meta:
        table_name = 'custom_column_1'


class CustomColumn2(BaseModel):
    book = IntegerField(null=True, unique=True)
    value = FloatField()

    class Meta:
        table_name = 'custom_column_2'


class CustomColumns(BaseModel):
    datatype = TextField()
    display = TextField(constraints=[SQL("DEFAULT '\"{}\"'")])
    editable = BooleanField(constraints=[SQL("DEFAULT 1")])
    is_multiple = BooleanField(constraints=[SQL("DEFAULT 0")])
    label = TextField(unique=True)
    mark_for_delete = BooleanField(constraints=[SQL("DEFAULT 0")])
    name = TextField()
    normalized = BooleanField()

    class Meta:
        table_name = 'custom_columns'


class Data(BaseModel):
    book = IntegerField(index=True)
    format = TextField(index=True)
    name = TextField()
    uncompressed_size = IntegerField()

    class Meta:
        table_name = 'data'
        indexes = (
            (('book', 'format'), True),
        )


class Feeds(BaseModel):
    script = TextField()
    title = TextField(unique=True)

    class Meta:
        table_name = 'feeds'


class Identifiers(BaseModel):
    book = IntegerField()
    type = TextField(constraints=[SQL("DEFAULT '\"isbn\"'")])
    val = TextField()

    class Meta:
        table_name = 'identifiers'
        indexes = (
            (('book', 'type'), True),
        )


class Languages(BaseModel):
    lang_code = TextField(unique=True)

    class Meta:
        table_name = 'languages'


class LastReadPositions(BaseModel):
    book = IntegerField(index=True)
    cfi = TextField()
    device = TextField()
    epoch = FloatField()
    format = TextField()
    pos_frac = FloatField(constraints=[SQL("DEFAULT 0")])
    user = TextField()

    class Meta:
        table_name = 'last_read_positions'
        indexes = (
            (('user', 'device', 'book', 'format'), True),
        )


class LibraryId(BaseModel):
    uuid = TextField(unique=True)

    class Meta:
        table_name = 'library_id'


class MetadataDirtied(BaseModel):
    book = IntegerField(unique=True)

    class Meta:
        table_name = 'metadata_dirtied'


class Preferences(BaseModel):
    key = TextField(unique=True)
    val = TextField()

    class Meta:
        table_name = 'preferences'


class Publishers(BaseModel):
    name = TextField(unique=True)
    sort = TextField(null=True)

    class Meta:
        table_name = 'publishers'


class Ratings(BaseModel):
    rating = IntegerField(null=True, unique=True)

    class Meta:
        table_name = 'ratings'


class Series(BaseModel):
    name = TextField(unique=True)
    sort = TextField(null=True)

    class Meta:
        table_name = 'series'


class SqliteSequence(BaseModel):
    name = UnknownField(null=True)  #
    seq = UnknownField(null=True)  #

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False


class Tags(BaseModel):
    name = TextField(index=True)

    class Meta:
        table_name = 'tags'
