# The new config inherits a base config to highlight the necessary modification
_base_ = '/home/yewenjie/mmdetection/configs/deformable_detr/deformable_detr_twostage_refine_r50_16x2_50e_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(num_classes=1)
)

# Modify dataset related settings
dataset_type = 'CocoDataset'
data_root = '/mnt/yewenjie/craterData/'
classes = ('crater',)

data = dict(
    train=dict(
        img_prefix='/mnt/yewenjie/craterData/train/',
        ann_file='/mnt/yewenjie/craterData/train/annotation_coco.json',
        classes = classes),
    val=dict(
        img_prefix='/mnt/yewenjie/craterData/val/',
        ann_file='/mnt/yewenjie/craterData/val/annotation_coco.json',
        classes = classes),
    test=dict(
        img_prefix='/mnt/yewenjie/craterData/train/',
        ann_file='/mnt/yewenjie/craterData/train/annotation_coco.json',
        classes = classes),
)

# We can use the pre-trained Mask RCNN model to obtain higher performance
# load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'