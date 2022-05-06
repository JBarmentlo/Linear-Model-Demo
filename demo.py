import 	pandas as pd
import 	numpy as np
import 	matplotlib
from 	matplotlib import pyplot as plt
import 	random
import	cv2

x = np.arange(7, 40)
y = x * 2000 + 20000
for i in range(len(y)):
	# y[i] += random.uniform(-17000, 17000)
	y[i] *= random.uniform(0.8, 1.2)
df = pd.DataFrame()
df["surface"] = x
df["price"] = y

# df = pd.read_csv("./smol_data.csv")

def error(a, b, data: pd.DataFrame):
	pred = data.surface.apply(lambda x: a * x + b)
	error = (data.price - pred).to_numpy()
	return np.square(error).mean() / 100000


def make_fig(a, b, data: pd.DataFrame):
	x = data.surface.to_numpy()
	y = data.price.to_numpy()
	ax = plt.figure()
	plt.scatter(x,y)
	plt.ylim(ymin=0) 
	plt.xlim(xmin=0) 
	plt.plot([0, 40], [b, a * 40 + b])
	plt.savefig("fig.jpg", dpi = 250)
	plt.close()


def controller(lol=0):
	a 	= cv2.getTrackbarPos('a', 'Linear Model')
	b 	= cv2.getTrackbarPos('b', 'Linear Model')

	make_fig(a, b, df)
	im 	= cv2.imread("fig.jpg")
	errore = error(a, b, df)
	cv2.putText(img=im, text=f"Error: {errore:.0f}", org=(250, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 255),thickness=3)
	cv2.imshow('Linear Model' ,im)


if __name__ == "__main__":
	# df = pd.read_csv("./data.csv")
	cv2.imread("fig.jpg")

	cv2.namedWindow('Linear Model')
 
	
	# cv2.imshow('GEEK')
 
	cv2.createTrackbar('a'		, 'Linear Model', 255	, 10000	, controller)
	cv2.createTrackbar('b'		, 'Linear Model', 127	, 10000	, controller) 

cv2.waitKey(0)
