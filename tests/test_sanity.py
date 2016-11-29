from unittest import TestCase

from mmeter.mmeter import App


class TestAppInstance(TestCase):

	def setUp(self):
		self.app = App()

	def tearDown(self):
		self.app.destroy()

	def test_instance(self):
		self.assertIsInstance(self.app, App)


if __name__ == '__main__':
	unittest.main()
