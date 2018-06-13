import sys
from PIL import Image

IMAGE_SIZE = (8, 8)
NUM_PIXELS = IMAGE_SIZE[0] * IMAGE_SIZE[1]

def loadImage(image_path):
	try:
		print "Attempting to load image " + image_path
		image = Image.open(image_path)
		width, height = image.size
		print "image size: " + str(width) + " " + str(height)
		return image
	except IOError:
		print "Failed to load image " + image_path
		sys.exit()

def compute_average_hash(avg, pixels):
	hashed_image_bit_string = ""
	for pixel in pixels:
		if (pixel > avg):
			hashed_image_bit_string += "1"
		else:
			hashed_image_bit_string += "0"
	print "hashed bit string: " + hashed_image_bit_string
	#hashed_int = int(hashed_image_bit_string, 2)
	#print "hashed int value: " + str(hashed_int)
	return hashed_image_bit_string

def ahash(image_path):
	image = loadImage(image_path)

	# set image to 8x8
	image = image.resize(IMAGE_SIZE)

	# set image to greyscale
	image = image.convert("L")

	pixels = list(image.getdata())
	print pixels
	color_avg = sum(pixels) / float(NUM_PIXELS)

	hash_value = compute_average_hash(color_avg, pixels)

	print "hash value for " + sys.argv[1] + " is " + str(hash_value)

	return hash_value


hash_string1 = ahash(sys.argv[1])
hash_string2 = ahash(sys.argv[2])

hamming_dist = 0

for i in range(NUM_PIXELS):
	if (hash_string1[i] != hash_string2[i]):
		hamming_dist += 1

print hamming_dist
