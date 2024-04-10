# -*- coding: utf-8 -*-
import glfw
from OpenGL.GL import *
if not glfw.init():
    sys.exit()
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 1)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 4)
window = glfw.create_window(800, 600, "Hello World", None, None)
if not window:
    sys.exit()
glfw.make_context_current(window)
glEnable(GL_BLEND)
glClearColor(1.0/255.0*68.0, 1.0/255.0*68.0, 1.0/255.0*68.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT)
glViewport(0, 0, 800, 600)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0.0, 800.0, 600.0, 0.0, 0.0, 1.0)

import numpy
from PIL import Image # pillow
def ReadTexture( filename):
  # PIL can open BMP, EPS, FIG, IM, JPEG, MSP, PCX, PNG, PPM
  # and other file types.  We convert into a texture using GL.
  print('trying to open', filename)
  try:
     image = Image.open(filename)
  except IOError as ex:
     print('IOError: failed to open texture file')
     message = template.format(type(ex).__name__, ex.args)
     print(message)
     return -1
  print('opened file: size=', image.size, 'format=', image.format)
  imageData = numpy.array(list(image.getdata()), numpy.uint8)

  textureID = glGenTextures(1)
  glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
  glBindTexture(GL_TEXTURE_2D, textureID)
  glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST);
  glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST);
  glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE);
  glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
  glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1],
     0, GL_RGB, GL_UNSIGNED_BYTE, imageData)

  image.close()
  return textureID

import sys
def get_user_input(str):
    if sys.version_info[0] < 3:
        return raw_input(str)
    else:
        return input(str)
print("started")

texture_id = ReadTexture("loading.png")
while True:
    glfw.poll_events()            
    glClear(GL_COLOR_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(0,0)
    glTexCoord2f(0, 1)
    glVertex2f(0,100)
    glTexCoord2f(1, 1)
    glVertex2f(100,100)
    glTexCoord2f(1, 0)
    glVertex2f(100,0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glfw.swap_buffers(window)

glfw.destroy_window(window)
glfw.terminate()

get_user_input("PRESS ENTER")