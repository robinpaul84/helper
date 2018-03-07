import os
import argparse
a = argparse.ArgumentParser()
a.add_argument("-f", "--folder", help="folder")
a.add_argument("-v" ,"--video", help="video")
a.add_argument("-d" ,"--delay", type = int, help="delay in seconds")
args = a.parse_args()
folder = str(args.folder)
if not os.path.exists(folder):
    os.mkdir(folder)
# use opencv to do the job
import cv2
vidcap = cv2.VideoCapture(args.video)
count = 0
while True:
    vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000  *  args.delay))
    success,image = vidcap.read()
    if not success:
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))