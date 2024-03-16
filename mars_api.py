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
            'jobs':
                [item.to_dict() for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_job(job_id):
    db_sess = db_session.create_session()
    try:
        job = db_sess.query(Job).filter(Job.id == job_id)[0]
    except IndexError:
        return 'No such job 😢'
    return flask.jsonify(
        {
            'jobs':
                [job.to_dict()]
        }
    )


@blueprint.app_errorhandler(404)
def er404(info):
    print(info)
    return 'API EROR 404'
