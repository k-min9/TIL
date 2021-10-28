/*
	[배열 관련 주요 메서드 연습 1]
	주어진 배열의 요소 중 null 값을 제거한 새로운 배열을 만드세요.
*/

const homeworks = ['david.zip', null, 'maria.zip', 'tom.zip', null]

const results = []
for (const homework of homeworks) {
	if (homework) {
		results.push(homework)
	}
}
console.log(results)

/*
	[배열 관련 주요 메서드 연습 2]
	
	주어진 배열을 사용하여 아래 문자열을 완성하세요.
	'www.samsung.com/sec/buds/galaxy-buds-pro'
*/

const arr1 = ['www', 'samsung', 'com']
const arr2 = ['galaxy', 'buds', 'pro']
const arr3 = ['sec', 'buds']

const domain = arr1.join('.')
const product = arr2.join('-')

arr3.unshift(domain)  // 배열의 앞에 추가(appendleft)
arr3.push(product)  // 배열의 뒤에 추가(append)
arr3.join('/')
console.log(arr3)


/*
	[배열 관련 주요 메서드 연습 3]

	주어진 배열의 요소 중 모든 'rainy' 요소를 'sunny'로 교체하세요
	- indexOf 메서드를 사용합니다.
*/

const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']

for (let idx=0; idx<weather.length; idx++) {
	if (weather[idx] === 'rainy') {
		weather[idx] = 'sunny'  // 교체
	}
}

// rainy 가 하나라도 있다면(indexOf : 특정문자 위치 찾기 없으면 -1을 반환)
while (weather.indexOf('rainy') >= 0) {
	weather[weather.indexOf('rainy')] = 'sunny'
}
