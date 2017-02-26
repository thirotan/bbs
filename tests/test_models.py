"""test_models.py"""
# -*- coding: utf-8 -*-

import pytest

from bbs.models import Thread, Title, Message


class TestModels:
    @pytest.mark.parametrize(('thread_field_name'), {
        'id', 'thread_name' 
    })
    def test_mode_has_proper_thread_field(self, thread_field_name):
        thread = Thread()
        assert hasattr(thread, thread_field_name)

    @pytest.mark.parametrize(('title_field_name'), {
        'id', 'title', 'created_at', 'thread_id'
    })
    def test_mode_has_proper_title_field(self, title_field_name):
        title = Title()
        assert hasattr(title, title_field_name)

    @pytest.mark.parametrize(('message_field_name'), {
        'id', 'name', 'message', 'ip_addr', 'created_at', 'board_id' 
    })
    def test_mode_has_proper_message_field(self, message_field_name):
        message = Message()
        assert hasattr(message, message_field_name)
