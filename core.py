"""
- Core module functions
    Criar id da url encurtada
    Buscar url encontrada

Example
>>> shortened_url('http://www.globo.com')
'04c235ce82'

>>> shortened_url('http://www.google.com')
'738ddf35b3'

"""

from hashlib import sha1


def shortened_url(url: str) -> str:
    encoded_url = url.encode('UTF-8')
    digest = sha1(encoded_url).hexdigest()
    return digest[:10]