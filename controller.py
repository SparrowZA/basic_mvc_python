from view import ViewInterface
from model import ModelInterface
import mvc_exceptions as mvc_exc

class Controller(object):
    def __init__(self, model: ModelInterface, view: ViewInterface):
        self._model: ModelInterface = model
        self._view: ViewInterface = view
    
    def show_items(self, bullet_points:bool=False):
        items = self._model.read_items()
        item_type = self._model.item_type

        if bullet_points:
            self._view.show_bullet_point_list(item_type, items)
        else:
            self._view.show_number_point_list(item_type, items)
    
    def show_item(self, item_name: str):
        try:
            item = self._model.read_item(item_name)
            item_type = self._model.item_type
            self._view.show_item(item_type, item_name, item)
        except mvc_exc.ItemNotStored as e:
            self._view.display_missing_item_error(item_name, e)
    
    def insert_item(self, name: str, price: int, quantity:int):
        assert price > 0, "price must be greater than 0"
        assert quantity > 0, "quantity must be greater than 0"

        item_type = self._model.item_type
        try:
            self._model.create_item(name, price, quantity)
            self._view.display_item_stored(name, item_type)
        except mvc_exc.ItemAlreadyStored as e:
            self._view.display_item_already_stored_error(name, item_type, e)
    
    def update_item(self, name: str, price: int, quantity:int):
        assert price > 0, "price must be greater than 0"
        assert quantity > 0, "quantity must be greater than 0"

        item_type = self._model.item_type
        try:
            older = self._model.read_item(name)
            self._model.update_item(name, price, quantity)
            self._view.display_item_updated(name, older['price'], 
                                            older['quantity'], price, quantity
                                            )
        except mvc_exc.ItemNotStored as e:
            self._view.display_item_not_yet_stored_error(name, item_type, e)
    
    def update_item_type(self, new_item_type: str):
        old_item_type = self._model.item_type
        self._model.item_type = new_item_type
        self._view.display_change_item_type(old_item_type, new_item_type)
    
    def delete_item(self, name: str):
        item_type = self._model.item_type
        try:
            self._model.delete_item(name)
            self._view.display_item_deletion(name)
        except mvc_exc.ItemNotStored as e:
            self._view.display_item_not_yet_stored_error(name, item_type, e)