"""test/conftest.py."""
# -*- config: utf-8 -*-

import pytest
import time

from bbs import create_app

@pytest.fixture
def app(request):
    """app fixture."""
    app = create_app(environment='Testing')
    cnt = app.app_context()
    cnt.push() 

    def teardown():
        cnt.pop()

    request.addfinalizer(teardown)

    return app

@pytest.fixture
def db(app, request):
    _db.app = app
    _db.create_all()

    def teardown():
        _db.drop_all()

    request.addfinalizer(teardown)

    return _db


@pytest.fixture(scope='function')
def db_session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()
    options = {'bind': connection, 'binds': {}}
    session = db.create_scoped_session(options=options)
    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)

    return session

