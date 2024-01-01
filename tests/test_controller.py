import unittest
from unittest.mock import Mock
from controller import Controller
from mvc_exceptions import ItemAlreadyStored, ItemNotStored


class TestController(unittest.TestCase):
    def setUp(self):
        self.model = Mock()
        self.view = Mock()
        self.controller = Controller(self.model, self.view)

    def test_show_items(self):
        self.controller.show_items()
        self.view.show_number_point_list.assert_called_once()

    def test_show_items_with_bullet_points(self):
        self.controller.show_items(bullet_points=True)
        self.view.show_bullet_point_list.assert_called_once()

    def test_show_item(self):
        self.controller.show_item('foo')
        self.view.show_item.assert_called_once()
    
    def test_show_item_item_not_stored(self):
        self.model.read_item.side_effect = ItemNotStored()
        self.controller.show_item('foo')
        self.view.display_missing_item_error.assert_called_once()

    def test_insert_item(self):
        self.controller.insert_item('foo', 1, 2)
        self.model.create_item.assert_called_once_with('foo', 1, 2)
        self.view.display_item_stored.assert_called_once()
    
    def test_insert_item_with_quantity_of_zero(self):
        with self.assertRaises(AssertionError):
            self.controller.insert_item('foo', 1, 0)

    def test_insert_item_with_price_of_zero(self):
        with self.assertRaises(AssertionError):
            self.controller.insert_item('foo', 0, 22)
    
    def test_insert_item_raise_item_already_stored(self):
        self.model.create_item.side_effect = ItemAlreadyStored()
        self.controller.insert_item('foo', 1442, 22)
        self.view.display_item_already_stored_error.assert_called_once()

    def test_update_item(self):
        # Arrange
        self.model.read_item.return_value = {'name': 'foo', 'price': 1, 'quantity': 2}
        # Act
        self.controller.update_item('foo', 1, 2)
        # Assert
        self.view.display_item_updated.assert_called_once()

    def test_update_item_price_less_than_zero(self):
        # Assert
        with self.assertRaises(AssertionError):
            self.controller.update_item('foo', -1, 2)
    
    def test_update_item_quantity_less_than_zero(self):
        # Assert
        with self.assertRaises(AssertionError):
            self.controller.update_item('foo', 124, -2)

    def test_update_item_raise_item_not_stored(self):
        # Arrange
        self.model.read_item.side_effect = ItemNotStored()
        # Act
        self.controller.update_item('foo', 1, 2)
        # Assert
        self.view.display_item_not_yet_stored_error.assert_called_once()

    def test_update_item_type(self):
        self.controller.update_item_type('new_type')
        self.view.display_change_item_type.assert_called_once()

    def test_delete_item(self):
        self.controller.delete_item('foo')
        self.model.delete_item.assert_called_with('foo')
        self.view.display_item_deletion.assert_called_with('foo')
    
    def test_delete_item_raise_item_not_stored(self):
        # Arrange
        self.model.delete_item.side_effect = ItemNotStored()
        # Act
        self.controller.delete_item('foo')
        # Assert
        self.view.display_item_not_yet_stored_error.assert_called_once()


if __name__ == '__main__':
    unittest.main()