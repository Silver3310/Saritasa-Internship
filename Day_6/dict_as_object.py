# -*- coding: utf-8 -*-
"""DictAsClass

This module demonstrates the implementation of a dict as a class with
attribute access control. You can use none of them, some of them or all of
them. When you try to do sth that you don't have access for this module throws
an AttributeError exception.

Example:
    ball = DictAsClass(
            ball_dict,
            add=True,
            change=False
        )

    ball.new_attribute = 'red'
    print(ball.color)

        |red

    ball.new_attribute = 'green'

        |AttributeError: Access is denied, you have no permission to change

"""


class DictAsClass:
    """The class that represents a dict as a class"""

    def __init__(
            self,
            dict_,
            change=False,
            add=False,
            delete=False
    ):
        self.data = dict()
        # Here we initialize our dictionary, this function checks if there
        # are subdictionaries and add them too as DictFactories
        self.init_dict(
            self.data,
            dict_,
            change,
            add,
            delete
        )

        # save our permissions
        self._change = change
        self._del = delete
        self._add = add

    @staticmethod
    def init_dict(in_dict, out_dict, *args):
        for k in out_dict:
            # if we have a subdict
            if isinstance(out_dict[k], dict):
                # add it as a DictFactory
                in_dict[k] = DictAsClass(out_dict[k], *args)
            # if we have a tuple or list
            elif isinstance(out_dict[k], (list, tuple)):
                list_ = []
                for v in out_dict[k]:
                    if isinstance(v, dict):
                        list_.append(DictAsClass(v))
                    else:
                        list_.append(v)
                        in_dict[k] = list_
            else:
                in_dict[k] = out_dict[k]

    def __getattr__(self, key):
        """Method that allows a user to access an item"""
        return self.data[key]

    def __setattr__(self, key, value):
        """Method that decides whether a user can change or add an item
        or not"""
        try:
            if key in self.__dict__['data']:
                if not self._change:
                    raise AttributeError(
                        'Access is denied, you have no permission to change'
                    )
                else:
                    self.data[key] = value
            else:
                if not self._add:
                    raise AttributeError(
                        'Access is denied, you have no permission to add'
                    )
                else:
                    self.data[key] = value
        except KeyError:
            super().__setattr__(key, value)

    def __delattr__(self, key):
        """Method that decides whether a user can delete the item or not"""
        if self._del:
            del self.data[key]
            print(f"'{key}' is removed successfully")
        else:
            raise AttributeError(
                'Access is denied, you have no permission to delete'
            )

    def __repr__(self):
        result_str = [each for each in self.data]
        return ', '.join(result_str)


def main():
    pass


if __name__ == "__main__":
    main()
