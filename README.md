# Wrench socket detection app

## Requirements

- python 3.11.6
- nvidia card


## Instalation

1. Install pytorch lib with cuda libs
run in console

```powershell

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install ultralytics

```
2. Install drivers for cuda 

2.1 In this scenario was used cuda 11.8, grab it from this link : https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11

2.2 Next install cudnn drivers for 11.x cuda from this link https://developer.nvidia.com/rdp/cudnn-archive (use the most actual available)

2.3 Restart PC after install

3. Check if cuda is available

```python
import torch
print(torch.cuda.is_available())
```

If it returns true, that signals that cuda is available for work, else you need to fix it

## Data preparation

Each object what we want to detect will be defined with a name and for each it is necessary to collect about (150-500 or even more photos) + 10% of it test samples. The next step is to label the object in our collected pictures, because somehow the model needs to know where in the picture it needs to look for the expected elements. There are many tools to do this task, you can use the attached program in the repo `labelImg.exe` (it works on windows). 

For each photo in collection mark using on the left panel function `Create RectBox` the object that you want to teach to the model, when you selected all models on the photo remember to select above save format as `YOLO` (not `PascalVOC`!) and save click save. It will automaticly create a .txt file, that representes the position of our object in the photo.
