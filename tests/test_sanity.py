from tkinter import Tk
from unittest import TestCase

from mmeter.mmeter import App


class TestAppInstance(TestCase):

	def setUp(self):
		self.root = Tk()
		self.app = App(self.root)

	def tearDown(self):
		self.app.destroy()

	def test_instance(self):
		self.assertIsInstance(self.app, App)


if __name__ == '__main__':
	unittest.main()
