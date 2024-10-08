from django import template
from django.urls import resolve
from ..models import Menu, MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').prefetch_related('children')
    return MenuTree(menu_items, request).render()

class MenuTree:
    def __init__(self, items, request):
        self.items = items
        self.request = request
        self.active_url = request.path_info  # Получаем текущий URL

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
            is_active = url == self.request.path_info
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
        return url == self.request.path_info