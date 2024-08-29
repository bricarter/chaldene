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