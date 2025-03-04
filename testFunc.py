from ikpy.chain import Chain
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

# getting robot joint infos from urdf file
my_chain = Chain.from_urdf_file("./test.urdf")

#print(my_chain.forward_kinematics([0] * 10))


checkpoints = [
	[0.2, -0.4, 0.6],
	[0.2, -0.4, 0.6],
	[-0.2, -0.4, 0.3],
	[-0.2, -0.4, 0.3],
]

for i in checkpoints:
	iv = my_chain.inverse_kinematics(i,[2.2, 2.2, 0])
	print("pour aller aux coordonnées: ", i)
	print(iv)

	# plotting the robot
	ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')
	my_chain.plot(iv, ax)
	matplotlib.pyplot.show()