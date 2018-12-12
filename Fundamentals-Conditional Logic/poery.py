

logic = """
一，创建makePoem()函数，返回多行字符串，就是一首完整的诗，只要print makePoem()调用这个函数就可以展示这首诗
二，创建多个列表，包含nouns,adjectives,adverbs,verbs,preposions,每个列表都有相关的单词
三，用random.choice()函数，从适当的列表中选出随机单词，每个选择存储在新的字符串中。选择三个名词，三个动词，三个形容词，一个副词，两个介词，
确保没有重复的单词（提示，用while循环重复选择过程，直到获取新的单词为止）
四，使用format()	方法将选择的单词插入上面的结构中，以创建一个诗歌字符串
五、如果第一个形容词以元音开头，标题和第一行中的A自动调整为An

"""
from random import choice

noun = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
preposions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]


def makePoem():	
#三个不同的名词
	n1 = choice(noun)
	n2 = choice(noun)
	n3 = choice(noun)
	while n1 == n2:
		n2 = choice(noun)
	while n1 == n3 or n2 == n3:
		n3 = choice(noun)
	
#三个不同的动词	
	v1 = choice(verbs)
	v2 = choice(verbs)
	v3 = choice(verbs)
	while v1 == v2:
		v2 = choice(verbs)
	while v1 == v3 or v2 == v3:
		v3 = choice(verbs)

#三个不同的形容词
	adj1 = choice(adjectives)
	adj2 = choice(adjectives)
	adj3 = choice(adjectives)
	while adj1 == adj2:
		adj2 = choice(adjectives)
	while adj1 == adj3 or adj2 == adj3:
		adj3 = choice(adjectives)
	

#两个介词
	prep1 = choice(preposions)
	prep2 = choice(preposions)
	while prep1 == prep2:
		prep2 = choice(preposions)

#一个副词
	adv1 = choice(adverbs)

#形容词首字母为元音
	if 'aeiou'.find(adj1[0]) != -1:
		artical = 'An'
	else:
		artical = 'A'
#整首诗
	poem = '{} {} {}\n'.format(artical, adj1, n1)
	poem = poem + '{} {} {} {} {} the {} {}\n{}, the {} {}\n'.format(artical, adj1, n1, v1, prep1, adj2, n2, adv1, n1, v2)
	poem = poem + 'the {} {} {} a {} {}'.format(n2, v3, prep2, adj3, n3)
	return poem


print(makePoem())

