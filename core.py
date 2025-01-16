"""
- Core module functions
    Criar id da url encurtada
    Buscar url encontrada

Example
>>> shortened_url('http://www.globo.com')
'04c235ce82'

>>> shortened_url('http://www.google.com')
'738ddf35b3'


>>> create_url('http://www.globo.com')
'04c235ce82'

>>> create_url('http://www.google.com')
'738ddf35b3'

>>> search_url('04c235ce82')
'http://www.globo.com'

>>> search_url('738ddf35b3')
'http://www.google.com'

>>> search_url('foobar')


"""

from hashlib import sha1
import db


def shortened_url(url: str) -> str:
    encoded_url = url.encode('UTF-8')
    digest = sha1(encoded_url).hexdigest()
    return digest[:10]

def create_url(url: str) -> str:
    return db.create(shortened_url(url), url)

def search_url(id: str) -> str | None:
    return db.find(id)