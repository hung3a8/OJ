from django import template
from lxml import html

from judge import lxml_tree
from judge.utils.texoid import get_texoid_url

register = template.Library()


@register.filter(is_safe=True)
def latex_math(text):
    tree = lxml_tree.fromstring(text)
    for latex in tree.xpath('.//latex'):
        img = html.Element('img')
        img.set('src', get_texoid_url(latex.text))
        latex.getParent().replace(latex, img)
    return tree