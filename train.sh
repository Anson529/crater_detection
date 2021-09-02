# CUDA_VISIBLE_DEVICES=1
# nohup python -u tools/train.py configs/crater/deformable_detr_r50_crater.py > log/T4.log&
# nohup python -u tools/train.py configs/crater/fcos.py --work-dir work_dirs/deformable_detr_r50_pretrain_new --gpu-ids 1 > log/T10.log&
# nohup python -u tools/train.py configs/crater/deformable_detr_r50_crater_pretrain.py --work-dir work_dirs/detr_get > log/T11.log&
nohup python -u tools/train.py configs/crater/fcos_r50_crater_pretrain.py --work-dir work_dirs/fcos_new_config  > log/T12.log&