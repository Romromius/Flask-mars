from flask_restful import reqparse


def user_parse():
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('email', required=True)
    parser.add_argument('password', required=True)
    return parser.parse_args()


def job_parse():
    parser = reqparse.RequestParser()
    parser.add_argument('team_leader', required=True)
    parser.add_argument('job', required=True)
    parser.add_argument('work_size', required=True)
    parser.add_argument('collaborators', required=False)
    parser.add_argument('start_date', required=False)
    parser.add_argument('end_date', required=False)
    parser.add_argument('is_finished', required=False)
    return parser.parse_args()
