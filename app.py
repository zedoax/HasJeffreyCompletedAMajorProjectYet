from flask import Flask
from flask import render_template
from sqlalchemy import create_engine
from config import DATABASE_URI

app = Flask(__name__)
engine = create_engine(DATABASE_URI)


@app.route('/')
def get_index():
    project = False
    connection = engine.connect()
    result = connection.execute("SELECT project FROM jeffrey")
    for row in result:
        if row['project']:
            project = True
    return render_template('index.html', project=project)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
