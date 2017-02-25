# -*- coding: utf-8 -*-

from flask import url_for


class TestViews:
    def test_index_page(self, client, fx_postmessage):
        res = client.get(url_for('app.index'))
        assert res.status_code == 200
        assert b'Sample BBS' in res.data

    def test_post_message(self, client, fx_postmessage):
        res = client.post(
            url_for('app.post_message'),
            data=dict(name='test user', content="test content"))

        assert res.status_code == 302
