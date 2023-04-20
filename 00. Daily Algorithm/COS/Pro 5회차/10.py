class Job:
	def __init__(self):
		self.salary = 0
	
	def get_salary(self):
		return salary

class PartTimeJob(Job):
	def __init__(self, work_hour, pay_per_hour):
		super().__init__()
		self.work_hour = work_hour
		self.pay_per_hour = pay_per_hour
	
	def get_salary(self):
		self.salary = self.work_hour * self.pay_per_hour
		if self.work_hour >= 40:
			self.salary += (self.pay_per_hour * 8)
		return self.salary

class SalesJob(Job):
	def __init__(self, sales_result, pay_per_sale):
		super().__init__()
		self.sales_result = sales_result
		self.pay_per_sale = pay_per_sale

	def get_salary(self):
		if self.sales_result > 20:
			self.salary = self.sales_result * self.pay_per_sale * 3
		elif self.sales_result > 10:
			self.salary = self.sales_result * self.pay_per_sale * 2
		else:
			self.salary = self.sales_result * self.pay_per_sale
		return self.salary
