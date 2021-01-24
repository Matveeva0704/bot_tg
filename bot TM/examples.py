class A:
	def _private(self):
		print('Это приватный метод!')

a = A()
a._private()
