
import pyaudio
import wave

import cv2
def dancegame():
    target_tone = True
    chunk = 1024
    player = pyaudio.PyAudio()

    cv2.namedWindow("Camera")
    cam = cv2.VideoCapture(1)

    if cam.isOpened():
        rval, frame = cam.read()
        rval, framex = cam.read()
    else:
        rval = False

    while rval:
        syes = wave.open("yes.wav",'rb')
        snon = wave.open("non.wav",'rb')
        data_y = syes.readframes(chunk)
        data_n = snon.readframes(chunk)
        ssyes = player.open(format = player.get_format_from_width(syes.getsampwidth()), channels = syes.getnchannels(), rate = syes.getframerate(), output = True)
        ssnon = player.open(format = player.get_format_from_width(snon.getsampwidth()), channels = snon.getnchannels(), rate = snon.getframerate(), output = True)
    
        cv2.imshow('Camera', frame[:,::-1])
        rval, frame = cam.read()

        key = cv2.waitKey(20)
        if key == 27: # press ESC to close
            break

        dst = cv2.absdiff(frame, framex)

        #cv2.imshow("Overlay", dst[:,::-1])
        h, w, ch = frame.shape
        leftQuad = cv2.rectangle(dst, (0, 0), (w // 2, h), (255, 255, 255), 2)[0:h, w//2:w]
        #cv2.imshow("Left", leftQuad)

        rightQuad = cv2.rectangle(dst, (w//2, 0), (w, h), (255, 255, 255), 2)[0:h, 0:w//2]
        #cv2.imshow("Right", rightQuad)

        if (target_tone):
            print('Go Left')
        else:
            print('Go Right')

        count1 = sum(1 for x in leftQuad.flatten() if x > 10)
        count2 = sum(1 for y in rightQuad.flatten() if y > 10)

        if count1 > count2:
            print('left')
            while len(data_y) > 0:
                ssyes.write(data_y)
                data_y = syes.readframes(chunk)
            ssyes.stop_stream()
            ssyes.close()

            if target_tone == True:
                target_tone = not target_tone

                yyes2 = wave.open("open.wav",'rb')
                data_yy2 = yyes2.readframes(chunk)
                ysyes2 = player.open(format = player.get_format_from_width(yyes2.getsampwidth()), channels = yyes2.getnchannels(), rate = yyes2.getframerate(), output = True)
                while len(data_yy2) > 0:
                    ysyes2.write(data_yy2)
                    data_yy2 = yyes2.readframes(chunk)
                ysyes2.stop_stream()
                ysyes2.close()
        elif count1 < count2:
            print('right')
            while len(data_n) > 0:
                ssnon.write(data_n)
                data_n = snon.readframes(chunk)
            ssnon.stop_stream()
            ssnon.close()

            if False == target_tone:
                target_tone = not target_tone

                yyes = wave.open("chirp_4.wav",'rb')
                data_yy = syes.readframes(chunk)
                ysyes = player.open(format = player.get_format_from_width(yyes.getsampwidth()), channels = yyes.getnchannels(), rate = yyes.getframerate(), output = True)
                while len(data_yy) > 0:
                    ysyes.write(data_yy)
                    data_yy = yyes.readframes(chunk)
                ysyes.stop_stream()
                ysyes.close()
        else:
            print('none')
        framex = frame
    player.terminate()

if __name__ == '__main__':
    dancegame()
