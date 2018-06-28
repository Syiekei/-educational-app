# services/users/manage.py
import os
import unittest
from flask.cli import FlaskGroup
import coverage
from project import app, db
from project.models import User


cli = FlaskGroup(app)


@cli.command()
def recreate_db():
    """ Creates DB based on models"""
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """ Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def cov():
    """ Runs the unit test with coverage"""
    cov = coverage.coverage(
        branch=True, include='project/*',
        omit='*/models.py')
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print("Coverage Summary:")
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'coverage')
    cov.html_report(directory=covdir)
    cov.erase()


@cli.command()
def seed_db():
    """Seeds the database. Needs recreate_db to be run first"""
    db.session.add(User(username='michael', email="hermanmu@gmail.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()


if __name__ == '__main__':
    cli()
