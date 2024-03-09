import flask

from data import db_session
from data.jobs import Job

blueprint = flask.Blueprint(
    'mars_api',
    __name__
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    return flask.jsonify(
        {
            'news':
                [item.to_dict()
                 for item in jobs]
        }
    )
