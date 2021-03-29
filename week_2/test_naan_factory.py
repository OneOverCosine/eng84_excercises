from naan_factory import NaanFactory
import unittest

class NannTest(unittest.TestCase):
    naan = NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.naan.make_dough("water", "flour"), "dough")
        self.assertNotEqual(self.naan.make_dough("milk", "flowers"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.naan.bake_dough("dough"), "naan")
        self.assertNotEqual(self.naan.bake_dough("chocolate"), "naan")

    def test_run_factory(self):
        self.assertEqual(self.naan.run_factory("water", "flour"), "naan")
        self.assertNotEqual(self.naan.make_dough("eggs", "vanilla"), "naan")