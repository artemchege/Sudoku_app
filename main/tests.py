# import datetime
from django.test import TestCase
# from django.utils import timezone
# from django.urls import reverse
from http import HTTPStatus
from .models import Matrix


class SudokuMainTests(TestCase):
    """
    Testing SudokuMain view both POST and GET.
    """
    def test_get(self):
        """
        Check if everything renders right, for example submit button.
        """
        response = self.client.get("/")

        # print(response.content)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, '<button type="submit" class="btn btn-light w-50">Send</button>', html=True)

    def test_correct_post(self):
        """
        Check what if someone submit valid matrix, we expect redirect on result page with id 1.
        """
        response = self.client.post("/", data={'1': ['1', '4', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['2', '5', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['3', '6', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/result/1')

    def test_incorrect_post_repeat_number_in_line(self):
        """
        Check if someone submit incorrect matrix: number is repeated at least twice in one line.
        """
        response = self.client.post("/", data={'1': ['1', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['1', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'do not violate sudoku rules')

    def test_incorrect_post_repeat_number_in_column(self):
        """
        Check if someone submit incorrect matrix: number is repeated at least twice in one column.
        """
        response = self.client.post("/", data={'1': ['1', '1', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'do not violate sudoku rules')

    def test_incorrect_post_repeat_number_in_box(self):
        """
        Check if someone submit incorrect matrix: number is repeated at least twice in one box.
        """
        response = self.client.post("/", data={'1': ['1', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '1', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'do not violate sudoku rules')

    def test_incorrect_post_not_int(self):
        """
        Check if someone submit incorrect matrix: number is not integer.
        """
        response = self.client.post("/", data={'1': ['lol', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid incoming data')

    def test_incorrect_post_int_gt_9(self):
        """
        Check if someone submit incorrect matrix: number is greater than 9.
        """
        response = self.client.post("/", data={'1': ['10', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid incoming data')

    def test_incorrect_post_int_lt_0(self):
        """
        Check if someone submit incorrect matrix: number is less than 0.
        """
        response = self.client.post("/", data={'1': ['-1', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid incoming data')

    def test_incorrect_post_float(self):
        """
        Check if someone submit incorrect matrix: number is float.
        """
        response = self.client.post("/", data={'1': ['1.5', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid incoming data')

    def test_incorrect_post_not_9x9(self):
        """
        Check if someone submit incorrect matrix: number is missing, matrix is not 9x9.
        """
        response = self.client.post("/", data={'1': ['', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'invalid incoming data')


class SudokuResultAndHistoryTests(TestCase):
    """
    Testing both History and Result page.
    """
    def test_history_without_submitted_matrix(self):
        """
        Check if everything renders right, for example submit button.
        """
        response = self.client.get("/history/")

        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'You do not have any submitted matrix')

    def test_result_page(self):
        """
        Testing result page, after submitting a valid matrix.
        """
        response = self.client.post("/", data={'1': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '2': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '3': ['3', '6', '0', '0', '0', '0', '0', '0', '0'],
                                               '4': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '5': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '6': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '7': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '8': ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                               '9': ['0', '0', '0', '0', '0', '0', '0', '0', '0']})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/result/1')

        url = response.url
        new_response = self.client.get(url)

        self.assertEqual(new_response.status_code, HTTPStatus.OK)
        self.assertContains(new_response, 'This is matrix that you submitted')
        self.assertContains(new_response, 'This is solved matrix')


