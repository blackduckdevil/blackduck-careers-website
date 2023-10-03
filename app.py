from flask import Flask, render_template, json, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_blackduck():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Blackduck')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return json.dumps(jobs, default=dict)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "NOT FOUND", 404
  
  return render_template('jobpage.html', 
                          job=job[0])

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)

  return render_template('application_submitted.html',
                          application=data,
                          job=job[0])

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
