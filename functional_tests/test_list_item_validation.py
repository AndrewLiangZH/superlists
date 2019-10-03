from .base import FunctionalTest

MAX_WAIT = 10


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.fail('write me!')
