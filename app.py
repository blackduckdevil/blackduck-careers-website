from flask import Flask, render_template, json
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_blackduck():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Blackduck')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return json.dumps(jobs, default=dict)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
