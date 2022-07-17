import wget

# Set up the image URL
image_url = "https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_detail/augmented-reality/aventador/svj/11_17/ar_aventador_svj.png"

# Use wget download method to download specified image url.
image_filename = wget.download(image_url)

print('Image Successfully Downloaded: ', image_filename)