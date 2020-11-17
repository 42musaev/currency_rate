import jinja2
import flask
import json

blueprint = flask.Blueprint('filters', __name__)


@jinja2.contextfilter
@blueprint.app_template_filter()
def str_to_dict(context, value):
    return json.loads(value)


blueprint.add_app_template_filter(str_to_dict)
