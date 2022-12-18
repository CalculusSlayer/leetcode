# Instructure Technical Interview

def recurse(deep_dict, sol=[]):
	for key in deep_dict:
		x = deep_dict[key]
		if not isinstance(x, dict):
			sol.append(x)
		else:
			recurse(x, sol)
	return sol

def iterative(deep_dict, sol=[]):
	stack = []
	stack.append(deep_dict)
	while len(stack) > 0:
		cur = stack.pop(-1)
		for key in cur:
			x = cur[key]
			if not isinstance(x, dict):
				sol.append(x)
			else:
				stack.append(x)
	return sol

def main():
	'''
	sol = [1, 2, 4, 6, 7, 8, 9, 10, 5, 3] 

	cur = {'e' : 3}

	stack = [ 
			]
	'''
	deep = {'a' : 1,
			'b' : 2,
			'c' : {'d' : {'e' : 3}
				},
			'f' : 4,
			'g' : {'h' : {'i' : 5}, 'j' : 6, 'k' : 7,
				'l' : {'m' : 8, 'n' : 9, 'o' : {'p' : 10}}},
			}

	print(recurse(deep)) # [1, 2, 3, 4]
	print(iterative(deep)) # [1, 2, 4, 3]
	# print([1, 2, 4, 6, 7, 8, 9, 10, 5, 3])

	x = deep['a']
	print(x)
	deep['a'] = 69
	print(x)
	print(deep['a'])


if __name__ == '__main__':
	main()
