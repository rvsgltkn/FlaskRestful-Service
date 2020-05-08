from flask_testing import TestCase
import json
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        self.BASE_URL='http://127.0.0.1:5000'

        """adding new record"""
        payload = {'text': 'test data'}
        response = self.client.post(self.BASE_URL + '/tasks/', json=payload)
        data = json.loads(response.data.decode())
        self.TASK_ID=data.get('task_id')


    def tearDown(self):
        pass