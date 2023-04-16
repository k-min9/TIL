'''
클래스 상속 = 인수 조심
'''
class ComicBook(Book):
	def get_rental_price(self, day):
		cost = 500
		day -= 2
		if day > 0:
			cost += 200 * day
		return cost

class Novel(Book):
	def get_rental_price(self, day):
		cost = 1000
		day -= 3
		if day > 0:
			cost += 300 * day
		return cost

def solution(book_types, day):
	books = []
	for types in book_types:
		if types == "comic":
			books.append(ComicBook())
		elif types == "novel":
			books.append(Novel())
	total_price = 0
	for book in books:
		total_price += book.get_rental_price(day)
	return total_price
