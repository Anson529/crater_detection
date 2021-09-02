# The new config inherits a base config to highlight the necessary modification
_base_ = '../fcos/fcos_r50_caffe_fpn_gn-head_1x_coco.py'

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
        img_prefix='/mnt/yewenjie/craterData/3/',
        ann_file='/mnt/yewenjie/craterData/3/annotation.json',
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


# lr_config = dict(
#     policy='step',
#     warmup='constant',
#     warmup_iters=500,
#     warmup_ratio=1.0 / 3,
#     step=[20, 30])
# runner = dict(type='EpochBasedRunner', max_epochs=20)

# We can use the pre-trained Mask RCNN model to obtain higher performance