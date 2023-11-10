# I really like foxes so I created this script to fetch fox images using an API

import os

for i in range(123):
	# a free api to get fox images
	os.system("wget https://randomfox.ca/images/"+ str(i) + ".jpg")