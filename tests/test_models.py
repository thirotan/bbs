"""test_models.py"""
# -*- coding: utf-8 -*-

import pytest

from bbs.models import Thread, Category, Message


class TestThread:
    @pytest.mark.parametrize(('category_field_name'), {
        'id', 'category_name'
    })
    def test_mode_has_proper_category_field(self, category_field_name):
        category = Category()
        assert hasattr(category, category_field_name)

class TestTitle:
    @pytest.mark.parametrize(('thread_field_name'), {
        'id', 'thread_title', 'created_at', 'category_id'
    })
    def test_mode_has_proper_thread_field(self, thread_field_name):
        thread = Thread()
        assert hasattr(thread, thread_field_name)

class TestMessage:
    @pytest.mark.parametrize(('message_field_name'), {
        'id', 'username', 'message', 'ip_addr', 'user_agent', 'created_at', 'thread_id'
    })
    def test_mode_has_proper_message_field(self, message_field_name):
        message = Message()
        assert hasattr(message, message_field_name)
