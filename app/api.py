from flask import current_app as app, g, request
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


@app.route('/api/requests', methods=['POST'])
def add_resource_request():
    new_request = Resource(
        item=request.json.get("item", None), 
        quantity=request.json.get("quantity", None), 
        description=request.json.get("description", None)
    )

    invalid_request = new_request.validate_input()
    if invalid_request:
        return invalid_request

    connect_db()

    invalid_request = g.db.execute(select(Resource).where(Resource.item == new_request.item)).first()
    if invalid_request:
        g.db.close()
        return "that resource request already exists."
    
    g.db.add(new_request)
    g.db.commit()
    g.db.close()
    
    return "resource request added successfully."