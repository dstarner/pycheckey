from dataclasses import dataclass


@dataclass
class KeyPairEnsurer:
    """Dataclass that allows to deeply check that keys exist.
    """

    data: typing.Union[typing.Dict, 'collections.OrderedDict[str, typing.Any]']
    required_keys: typing.List[str]

    def key_exists(self, data, key):
        rest = ''
        if '.' in key:
            key, rest = key.split('.', 1)
        if key not in data:
            raise BuildException(f'"{key}" not found in the configuration.')
        if rest:
            self.key_exists(data[key], rest)

    def validate(self):
        for key in self.required_keys:
            self.key_exists(self.data, key)