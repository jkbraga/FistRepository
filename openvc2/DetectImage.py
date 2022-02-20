import cv2
import time


def main(args):

    camera_port = 0

    nFrames = 30

    camera = cv2.VideoCapture(camera_port)

    file = "./image/carrossel.png"

   # print "Digite <ESC> para sair / <s> para Salvar"

    emLoop = True

    while(emLoop):

        retval, img = camera.read()
        cv2.imshow('Foto', img)

    import sys
    sys.exit(main(sys.argv))
