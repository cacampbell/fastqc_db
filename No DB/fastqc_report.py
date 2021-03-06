#!/usr/bin/env python3
from sys import argv
from io import StringIO
from flask import send_file
from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from FastqcDatabase import FastqcDatabase

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template('main.html', title='Fastqc DB')


@app.route("/all_results")
def all():
    all_results = app.records.get_all()
    return render_template('display.html',
                           title="All Results",
                           records=all_results)


@app.route("/pass_results")
def passed():
    pass_records = app.records.get('pass')
    return render_template('display.html',
                           title="Passed Results",
                           records=pass_records)


@app.route("/warn_results")
def warned():
    warn_records = app.records.get('warn')
    return render_template('display.html',
                           title="Warning Results",
                           records=warn_records)


@app.route("/fail_results")
def failed():
    failed_records = app.records.get('fail')
    return render_template('display.html',
                           title="Failed Results",
                           records=failed_records)


@app.route("/passed_modules")
def modulepassed():
    only_passed = app.records.get_only(result='pass')
    return render_template('display.html',
                           title="Only Passing Modules",
                           records=only_passed)


@app.route("/warned_modules")
def modulewarned():
    only_warned = app.records.get_only(result='warn')
    return render_template('display.html',
                           title="Only Warning Modules",
                           records=only_warned)


@app.route("/failed_modules")
def modulefailed():
    only_failed = app.records.get_only(result='fail')
    return render_template('display.html',
                           title="Only Failing Modules",
                           records=only_failed)


if __name__ == "__main__":
    app.records = FastqcDatabase(argv[1])
    app.records.load_from_dir(argv[1])
    app.run('0.0.0.0', debug=True)
