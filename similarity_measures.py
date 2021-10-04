import numpy as np
from skimage.metrics import structural_similarity as compare_ssim


def computeGFC(groundTruth, recovered):
    """
    Compute Goodness-of-Fit Coefficient (GFC) between the recovered and the
    corresponding ground-truth image

    :param groundTruth: ground truth reference image.
        numpy.ndarray (Height x Width x Spectral_Dimension)
    :param recovered: image under evaluation.
        numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        GFC between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    GFCn = np.sum(np.multiply(groundTruth, recovered), axis=2)
    GFCd = np.multiply(np.sqrt(np.sum(np.power(groundTruth, 2), axis=2)),
                       np.sqrt(np.sum(np.power(recovered, 2), axis=2)))
    GFC = np.divide(GFCn, GFCd)
    return np.mean(GFC)


def computeMSSIM(groundTruth, recovered):
    """
    Compute Mean Structural SImilarity Measure (MSSIM) between
    the recovered and the corresponding ground-truth image

    Args:
        :param groundTruth: ground truth reference image.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param rc: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        MSSIM between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    # to get SSIM put full = True to get values instead of mean
    return compare_ssim(groundTruth, recovered, multichannel=True)
