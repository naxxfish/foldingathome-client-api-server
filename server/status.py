import flask

bp = flask.Blueprint('status', __name__, url_prefix='/status')

@bp.route('/', methods=['GET'])
def status():
    status_dict = { "status": "ok", "message": "everything is A-OK" }
    return flask.jsonify(status_dict)