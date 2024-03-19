from flask import *
from flask_restful import *

import api_argparser
from data import db_session
from data.jobs import Job


def abort_if_jobs_not_found(job_id):
    session = db_session.create_session()
    jobs = session.query(Job).get(job_id)
    if not jobs:
        abort(404, message=f"job {job_id} not found")


class JobResource(Resource):
    def get(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Job).filter(Job.id == job_id)[0]
        return jsonify({'job': job.to_dict()})

    def delete(self, job_id):
        abort_if_jobs_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Job).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Job).all()
        return jsonify({'jobs': [item.to_dict(
            only=('id',
                  'team_leader',
                  'job',
                  'work_size',
                  'collaborators',
                  'start_date',
                  'end_date',
                  'is_finished')) for item in jobs]})

    def post(self):
        args = api_argparser.job_parse()
        session = db_session.create_session()
        job = Job()
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.start_date = args['start_date']
        job.end_date = args['end_date']
        job.is_finished = args['is_finished']
        session.add(job)
        session.commit()
        return jsonify({'id': job.id})
