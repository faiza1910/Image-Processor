# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s):
# Date:
# Description:

import cmpt120imageProjHelper as ch
import numpy
import copy 

def ApplyRedFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Retains the R values of all pixels in the image, and sets G and B to zero
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      black[row][col] = [r,0,0]
   
  return black  

def ApplyGreenFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Retains the G values of all pixels in the image, and sets R and B to zero
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      g = pixels[row][col][1]
      black[row][col] = [0,g,0]
   
  return black

def ApplyBlueFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Retains the B values of all pixels in the image, and sets R and G to zero
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      b = pixels[row][col][2]
      black[row][col] = [0,0,b]
   
  return black

def SepiaFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Gives all colours of the img a warm brownish tone
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      sepiaRed = int((r * .393) + (g *.769) + (b * .189))
      sepiaGreen = int((r * .349) + (g *.686) + (b * .168))
      sepiaBlue = int((r * .272) + (g *.534) + (b * .131))
      black[row][col] = [min(255,sepiaRed),min(255,sepiaGreen),min(255,sepiaBlue)]
  
  return black 

def scale_down(value):
  """
  Input:  value - integer or float 
  Output: returns result- from the value scaled down 
  """
  if value<64:
    result = int(value/64 * 50)
  elif 64<=value<128:
    result = int((value-64)/(128-64) * (100-50) + 50)
  else:
    result = int((value-128)/(255-128) * (255-100) + 100)
  return result  

def scale_up(value):
  """
  Input:  value - integer or float 
  Output: returns result- from the value scaled up 
  """
  if value<64:
    result = int(value/64 * 80)
  elif 64<=value<128:
    result = int((value-64)/(128-64) * (160-80) + 80)  
  else:
    result = int((value-128)/(255-128) * (255-160) + 160) 
  return result  

def ApplyWarmFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Gives all colours of the img a warm tone
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      
      black[row][col] = [scale_up(r),g,scale_down(b)]
   
  return black  
   
def ApplyColdFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Gives all colours of the img a cold tone
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      black[row][col] = [scale_down(r),g,scale_up(b)]
   
  return black

def RotateLeft(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns the img rotated counter-clockwise by 90 degrees
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(height, width)
  for col in range(width):
    for row in range(height):
      black[col][row] = pixels[row][width-1-col]
 
  return black

def RotateRight(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns the img rotated clockwise by 90 degrees
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(height, width)
  for col in range(width):
    for row in range(height):
      black[col][row] = pixels[height-1-row][col]

  return black

def DoubleSize(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns an img with both width and height doubled
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage(2*width, 2*height)
  for row in range(height):
    for col in range(width):
          black[(2*row)+1][(2*col)+1] = pixels[row][col]
          black[2*row][2*col] = pixels[row][col]
          black[2*row][(2*col)+1] = pixels[row][col]
          black[(2*row)+1][2*col] = pixels[row][col]
  
  return black 

def HalfSize(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns an img with both width and height halved
  """
  height = len(pixels)
  width = len(pixels[0])
  black = ch.getBlackImage((width+1)//2, (height+1)//2)
  for row in range(height):
    for col in range(width):
          black[row//2][col//2] = pixels[row//2][col//2]
          black[row//2][col//2] = pixels[row][col//2]
          black[row//2][col//2] = pixels[row//2][col]
          black[row//2][col//2] = pixels[row][col]

  return black

def LocateFish(pixels): 
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns a deepcopy img of the fish with a drawn green bounding box around the fish
  """
  fish_copy = copy.deepcopy(pixels)
  height_f = len(pixels)
  width_f = len(pixels[0]) 

  #a list containing all the row and columns which contain the yellow pixels of the fish
  row_list = []
  col_list = []
  for row in range(height_f):
    for col in range(width_f):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      h = ch.rgb_to_hsv(r,g,b)[0]
      s = ch.rgb_to_hsv(r,g,b)[1]
      v = ch.rgb_to_hsv(r,g,b)[2]
      
      if 40<h<100 and 30<s<101 and 85<v<101:
        row_list.append(row)
        col_list.append(col)
  
  for row in range(height_f):
    for col in range(width_f):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      h = ch.rgb_to_hsv(r,g,b)[0]
      s = ch.rgb_to_hsv(r,g,b)[1]
      v = ch.rgb_to_hsv(r,g,b)[2]
      
      if 40<h<100 and 30<s<101 and 85<v<101:
        fish_copy[row][min(col_list)] = [0,255,0]
        fish_copy[min(row_list)][col] = [0,255,0]
        fish_copy[row][max(col_list)] = [0,255,0]
        fish_copy[max(row_list)][col] = [0,255,0]
      
  return fish_copy
    