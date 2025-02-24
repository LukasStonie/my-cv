from flask import render_template
from app.routes.home import bp
import markdown

from app.utils import read_files as rf

@bp.route('/')
def index():
    """
    Renders the landing page.
    :return: rendered template of the landing page
    """

    education_text = rf.read_files('/Users/lukas/Projects/my-cv/data/education')
    education = []
    for e in education_text.values():
        entry = dict()
        entry['content'] = markdown.markdown(e)
        education.append(entry)

    working_text = rf.read_files('/Users/lukas/Projects/my-cv/data/working')
    working = []
    for e in working_text.values():
        entry = dict()
        entry['content'] = markdown.markdown(e)
        working.append(entry)

    return render_template('index.html', education=education, working=working)