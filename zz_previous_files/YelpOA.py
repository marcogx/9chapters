def dot_product(v1, v2):
	map, ans = {}, 0
	for x, y in v1:
		map[x] = y
	for x, y in v2:
		ans += map.get(x, 0) * y

	return ans

(k, n) = [int(_) for _ in raw_input().split()]
v1, v2 = [], []

for _ in xrange(k):
	(x, y) = (int(_) for _ in raw_input().split())
	v1.append((x, y))

for _ in xrange(n):
	(x, y) = (int(_) for _ in raw_input().split())
	v2.append((x, y))

print dot_product(v1, v2)





def is_anagram(s, t):
	map = {}
	for c in s:
		map[c] = map.get(c, 0) + 1
	for c in t:
		map[c] = map.get(c, 0) - 1
	for c in map:
		if map[c] != 0:
			return False

	return True

# given N
N = input()
for _ in xrange(N):
	s, t = raw_input().split()
	print is_anagram(s, t)




def check_palin(s):
	map, odd = {}, 0
	for c in s:
		map[c] = map.get(c, 0) + 1
	for c in map:
		if map[c] % 2 == 1:
			odd += 1
		if odd > 1:
			return False
	return True


def reverse_words(s):
	return ' '.join(reversed(s.split()))

while True:
	try:
		s = raw_input()
		# print check_palin(s)
		print reverse_words(s)
	except EOFError:
		break

# import sys
# for line in sys.stdin:
# 	s, t = line.split()
# 	print is_anagram(s, t)

# import sys
# pairs = []
# for line in sys.stdin:
# 	(k, v) = (int(x) for x in raw_input().split())
# 	pairs.append((v, k))
#
# pairs.sort()
# for (v, k) in pairs:
# 	print k, v




def get_key(item):
	return -item[1]

pairs = []
while True:
	try:
		(k, v) = [int(x) for x in raw_input().split()]
		# x, y = raw_input().split()
		pairs.append((k, v))
	except EOFError:
		break
pairs.sort(key=get_key)
for k, v in pairs:
	print k, v




def reverseWords(s):
	if not s:
		return ""
	words = word_split(s)
	return ' '.join(reversed(words))


def word_split(s):
	start, end, n, words = 0, 0, len(s), []
	while start < n:
		if s[start] == ' ':
			start += 1
		else:
			end = start
			while end < n and s[end] != ' ':
				end += 1
			words.append(s[start:end])
			start = end
	return words



n = int(raw_input())
for i in range(0,n):
    a, b = raw_input().split()
    print int(a) + int(b)