from flask import current_app as app, g
from sqlalchemy import select

from .db import connect_db
from .models import Resource


@app.route('/api/requests', methods=['GET'])
def get_resource_requests():
    connect_db()
    requested = g.db.execute(select(Resource)).scalars().all()
    g.db.close()

    if not requested:
        return "there are no requests at this time."
        
    requests = list()
    for row in requested:
        del row.__dict__['_sa_instance_state']
        requests.append(row.__dict__)

    return requests


@app.route('/api/requests/<int:id>', methods=['GET'])
def get_individual_request(id:int):
    connect_db()
    requested = g.db.get(Resource, id)
    g.db.close()

    if requested is None:
        return "that resource request is not available at this time."
    
    del requested.__dict__['_sa_instance_state']

    return [requested.__dict__]