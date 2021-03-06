# This file is part of EbookLib.
# Copyright (c) 2013 Aleksandar Erkalovic <aerkalov@gmail.com>
#
# EbookLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# EbookLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with EbookLib.  If not, see <http://www.gnu.org/licenses/>.

import io
from lxml import html, etree

def debug(obj):
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(obj)

def parse_string(s):

    if isinstance(s, str):
        encoded_string = s.encode('utf-8')
    else:
        encoded_string = s    

    encoded_string = encoded_string.replace(b"\r\n", b"\n")
    try:
        tree = etree.parse(io.BytesIO(encoded_string))
        
    except:
        raise Exception('Can\'t parse encoded string')
        pass

    return tree

def parse_html_string(s):
    from lxml import html

    utf8_parser = html.HTMLParser(encoding='utf-8')

    html_tree = html.document_fromstring(s , parser=utf8_parser)

    return html_tree

def parse_xhtml_string(s):
    if isinstance(s, bytes):
        s = s.replace(b"\r\n", b"\n")

    parser = etree.XMLParser(encoding='utf-8')
    use_html_parser = True
    if use_html_parser:
        parser = html.HTMLParser(encoding='utf-8')
    tree = etree.fromstring(s, parser=parser)
    return tree