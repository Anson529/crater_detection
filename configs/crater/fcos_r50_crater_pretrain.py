# The new config inherits a base config to highlight the necessary modification
_base_ = '../fcos/fcos_center-normbbox-centeronreg-giou_r50_caffe_fpn_gn-head_dcn_1x_coco.py'

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
        img_prefix='/mnt/yewenjie/craterData/get/',
        ann_file='/mnt/yewenjie/craterData/get/annotation.json',
        filter_empty_gt=False,
        classes = classes),
    val=dict(
        img_prefix='/mnt/yewenjie/craterData/val/',
        ann_file='/mnt/yewenjie/craterData/val/annotation_coco.json',
        classes = classes),
    test=dict(
        img_prefix='/mnt/yewenjie/craterData/split/',
        ann_file='/mnt/yewenjie/craterData/split/annotation_coco.json',
        classes = classes),
)

# lr_config = dict(
#     policy='step',
#     warmup='constant',
#     warmup_iters=500,
#     warmup_ratio=1.0 / 3,
#     step=[20, 30])
# runner = dict(type='EpochBasedRunner', max_epochs=20)
# runner = dict(type='EpochBasedRunner', max_epochs=15)

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = '/home/yewenjie/mmdetection/work_dirs/fcos_r50_crater_pretrain_new/latest.pth'