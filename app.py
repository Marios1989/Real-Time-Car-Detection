import cv2

video = cv2.VideoCapture('/home/user/Downloads/cars.mp4')

cars_cascade = cv2.CascadeClassifier('/home/user/PycharmProjects/Real-time-Vehicle-Dection-Python/haarcascade_car.xml')

if video.isOpened == False:
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('filename.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)


def detect_cars(frame):
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w,y+h), color=(0, 255, 0), thickness=2)
    return frame


def Simulator():
    CarVideo = cv2.VideoCapture('/home/user/Downloads/cars.mp4')
    while CarVideo.isOpened():
        ret, frame = CarVideo.read()
        controlkey = cv2.waitKey(1)
        if ret:        
            cars_frame = detect_cars(frame)
            result.write(frame)
            cv2.imshow('frame', cars_frame)
        else:
            break
        if controlkey == ord('q'):
            break

    CarVideo.release()
    video.release()
    result.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Simulator()