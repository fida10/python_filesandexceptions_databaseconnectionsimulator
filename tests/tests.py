import unittest
from src.ans import database_connection_simulator
from unittest.mock import patch
import random


class TestDatabaseConnectionSimulator(unittest.TestCase):
    def test_successful_connection(self):
        with patch('random.choice', return_value=None):
            self.assertEqual(database_connection_simulator(),
                             'Connected successfully')

    def test_connection_error(self):
        with patch('random.choice', side_effect=[ConnectionError, ConnectionError, ConnectionError]):
            self.assertEqual(database_connection_simulator(),
                             'Failed to connect: ConnectionError')

    def test_timeout_error(self):
        with patch('random.choice', side_effect=[TimeoutError, TimeoutError, TimeoutError]):
            self.assertEqual(database_connection_simulator(),
                             'Failed to connect: TimeoutError')


if __name__ == '__main__':
    unittest.main()
