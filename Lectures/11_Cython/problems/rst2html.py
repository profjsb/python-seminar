# -*- coding: utf-8 -*-

#!/opt/local/bin/python

# Author: David Goodger
# Contact: goodger@python.org
# Revision: $Revision: 3901 $
# Date: $Date: 2005-09-25 17:49:54 +0200 (Sun, 25 Sep 2005) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML.
"""

# ----------------------------------------------------------------------------
"""
    The Pygments reStructuredText directive
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This fragment is a Docutils_ 0.4 directive that renders source code
    (to HTML only, currently) via Pygments.

    To use it, adjust the options below and copy the code into a module
    that you import on initialization.  The code then automatically
    registers a ``sourcecode`` directive that you can use instead of
    normal code blocks like this::

        .. sourcecode:: python

            My code goes here.

    If you want to have different code styles, e.g. one with line numbers
    and one without, add formatters with their names in the VARIANTS dict
    below.  You can invoke them instead of the DEFAULT one by using a
    directive option::

        .. sourcecode:: python
            :linenos:

            My code goes here.

    Look at the `directive documentation`_ to get all the gory details.

    .. _Docutils: http://docutils.sf.net/
    .. _directive documentation:
       http://docutils.sourceforge.net/docs/howto/rst-directives.html

    :copyright: 2007 by Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

# Options
# ~~~~~~~

# Set to True if you want inline CSS styles instead of classes
INLINESTYLES = True

from pygments.formatters import HtmlFormatter

# The default formatter
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES, style='borland')
# One of 'manni', 'perldoc', 'borland', 'colorful', 'default',
#  'murphy', 'trac', 'fruity', 'autumn', 'bw', 'emacs', 'pastie',
#  'friendly', 'native'


# Add name -> formatter pairs for every variant you want to use
VARIANTS = {
    'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
}

from docutils import nodes
from docutils.parsers.rst import directives

from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer

def pygments_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):
    try:
        lexer = get_lexer_by_name(arguments[0])
    except ValueError:
        # no lexer found - use the text one instead of an exception
        lexer = TextLexer()
    # take an arbitrary option if more than one is given
    formatter = options and VARIANTS[options.keys()[0]] or DEFAULT
    parsed = highlight(u'\n'.join(content), lexer, formatter)
    return [nodes.raw('', parsed, format='html')]

pygments_directive.arguments = (1, 0, 1)
pygments_directive.content = 1
pygments_directive.options = dict([(key, directives.flag) for key in VARIANTS])

directives.register_directive('sourcecode', pygments_directive)

# ----------------------------------------------------------------------------

import math_directive
math_directive.register()

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description

description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='html', description=description)
