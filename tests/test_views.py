"""test_views.py."""

from flask import url_for


class TestViews:
    def test_index_page(self, client):
        res = client.get(url_for('app.index'))
        assert res.status_code == 200
        assert b'Test' in res.data
