import unittest

from app.components.ConfigurationComponent import ConfigurationComponent


class TestConfigurationComponent(unittest.TestCase):

    def setUp(self):
        pass

    def test_configuration(self):
        configuration = ConfigurationComponent()
        self.assertEqual("test", configuration.name)





