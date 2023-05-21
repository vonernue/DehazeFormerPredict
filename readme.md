# DehazeFormer Predict
This is a DehazeFormer implementation copied from the original [HuggingFace](https://huggingface.co/spaces/IDKiro/DehazeFormer_Demo).
This repository includes the pretrained model of the DehazeFormer used on the HuggingFace demo.
The code can be run without anaconda environment.

## Prerequisites
Python version needs to be higher than `3.8`.
Install the dependencies by running:
```shell
pip install -r requirements.txt
```

Make sure to have Git LFS installed to pull the pretrained model.
[Git LFS](https://git-lfs.com/)
Pull the pretrained model by running:
```shell
git lfs pull
```

## Usage
```
usage: predict.py [-h] -i INPUT -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input image path
  -o OUTPUT, --output OUTPUT
                        output image path
```

### Example
```shell
python predict.py -i <input image> -o <output image>
```

## Credit
* [Vision Transformers for Single Image Dehazing](https://arxiv.org/abs/2204.03883)
* [DehazeFormer](https://github.com/IDKiro/DehazeFormer)
* [DehazeFormer HuggingFace Demo](https://huggingface.co/spaces/IDKiro/DehazeFormer_Demo)