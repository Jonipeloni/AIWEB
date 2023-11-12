import os

from whoosh import index
from whoosh.fields import *

# Here, the structure of index entries is defined. You can add more fields with metadata, computed values etc.,
# and use them for searching and ranking.
# We only use a title and a text.
#
# The "stored" attribute is used for all parts that we want to be able to fully retrieve from the index

schema = Schema(title=TEXT(stored=True), url=ID, content=TEXT)

def get_index():
    if not os.path.exists('indexdir'):
        os.mkdir('indexdir')
        return index.create_in("indexdir", schema)
    return index.open_dir("indexdir")


# Create an index in the directory indexdir (the directory must already exist!)
#ix = create_in("indexdir", schema)
#writer = ix.writer()
