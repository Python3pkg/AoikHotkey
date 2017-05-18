# coding: utf-8
"""
Pytest plugin that filters collected test items.
"""



def pytest_collection_modifyitems(items, config):
    """
    Filter given test items.

    This is a hook function called by `pytest`.

    :param items: Test items list.

    :param config: Config object.

    :return: None.
    """
    # Do nothing
