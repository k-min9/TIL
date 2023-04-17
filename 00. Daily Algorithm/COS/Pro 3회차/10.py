'''
최초로 Class 내의 변수 쓴거 같은데...?
'''
class HairShop(Shop):
	def __init__(self):
		super().__init__()

	def reserve(self, customer):
		if customer.num_of_people != 1:
			return False
		for r in self.reserve_list:
			if r.time == customer.time:
				return False
		self.reserve_list.append(customer)
		return True

class Restaurant(Shop):
	def __init__(self):
		super().__init__()
		
	def reserve(self, customer):
		if 2 <= customer.num_of_people <= 8:
			return False
		count = 0
		for r in self.reserve_list:
			if r.time == customer.time:
				count += 1
		if count >= 2:
			return False
		self.reserve_list.append(customer)
		return True

def solution(customers, shops):
	hairshop = HairShop()
	restaurant = Restaurant()

	count = 0
	for customer, shop in zip(customers, shops):
		if shop == "hairshop":
			if hairshop.reserve(Customer(customer[0], customer[1], customer[2])):
				count += 1
		elif shop == "restaurant":
			if restaurant.reserve(Customer(customer[0], customer[1], customer[2])):
				count += 1

	return count
