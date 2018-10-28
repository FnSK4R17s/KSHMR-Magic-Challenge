from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation
path = 'C:/Users/Shikhar Shukla/Desktop/GAN_Collection/KSHMR Magic Challenge/Datasets'
cdriver = 'C:/Users/Shikhar Shukla/Downloads/chromedriver_win32/chromedriver.exe'
arguments = {"keywords":"madhubani paintings hd, chikankari designs hd","limit":2000,"print_urls":True,"size":">640*480","output_directory":path,"chromedriver":cdriver}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
