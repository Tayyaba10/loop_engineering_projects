# def get_last_n_items(items, n):
#     """Return the last n items from a list."""
#     return items[-n:]

# def get_last_n_items(items, n):
#     """Return the last n items from a list."""
#     return items[-n - 1:]

def get_last_n_items(items, n):
    """Return the last n items from a list. Fixed the off-by-one bug."""
    return items[-n:]