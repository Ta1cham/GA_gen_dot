from collections import deque
import numpy as np
import os
import cv2

#　ユークリッド距離を計算する関数
def euclid(rgb, img, width, height):
	dist = 0
	for i in range(height):
		for j in range(width):
			tmp = 0
			for k in range(3):
				tmp += (rgb[i, j, k] - img[i, j, k])**2
			dist += tmp ** 0.5
	return dist

# トーナメント方式で淘汰
def eval(img, gen, width=50, height=50, population=256):
	r = []
	g = []
	b = []
	q = deque()
	with open('gen{}.txt'.format(gen),'r') as file:
		head = file.read()
		data = head.replace('[','').replace(']','').split('\n')
		for i in range(population):
			r.append([ int(_) for _ in data[i*3].split(', ')])
			g.append([ int(_) for _ in data[i*3+1].split(', ')])
			b.append([ int(_) for _ in data[i*3+2].split(', ')])
			q.append(i)
	os.remove('gen{}.txt'.format(gen))

	while q.__len__() > 4:
		idx1 = q.popleft()
		idx2 = q.popleft()
		r_1 = r[idx1]
		g_1 = g[idx1]
		b_1 = b[idx1]
		r_2 = r[idx2]
		g_2 = g[idx2]
		b_2 = b[idx2]
		rgb1 = np.zeros((height, width, 3), np.uint8)
		rgb2 = np.zeros((height, width, 3), np.uint8)
		cnt = 0
		for i in range(height):
			for j in range(width):
				rgb1[i, j] = [r_1[cnt], g_1[cnt], b_1[cnt]]
				rgb2[i, j] = [r_2[cnt], g_2[cnt], b_2[cnt]]
				cnt += 1
		lab1 = cv2.cvtColor(rgb1, cv2.COLOR_RGB2LAB)
		lab2 = cv2.cvtColor(rgb2, cv2.COLOR_RGB2LAB)
		if euclid(lab1, img, width, height) < euclid(lab2, img, width, height):
			q.append(idx1)
		else:
			q.append(idx2)
	print("selecting...", gen)
	with  open('select{}.txt'.format(gen), 'w') as file:
		while q.__len__() > 0:
			idx = q.popleft()
			file.write('{}\n{}\n{}\n'.format(r[idx], g[idx], b[idx]))
	show_result(gen)

# 結果の表示
def show_result(gen, width=50, height=50, population=256):
	r = np.zeros((population, height*width), np.uint8)
	g = np.zeros((population, height*width), np.uint8)
	b = np.zeros((population, height*width), np.uint8)
	with open('select{}.txt'.format(gen), 'r') as file:
		head = file.read()
		data = head.replace('[','').replace(']','').split('\n')
		for i in range(4):
			r[i] = [ int(_) for _ in data[i*3].split(', ')]
			g[i] = [ int(_) for _ in data[i*3+1].split(', ')]
			b[i] = [ int(_) for _ in data[i*3+2].split(', ')]
	
	for i in range(4):
		tmp = np.zeros((height, width, 3), np.uint8)
		cnt = 0
		for j in range(height):
			for k in range(width):
				tmp[j, k] = [r[i][cnt], g[i][cnt], b[i][cnt]]
				cnt += 1
		tmp = cv2.resize(tmp, (400, 400))
		str = 'gen{}'.format(gen)
		cv2.imshow(str, tmp)
		cv2.waitKey(100)
		cv2.destroyAllWindows()