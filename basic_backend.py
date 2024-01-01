from mvc_exceptions import ItemAlreadyStored, ItemNotStored


items = list()

def create_items(app_items):
    global items
    items = app_items

def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise ItemAlreadyStored(f'"{name}" already stored')
    else:
        items.append({"name": name, "price": price, "quantity": quantity})


def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise ItemNotStored(f'Can\'t read "{name}" because it was not stored')

def read_items():
    global items
    return [item for item in items]

def update_item(name, price, quantity):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {"name": name, "price": price, "quantity": quantity}
    else:
        raise ItemNotStored(f'Can\'t update "{name}" because it was not stored')

def delete_item(name):
    global items
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise ItemNotStored(f'Can\'t delete "{name}" because it was not stored')
