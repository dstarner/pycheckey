import unittest

from pycheckey import KeyEnsurer


class TestKeyEnsurer(unittest.TestCase):

    def test_key_exists_basic(self):
        """Test that the basic key exists functionality works
        """
        data = {
            'hello': 'world'
        }
        self.assertTrue(
            KeyEnsurer(
                data=data, required_keys=[]
            ).key_exists(data, 'hello')
        )

        self.assertFalse(
            KeyEnsurer(
                data=data, required_keys=[]
            ).key_exists(data, 'world')
        )

    def test_key_exists_nested(self):
        """Test that key_exists works on basic nested keys
        """
        data = {
            'hello': {
                'world': '15'
            }
        }
        self.assertTrue(
            KeyEnsurer(
                data=data,
                required_keys=['hello.world']
            ).validate()
        )

        self.assertFalse(
            KeyEnsurer(
                data=data,
                required_keys=['hello.false']
            ).validate()
        )

    def test_validate(self):
        data = {
            'hello': {
                'world': '15'
            },
            'world': 'hello'
        }
        self.assertTrue(
            KeyEnsurer(
                data=data,
                required_keys=['hello.world', 'world']
            ).validate()
        )