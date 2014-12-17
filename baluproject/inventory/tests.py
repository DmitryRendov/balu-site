# coding=utf-8
from django.test import TestCase
from inventory.models import Inventory

class InventoryTests(TestCase):
    """Inventory model tests."""

    def test_unicode(self):
        invobj = Inventory(name="Сад",description="Верхний уровень инвентаря")
        self.assertEquals(
            str(invobj),
            str('Сад Верхний уровень инвентаря'),
        )
