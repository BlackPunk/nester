"""This is the “nester.py" module, and it provides one function called
print_list() which prints lists that may or may not include nested lists."""

# example of nested list
# movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
#             ["Graham Chapman", ["Michael Palin", "John Cleese",
#                 "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


def print_list(the_list):
    """This function takes positional argument called "the_list", which is any Python
    list (of, possibly, nested list). Each data item in the provided list is (recursively)
    printed to the screen on its own line."""
    for item in the_list:
        if isinstance(item, list):
            print_list(item)
        else:
            print(item)
