import unittest
from student import Student
from datetime import date, timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup--')
        self.student = Student('Mack', 'Deo')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):

        print('test_full_name')
        self.assertEqual(self.student.full_name, 'Mack Deo')

    def test_email(self):

        print('test_emai')
        self.assertEqual(self.student.email, 'mack.deo@email.com')

    def test_alert_santa(self):

        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        # new_end_date = old_end_date+timedelta(days=365)
        
        self.assertEqual(self.student.end_date, old_end_date+timedelta(days=5))

    def test_course_schedule_success(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, 'Success')

    def test_course_schedule_fail(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = False
            # mocked_get.return_value.text = "Somethng.."
           
            schedule = self.student.course_schedule()
            self.assertEqual(schedule, 'Something wrong..')


if __name__ == '__main__':
    unittest.main()
