'''
저어는 이걸 겁나 느리게 풀기로 했어요
'''

movies = []
movie = 666
while len(movies)<10000:
    if '666' in str(movie):
        movies.append(movie)    
    movie = movie + 1

print(movies[int(input())-1])