import unittest


class TestSanity(unittest.TestCase):

	def setUp(self):
		self.one = 1

	def tearDown(self):
		pass

	def test_sanity(self):
		self.assertEqual(1, self.one)
		self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
	unittest.main()
