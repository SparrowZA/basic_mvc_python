from controller import Controller
from view import View
from model import ModelBasic

def main():
    items = [
        {'name': 'bread', 'price': 1, 'quatity': 1},
        {'name':'milk', 'price': 2, 'quantity': 2},
        {'name': 'eggs', 'price': 3, 'quantity': 3}
    ]

    controller: Controller = Controller(model=ModelBasic(items),
                                        view=View)
    print()
    controller.show_items(True)
    print()


if __name__ == "__main__":
    main()