import flask

bp = flask.Blueprint('clients', __name__, url_prefix='/clients')

@bp.route('/', methods=['GET'])
def root():
    return flask.jsonify('ahoyhoy')