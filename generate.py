from random import randrange, randint, random
import os

# 初期世代の生成
def gen0(width=50, height=50, population=256):
	with open('gen0.txt','w') as file:
		
		for i in range(population):
			r, g, b = [], [], []
			for y in range(height):
				for x in range(width):
					r.append((randrange(0, 255, 20)))
					g.append((randrange(0, 255, 20)))
					b.append((randrange(0, 255, 20)))
				
			file.write('{}\n{}\n{}\n'.format(r,g,b))

# gen世代の生成
def new_gen(gen,  width=50, height=50, population=256):
	# selectファイルから親個体の情報を取得
	with open('select{}.txt'.format(gen), 'r') as parfile:
		lines = parfile.readlines()
		r_par = []
		g_par = []
		b_par = []
		for i in range(4):
			r_par.append([ int(_) for _ in lines[i*3].replace('[','').replace(']','').split(', ')])
			g_par.append([ int(_) for _ in lines[i*3+1].replace('[','').replace(']','').split(', ')])
			b_par.append([ int(_) for _ in lines[i*3+2].replace('[','').replace(']','').split(', ')])
	
	# 次世代の情報をgen+1ファイルに書き込み
	with open('gen{}.txt'.format(gen+1),'w') as file1:
		for i in range(population):
			r, g, b = [], [], []
			for y in range(height):
				for x in range(width):
					if random() < 0.005:
						# 1/200の確率で突然変異
						r.append((randrange(0, 255, 20)))
						g.append((randrange(0, 255, 20)))
						b.append((randrange(0, 255, 20)))
					else:
						par = randint(0, 3)
						r.append(r_par[par][height*y+x])
						g.append(g_par[par][height*y+x])
						b.append(b_par[par][height*y+x])
			file1.write('{}\n{}\n{}\n'.format(r,g,b))