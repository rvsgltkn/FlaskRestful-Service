import unittest
import json
from flask_api import status
from app.test.base import BaseTestCase


class TestTaskList(BaseTestCase):

    def test_get_all_tasks(self):
        response=self.client.get(self.BASE_URL+'/Tasks/')
        self.assertTrue(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_add_new_task(self):
        payload={'text':'test data'}
        response = self.client.post(self.BASE_URL + '/Tasks/', json=payload)

        data=json.loads(response.data.decode())

        self.assertTrue(response)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertTrue(data.get('task_id'))


    def test_add_new_task_without_payload(self):
        payload = None
        response = self.client.post(self.BASE_URL + '/Tasks/', json=payload)

        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


    def test_add_new_task_without_text(self):
        payload = {}
        response = self.client.post(self.BASE_URL + '/Tasks/', json=payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_new_task_with_blank_text(self):
        payload = {'text': ''}
        response = self.client.post(self.BASE_URL + '/Tasks/', json=payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class TestTask(BaseTestCase):

    def test_get_individual_task(self):
        response=self.client.get(self.BASE_URL+'/Tasks/'+self.TASK_ID)
        self.assertTrue(response)
        self.assertEqual(response.status_code,status.HTTP_200_OK)



    def test_get_individual_task_with_wrong_task_id(self):
        response=self.client.get(self.BASE_URL+'/Tasks/123456789')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)



    def test_edit_individual_task(self):
        payload = {'text': 'test data'}
        response=self.client.put(self.BASE_URL+'/Tasks/'+self.TASK_ID,json=payload)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


    def test_edit_individual_task_with_wrong_task_id(self):
        payload = {'text': 'test data'}
        response=self.client.put(self.BASE_URL+'/Tasks/123456789',json=payload)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_edit_individual_task_without_payload(self):
        payload = None
        response=self.client.put(self.BASE_URL+'/Tasks/'+self.TASK_ID,json=payload)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_edit_individual_task_without_text(self):
        payload = {}
        response=self.client.put(self.BASE_URL+'/Tasks/'+self.TASK_ID,json=payload)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


    def test_edit_individual_task_with_blank_text(self):
        payload = {'text': ''}
        response=self.client.put(self.BASE_URL+'/Tasks/'+self.TASK_ID,json=payload)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


if __name__ == '__main__':
    unittest.main()