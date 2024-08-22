from django import template
from django.urls import resolve
from ..models import Menu, MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent')
    return MenuTree(menu_items, menu_name).render()

class MenuTree:
    def __init__(self, items, menu_name):
        self.items = items
        self.menu_name = menu_name
        self.active_url = resolve('/').url_name

    def build_tree(self):
        tree = {}
        for item in self.items:
            if item.parent is None:
                tree[item] = []
        for item in self.items:
            if item.parent:
                tree.setdefault(item.parent, []).append(item)
        return tree

    def render(self):
        tree = self.build_tree()
        return self.render_node(None, tree)

    def render_node(self, parent, tree):
        html = []
        for node in tree.get(parent, []):
            url = node.get_absolute_url()
            is_active = url == resolve('/').url
            is_expanded = is_active or any(self.is_descendant_active(child) for child in tree.get(node, []))
            html.append('<li class="{}">'.format('active' if is_active else ''))
            html.append('<a href="{}">{}</a>'.format(url, node.title))
            if is_expanded:
                html.append('<ul>')
                html.append(self.render_node(node, tree))
                html.append('</ul>')
            html.append('</li>')
        return ''.join(html)
    
    def is_descendant_active(self, node):
        url = node.get_absolute_url()
        return url == resolve('/').url
    
