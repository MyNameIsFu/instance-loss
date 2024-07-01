from monai.losses import DiceLoss
from instance_loss.InstanceLoss import InstanceLoss


def getDefaultInstanceLoss():
    """ returns the default loss configuration as initialized
    in the corresponding 'example_colab' notebook.
    """
    loss_dice = DiceLoss(
        to_onehot_y=False,
        sigmoid=False,
        softmax=False
    )

    loss_dice_center = DiceLoss(
        to_onehot_y=False,
        sigmoid=False,
        softmax=False
    )

    activation="none"
    num_out_chn = 1
    object_chn = 1
    mul_too_many = 50
    centroid_offset = 3
    num_iterations = 250
    max_false_detections = 50
    rate_instead_number = True

    return InstanceLoss(
        loss_function_pixel=loss_dice,
        loss_function_instance=loss_dice_center,
        loss_function_center=loss_dice_center,
        activation=activation,
        num_out_chn=num_out_chn,
        object_chn=object_chn,
        mul_too_many=mul_too_many,
        max_cc_out=max_false_detections,
        num_iterations=num_iterations,
        centroid_offset=centroid_offset,
        rate_instead_number=rate_instead_number,
        instance_wise_loss_no_tp=True,
        spatial_dims=2
    )