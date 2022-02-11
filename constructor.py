class car:
	def __init__(self):
		self.x=10;
		print("car object")
class BMW(car):
	def __init__(self):
		self.x=20;
		print("BMW object")
class BMW_7_series(BMW):
	def __init__(self):
		self.x=40;
		print("BMW_7_series")
class  benz(car):
	def __init__(self):
		self.x=50;
		super().__init__();
class test(BMW_7_series):
	pass
t =test()
print(t.x)






