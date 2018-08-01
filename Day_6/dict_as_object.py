# -*- coding: utf-8 -*-
"""DictFactory

This module demonstrates the implementation of a dict as a class with
attribute access control. You can use none of them, some of them or all of
them. In order to change, add and delete a dict's attributes you also need an
ability to read these attributes. When you try to do sth that you don't have
access for this module throws an AttributeError exception.

Example:
    ball = DictFactory(
            ball_dict,
            read=True,
            add=True,
            change=False
        )

    ball.new_attribute = 'red'
    print(ball.color)

        |red

    ball.new_attribute = 'green'

        |AttributeError: Access is denied, you have no permission to change

"""


class DictFactory:
    """The class that represents a dict as a class"""

    def __init__(
            self,
            dict_,
            read=False,
            change=False,
            add=False,
            delete=False
    ):
        self.dict = dict()
        # Here we initialize our dictionary, this function checks if there
        # are subdictionaries and add them too as DictFactories
        self.init_dict(
            self.dict,
            dict_,
            read,
            change,
            add,
            delete
        )

        # save our permissions
        self._read = read
        self._change = change
        self._del = delete
        self._add = add

    @staticmethod
    def init_dict(in_dict, out_dict, *args):
        for k in out_dict:
            # if we have a subdict
            if isinstance(out_dict[k], dict):
                # add it as a DictFactory
                in_dict[k] = DictFactory(out_dict[k], *args)
            # if we have a tuple or list
            elif isinstance(out_dict[k], (list, tuple)):
                list_ = []
                for v in out_dict[k]:
                    if isinstance(v, dict):
                        list_.append(DictFactory(v))
                    else:
                        list_.append(v)
                        in_dict[k] = list_
            else:
                # if we just have a value, we add it as a dictionary
                # dict(default=our_dict[k]
                if k != 'default':
                    in_dict[k] = DictFactory(dict(default=out_dict[k]), *args)
                else:
                    in_dict[k] = out_dict[k]

    def __getattr__(self, key):
        """Method that decides whether a user can access an item or not"""
        if self.__dict__['_read']:
                return self.__dict__['dict'][key]
        else:
            raise AttributeError(
                f'Access is denied, you have no permission to read'
            )

    def __setattr__(self, key, value):
        """Method that decides whether a user can change or add an item
        or not"""
        try:
            if key in self.__dict__['dict']:
                if not self.__dict__['_change']:
                    raise AttributeError(
                        'Access is denied, you have no permission to change'
                    )
                else:
                    self.__dict__['dict'][key] = DictFactory(dict(
                        default=value),
                        self._read,
                        self._change,
                        self._add,
                        self._del
                    )
            else:
                if not self.__dict__['_add']:
                    raise AttributeError(
                        'Access is denied, you have no permission to add'
                    )
                else:
                    self.__dict__['dict'][key] = DictFactory(dict(
                        default=value),
                        self._read,
                        self._change,
                        self._add,
                        self._del
                    )
        except KeyError:
            super().__setattr__(key, value)

    def __delattr__(self, key):
        """Method that decides whether a user can delete the item or not"""
        if self._del:
            del self.__dict__['dict'][key]
            print(f"'{key}' is removed successfully")
        else:
            raise AttributeError(
                'Access is denied, you have no permission to delete'
            )

    def __str__(self):
        """Method that represents an item in a readable format"""
        # if we have only one value so that means it's a default value
        if len(self.__dict__['dict'].keys()) == 1 and \
                'default' in self.__dict__['dict'].keys():
            return str(self.__dict__['dict']['default'])
        # in another case, we output all values
        else:
            result_str = [each for each in self.__dict__['dict']
                          if not each == 'default']
            if 'default' in self.__dict__['dict']:
                result_str.append(str(self.__dict__['dict']['default']))
            return '|' + ', '.join(result_str) + '|'


def main():
    pass


if __name__ == "__main__":
    main()
