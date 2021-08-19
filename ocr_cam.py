import easyocr
import cv2 as cv

# initialize the instance of the easyocr reader to read english text;
reader = easyocr.Reader(['en'], gpu=False)
# start capturing video from the input 0;
cap = cv.VideoCapture(0)
# change the size of the frames;
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 175)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 175)

while True:
    # capture frame-by-frame;
    ret, frame = cap.read()
    font = cv.FONT_HERSHEY_SIMPLEX
    # show the video window;
    cv.imshow('Video', frame)
    # save the result of the processed frame;
    result = reader.readtext(frame)
    if result:
        # retrieve the coordinates;
        # int() - conversion from float;
        top_left = tuple([int(val) for val in result[0][0][0]])
        bottom_right = tuple([int(val) for val in result[0][0][2]])
        # retrieve the text;
        text = result[0][1]
        # draw the rectangle on the frame around the text;
        cv.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)
        # get the height of the frame;
        frame_height = int(cap.get(4))
        # get the coordinate of the left bottom to put the text;
        left_bottom = (0, frame_height - 5)
        # place the text on the rectangular left bottom;
        cv.putText(frame, text, left_bottom, font, 0.7, (0, 0, 255), 1, cv.LINE_AA)
        # show the video;
        cv.imshow('Video', frame)
    if cv.waitKey(1) == ord('q'):
        break

# when everything done, release the capture;
cap.release()
cv.destroyAllWindows()
