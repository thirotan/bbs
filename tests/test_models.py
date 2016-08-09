"""test_models.py"""

import pytest

from bbs.models import Bbs


class TestModels:
    @pytest.mark.parametrize(('field_name'), {
        'id', 'name', 'content' 
    })
    def test_mode_has_proper_field(self, field_name):
        bbs = Bbs()
        assert hasattr(bbs, field_name)
