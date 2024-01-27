from eval import eval
from generate import gen0, new_gen
import os
from read_image import readImage

def main():
	img = readImage()
	gen0()
	i = 0
	# 1000世代分の評価を行う
	while i <= 1000:
		eval(img, i)
		new_gen(i)
		# 50世代ごとに遺伝情報を記録
		if (i % 50 != 0):
			os.remove('select{}.txt'.format(i))
		i += 1

if __name__ == '__main__':
	main()