from flask import request
from flask_restx import Resource
from ..util.dto import TaskDto
import uuid
from datetime import datetime

api = TaskDto.api
_task = TaskDto.task
_task_content=TaskDto.model_content

TASK_REQUEST={}

@api.route('/')
class TaskList(Resource):

    @api.doc('list of all tasks')
    @api.marshal_list_with(_task)
    def get(self):
        """list of all tasks"""
        return TASK_REQUEST



    @api.response(201,'Task created successfully')
    @api.doc('create a new task')
    @api.expect(_task_content, validate=True)
    def post(self):
        """create a new task"""
        data = request.json

        if not data.get('text'):
            api.abort(400)

        task_id=str(uuid.uuid4())
        new_task={
            'text':data.get('text'),
            'created_on':datetime.utcnow()
        }

        TASK_REQUEST[task_id]=new_task
        response_obj={'task_id':task_id}

        return response_obj,201


@api.route('/<task_id>')
@api.param('task_id','Task identifier')
@api.response(404,'Task not found')
class Task(Resource):


    @api.doc('Get a Task')
    @api.marshal_with(_task_content)
    def get(self,task_id):
        """ get a task given its identifier"""

        if task_id not in TASK_REQUEST:
            api.abort(404)

        return TASK_REQUEST[task_id]


    @api.response(204, 'Task updated successfully')
    @api.doc('Update a Task')
    @api.expect(_task_content, validate=True)
    def put(self,task_id):
        """ get a task given its identifier"""

        data = request.json

        if not data.get('text'):
            api.abort(400)

        if task_id not in TASK_REQUEST:
            api.abort(404)


        TASK_REQUEST[task_id]['text'] = data.get('text')
        TASK_REQUEST[task_id]['updated_on'] = datetime.utcnow()

        response_obj = {'status': 'task updated successfuly'}
        return response_obj,204
