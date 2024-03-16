from flask_restful import reqparse


def parse():
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('email', required=True)
    parser.add_argument('password', required=True)
    return parser.parse_args()
