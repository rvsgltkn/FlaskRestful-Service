from flask_restx import Namespace, fields

class TaskDto():

    api = Namespace('Tasks', description='Task api information')

    model_content=api.model('content',{
        'text':fields.String(required=True, description='text value'),
        'created_on':fields.Date(description='YYYY-MM-DD'),
        'updated_on':fields.Date(description='YYYY-MM-DD'),
    })

    model_nest=fields.Nested(model_content)

    model_wild = fields.Wildcard(model_nest)

    task = api.model('task',{
       '*':model_wild
    })




