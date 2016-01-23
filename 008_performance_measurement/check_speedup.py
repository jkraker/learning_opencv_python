import cv2

img1 = cv2.imread('messi5.jpg')

cv2.setUseOptimized(False)
print "Optimized:", cv2.useOptimized()
e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t_no = (e2 - e1)/cv2.getTickFrequency()
print "time to run:",t_no,"sec"

cv2.setUseOptimized(True)
print "Optimized:", cv2.useOptimized()
e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t_yes = (e2 - e1)/cv2.getTickFrequency()
print "time to run:",t_yes,"sec"

print "non-optimized code takes",t_no/t_yes,"times longer"
