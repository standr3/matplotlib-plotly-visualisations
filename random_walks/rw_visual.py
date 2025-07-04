import matplotlib.pyplot as plt
	
from random_walk import RandomWalk



while True:
	#Make a random walk
	rw = RandomWalk(50_000)
	rw.fill_walk()
	#Plot the points in the walk
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolors='none', s=1)
	
	# Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	ax.set_aspect('equal')
	plt.show()
  
	keep_running = input('Make another walk? (y/n): ')
	if keep_running == 'n':
		break
