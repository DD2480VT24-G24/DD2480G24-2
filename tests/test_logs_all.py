import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.logs.logs_all import get_log_ids


class GetLogIdsTestCase(unittest.TestCase):
    def setUp(self):
        self.logs_dir = 'logs/'

        self.test_logs = ['test1.log', 'test2.log']
        for log in self.test_logs:
            with open(os.path.join(self.logs_dir, log), 'w') as f:
                f.write(f'Content for {log}')

        with open(os.path.join(self.logs_dir, 'not_a_log.txt'), 'w') as f:
            f.write('This is not a log file.')

    def tearDown(self):
        os.remove(os.path.join(self.logs_dir, 'test1.log'))
        os.remove(os.path.join(self.logs_dir, 'test2.log'))
        os.remove(os.path.join(self.logs_dir, 'not_a_log.txt'))

    def test_get_log_ids(self):
        log_ids = get_log_ids()
        expected_ids = [log[:-4] for log in self.test_logs]
        for expected_id in expected_ids:
            self.assertIn(expected_id, log_ids['ids'])

    def test_get_log_ids_filters_non_log_files(self):
        log_ids = get_log_ids()
        self.assertNotIn('not_a_log', log_ids['ids'])


if __name__ == '__main__':
    unittest.main()
