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

def solution(part_time_jobs, sales_jobs):
	answer = 0
	for p in part_time_jobs:
		part_time_job = PartTimeJob(p[0], p[1])
		answer += part_time_job.get_salary()
	for s in sales_jobs:
		sale_job = SalesJob(s[0], s[1])
		answer += sale_job.get_salary()
	return answer