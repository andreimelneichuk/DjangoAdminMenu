from django.test import TestCase
from django.urls import reverse
from .models import Menu, MenuItem

class MenuTest(TestCase):
    
    def setUp(self):
        # Создаем тестовое меню
        self.menu = Menu.objects.create(name='Main Menu')
        
        # Создаем элементы меню
        self.parent_item = MenuItem.objects.create(
            menu=self.menu,
            title='Home',
            url='menu/home/',
            order=1
        )
        
        self.child_item = MenuItem.objects.create(
            menu=self.menu,
            parent=self.parent_item,
            title='About',
            url='menu/about/',
            order=2
        )

    def test_menu_structure(self):
        """Проверка структуры меню."""
        self.assertEqual(self.menu.items.count(), 2)
        self.assertEqual(self.parent_item.children.count(), 1)

    def test_active_menu_item(self):
        """Проверка, что активный элемент меню помечен классом 'active'."""
        # Используем путь, который существует в тестовых данных
        response = self.client.get(self.parent_item.url)
        self.assertEqual(response.status_code, 200)
        
        # Проверяем, что в HTML присутствует класс 'active' у соответствующего элемента
        self.assertContains(response, 'class="active"')