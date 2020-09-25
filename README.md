# Crawler image removed background with remove.bg 

## Required 
* Python 3.6 
* Ubuntu 16.04 
* Chrome Version 84.0.4147.105 (Official Build) (64-bit)
## Install 

```python
pip install -r requirements.txt 
```

## Crawler with local image (NO Parallel Support)
* Step 1: Change the `MODE='local' in `constance.py`
* Step 2: Run this command 

```python 
python crawler.py --href=ABSOLUTE_PATH_TO_IMAGE
```

## Crawler with online urls of images (ALLOW Parallel Support)
* Step 1: Open the `list_urls.txt` 
* Step 2: Write urls need to remove background in this file. Each line have one url. Number of urls for each runners depend of your hardware resource. I use 8 urls in each run.
* Step 3: Run this command
```python
python runners.py
``` 

## Result 
* Image upload 

![](./images/cf6ada6aa3294a771338.jpg)

* Image Removed Background 

![](./downloads/cf6ada6aa3294a771338-removebg-preview.png)