from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Hotel

import cv2
import numpy as np


# Create your views here.
@login_required
def home(request):
    return HttpResponse("Hello from blog app!")

@login_required
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            # return redirect('success')
            img_obj = form.instance  
            print(img_obj)
            return render(request, 'show_img.html', {'img_obj': img_obj}) 
    else:
        form = HotelForm()
    
    return render(request, 'upload.html', {'form': form})
 

def success(request):
    return HttpResponse('successfully uploaded')

@login_required
def transform_img(request):  
    if request.method == 'POST':
        temp = request.POST.get("Name")
        print(temp)

        if temp == 'rgbtogray':
            return render(request, 'r2g.html')
        elif temp == 'rgbtobin':
            return render(request, 'r2b.html')
        elif temp == 'rgbtored':
            return render(request, 'r2r.html')
        elif temp == 'rgbtolog':
            return render(request, 'r2L.html')
        elif temp == 'rgbtologi':
            return render(request, 'r2li.html')
        else:
            return HttpResponse("Page not found!")


        
            # return HttpResponse('successfully uploaded')
        
def rgb2gray(request):
    if request.method == 'POST':
        temp = request.POST.get("Name")
        print(temp)
        mydata = Hotel.objects.filter(name = temp)
        pth = str(mydata[0].hotel_Main_Img.url)
        pth = pth[1:]
        print(pth)


        gray_img = cv2.imread(pth,0)
        gray_img = cv2.resize(gray_img, (1280,720))
        cv2.imwrite("media/images/output.jpg", gray_img)
        cv2.imshow("Gray image", gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pth = 'media/images/output.jpg'
        temp_obj = Hotel()
        temp_obj.name = 'output'
        temp_obj.hotel_Main_Img = cv2.imread(pth)
            
        print(mydata[0], temp_obj)
        return render(request, 'show_img.html', {'img_obj': mydata[0]})
    
def rgb2bin(request):
    if request.method == 'POST':
        temp = request.POST.get("Name")
        print(temp)
        mydata = Hotel.objects.filter(name = temp)
        pth = str(mydata[0].hotel_Main_Img.url)
        pth = pth[1:]
        print(pth)


        img = cv2.imread(pth,0)
        # cv2.imshow("Color image", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        ret, bin_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("Binary Image", bin_img)
        cv2.imwrite("media/images/output.jpg", bin_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pth = 'media/images/output.jpg'
        temp_obj = Hotel()
        temp_obj.name = 'output'
        temp_obj.hotel_Main_Img = cv2.imread(pth)
            
        print(mydata[0], temp_obj)
        return render(request, 'show_img.html', {'img_obj': mydata[0]})


def rgb2red(request):
    if request.method == 'POST':
        temp = request.POST.get("Name")
        print(temp)
        mydata = Hotel.objects.filter(name = temp)
        pth = str(mydata[0].hotel_Main_Img.url)
        pth = pth[1:]
        print(pth)


        img = cv2.imread(pth)
        # img = cv2.resize(img, (1280,720))
        # cv2.imshow("Color image", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        b, g, r = cv2.split(img)
        zeroes = np.zeros(img.shape[0:2], dtype="uint8")
        red_img = cv2.merge([zeroes, zeroes, r])
        cv2.imshow("Blue image", red_img)
        cv2.imwrite("media/images/output.jpg", red_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pth = 'media/images/output.jpg'
        temp_obj = Hotel()
        temp_obj.name = 'output'
        temp_obj.hotel_Main_Img = cv2.imread(pth)
            
        print(mydata[0], temp_obj)
        return render(request, 'show_img.html', {'img_obj': mydata[0]})

def rgb2log(request):
    if request.method == 'POST':
        temp = request.POST.get("Name")
        print(temp)
        mydata = Hotel.objects.filter(name = temp)
        pth = str(mydata[0].hotel_Main_Img.url)
        pth = pth[1:]
        print(pth)

        image = cv2.imread(pth)
        # Convert the image to float32 for mathematical operations
        image = image.astype(np.float32)

        # Apply the log transformation on each channel of the image
        log_image = np.log1p(image)

        # Convert the transformed image back to the original data type
        log_image = log_image.astype(image.dtype)
        cv2.imshow('Log Transformed Image', log_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return render(request, 'show_img.html', {'img_obj': mydata[0]})
    
def rgb2logi(request):
    if request.method == 'POST':
        temp = request.POST.get("Name")
        print(temp)
        mydata = Hotel.objects.filter(name = temp)
        pth = str(mydata[0].hotel_Main_Img.url)
        pth = pth[1:]
        print(pth)

        image = cv2.imread(pth)
       # Convert the image to float32 for mathematical operations
        image = image.astype(np.float32)

        # Apply the exponential function on each channel of the image
        inv_log_image = np.expm1(image)

        # Scale the values back to the original range
        inv_log_image = inv_log_image * 255 / np.max(inv_log_image)

        # Convert the transformed image to the original data type
        inv_log_image = inv_log_image.astype(image.dtype)
        cv2.imshow('Log Transformed Image', inv_log_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return render(request, 'show_img.html', {'img_obj': mydata[0]})
