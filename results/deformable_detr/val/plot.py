import mmcv
import cv2

data_infos = mmcv.load('bbox.json')

# print (data_infos)
print (len(data_infos))
fig = cv2.imread('mars_crater (91).jpg')
for v in data_infos:
    image_id = v['image_id']
    if image_id > 0:
        break

    bbox = v['bbox']
    print (fig.shape)
    BR = (int(bbox[1]), int(bbox[0]))
    TL = (int(bbox[3]), int(bbox[2]))
    print (TL, BR)
    
    cv2.rectangle(fig, TL, BR, (0, 255, 0), 3, 8)

cv2.imwrite('sample.png', fig)
    
    