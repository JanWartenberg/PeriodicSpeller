""" Extend the jinja templates by convenience methods. """


def is_list(value):
    return isinstance(value, list)


def is_str(value):
    return isinstance(value, str)


def extend_filters(app):
    app.jinja_env.filters["is_list"] = is_list
    app.jinja_env.filters["is_str"] = is_str
