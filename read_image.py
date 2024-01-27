import numpy as np
import sys
import cv2

def readImage():
	if len(sys.argv) > 1:
		fname = sys.argv[1]
	else:
		fname = input('元となる画像ファイル名を入力してください ->')
	image = cv2.imread(fname)
	if image is None:
		print('イメージファイル', fname, 'が見つかりません')
		sys.exit(1)
	image = cv2.resize(image, (50, 50))
	return image

def main():
	img = readImage()
	cv2.imshow('image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()