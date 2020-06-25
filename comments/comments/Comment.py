# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Comment(Component):
    """A Comment component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; required): The ID used to identify this component in Dash callbacks.
- value (string; optional): The value displayed in the input.
- className (string; optional): className to select div with CSS"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, value=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'className']
        self._type = 'Comment'
        self._namespace = 'comments'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Comment, self).__init__(**args)
