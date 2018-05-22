import cv2
import copy

def main():
    mirror = True
    scan_height = 6

    cam = cv2.VideoCapture(0)

    while True:
        ret_val, img = cam.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = img.shape

        if mirror: 
            img = cv2.flip(img, 1)

        #cv2.imshow("Binarized", cv2.adaptiveThreshold(copy.deepcopy(img), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 255, 1))
        
        #Whole image
        preview = cv2.rectangle(cv2.cvtColor(copy.deepcopy(img), cv2.COLOR_GRAY2RGB), (0, (height / 2 - 3)), (width, (height / 2 + 3)), (0, 255, 255), -1)

        img = img[(height / 2 - scan_height / 2):(height / 2 + scan_height / 2), 0:img.shape[1]]

        averages = []

        for i in range(width):
            average_point = 0

            for j in range(scan_height):
                average_point += img[j, i]

            average_point /= scan_height

            averages.append(average_point)

        squares = []

        for i in range(len(averages) / scan_height):
            average_point = 0

            for j in range(i * scan_height, (i + 1) * scan_height):
                average_point += averages[j]
                
            average_point /= scan_height

            squares.append(average_point)

        contrast = 0

        for i in range(1, len(squares)):
            if squares[i] - squares[i - 1] > 50:
                contrast = scan_height * i

        print(float(contrast) / float(width))
    

        #Print
        cv2.imshow("Preview", preview)
        cv2.imshow("Workspace", img)

        if cv2.waitKey(1) == 27: 
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
