import numpy as np
import cv2
import sys
import os
import math

CAMINHO_PROJETO = sys.path[0]

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def criarPasta(caminhoDir):
    if not os.path.exists(caminhoDir):
        os.makedirs(caminhoDir)

def abrirArquivo(imgName):
    img = cv2.imread(CAMINHO_PROJETO + "\\original\\" + imgName, 1)
    return img

def salvarImagem(imgName, img):
    pasta_destino = CAMINHO_PROJETO + "\\processed\\"
    criarPasta(pasta_destino)
    cv2.imwrite(pasta_destino + imgName, img)


#Questão 1
def clarearImagem(img):

    height, width = img.shape[0], img.shape[1]
    for y in range(height):
        for x in range(width):
            intensity_img = img[y,x]
            img[y,x] = 255 * (intensity_img/255)**0.6

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def escurecerImagem(img):

    height, width = img.shape[0], img.shape[1]
    b,g,r = cv2.split(img)
    for y in range(height):
        for x in range(width):
            r[y,x] = 255 * (r[y,x]/255)**1.56
            g[y,x] = 255 * (g[y,x]/255)**1.56
            b[y,x] = 255 * (b[y,x]/255)**1.56

    img = cv2.merge((b,g,r))
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def escurecerHSV(img):

    height, width = img.shape[0], img.shape[1]
    b,g,r = cv2.split(img)

    for y in range(height):
        for x in range(width):
            h, s, v = rgb2hsv(b[y,x],g[y,x],r[y,x])
            v *= 0.4
            s *= 0.9
            b2,g2,r2 = hsv2rgb(h,s,v)
            b[y,x] = b2
            g[y,x] = g2
            r[y,x] = r2

    img = cv2.merge((b,g,r))
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




imagem = abrirArquivo("Image_(1b).jpg")
#clarearImagem(imagem)
escurecerHSV(imagem)
