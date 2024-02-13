import unittest
import sys
import os
from flask import Flask

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.logs.log_individual import get_log_individual


class TestLogIndividual(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        self.test_log_id = 'test_log'
        self.log_file_path = f'logs/{self.test_log_id}.log'

        with open(self.log_file_path, 'w') as f:
            f.write('This is a test log file.')

    def tearDown(self):
        os.remove(self.log_file_path)

    def test_get_log_individual_success(self):
        with self.app.app_context():
            response = get_log_individual(self.test_log_id)
            self.assertEqual(response.status_code, 200)
            self.assertIn('This is a test log file.', response.get_data(as_text=True))

    def test_get_log_individual_not_found(self):
        with self.app.app_context():
            with self.assertRaises(Exception) as context:
                get_log_individual('nonexistent_log')
            self.assertTrue('404' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
