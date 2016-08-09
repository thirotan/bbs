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

