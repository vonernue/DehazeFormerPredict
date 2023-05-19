import torch
import torchvision.transforms.functional as TF
from pytorch_msssim import ssim
import cv2
import argparse
from models import *
from PIL import Image
import numpy as np

def infer(raw_image):
	network = DehazeFormer()
	pth = torch.load(f'./trainedModels/dehazeformer-mct.pth', map_location=torch.device('mps'))['state_dict']
	network.load_state_dict(pth)

	network.eval()
	
	image = np.array(raw_image, np.float32) / 255. * 2 - 1
	image = torch.from_numpy(image)
	image = image.permute((2, 0, 1)).unsqueeze(0)

	with torch.no_grad():
		output = network(image).clamp_(-1, 1)[0] * 0.5 + 0.5	
		output = output.permute((1, 2, 0))
		output = np.array(output, np.float32)
		output = np.round(output * 255.0)

	# output = Image.fromarray(output.astype(np.uint8))

	return output

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', type=str, help='input image path')
	parser.add_argument('-o', '--output', type=str, help='output image path')
	args = parser.parse_args()
	img = Image.open(args.input)
	output = infer(img)
	cv2.imwrite(args.output, output)