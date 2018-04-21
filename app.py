from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from config import DATABASE_URI
import sqlalchemy.exc as exc
import logging

app = Flask(__name__)
engine = create_engine(DATABASE_URI)

try:
    conn = engine.connect()
    res = conn.execute("INSERT INTO jeffrey VALUES (True)")
except exc.SQLAlchemyError:
    log = logging.getLogger(__name__)
    log.log(level=__ge__, msg="Error adding major project")


@app.route('/')
def get_index():
    project = False
    connection = engine.connect()
    result = connection.execute("SELECT project FROM jeffrey")
    if result['project']:
        project = True
    return render_template('index.html', project=project)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
