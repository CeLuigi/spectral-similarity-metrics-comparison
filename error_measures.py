import numpy as np


def computeMSE(groundTruth, recovered):
    """
    Compute Mean Square Error (MSE) between the recovered and the
    corresponding ground-truth image

    Args:
        :param groundTruth: ground truth reference image.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param recovered: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        MSE between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    square_diff = np.power(groundTruth - recovered, 2)
    mse = np.mean(square_diff)

    return mse


def computeRMSE(groundTruth, recovered):
    """
    Compute Root Mean Square Error (RMSE) between the recovered and the
    corresponding ground-truth image

    :param groundTruth: ground truth reference image.
        numpy.ndarray (Height x Width x Spectral_Dimension)
    :param recovered: image under evaluation.
        numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        RMSE between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    square_diff = np.power(groundTruth - recovered, 2)
    rmse = np.sqrt(np.mean(square_diff))

    return rmse


def computeMRAE(groundTruth, recovered):
    """
    Compute Mean Relative Absolute Error (MRAE) between the recovered and the
    corresponding ground-truth image

    Args:
        :param groundTruth: ground truth reference image.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param recovered: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        MRAE between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    difference = np.abs(groundTruth - recovered) / (groundTruth + 1e-15)
    mrae = np.mean(difference)
    return mrae


def computeBPMRAE(groundTruth, recovered, crf=None, RGB=False):
    """
    Compute Back Projection Mean Relative Absolute Error (BPMRAE) between
    the recovered and the corresponding ground-truth image

    Args:
        :param groundTruth: ground truth reference image.
            numpy.ndarray (Height x Width x d). d = 3 if RGB = `True`,
            otherwise d = Spectral_Dimension
        :param recovered: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param crf: camera response functions.
            numpy.ndarray (Spectral_Dimension x 3)

    Returns:
        BPMRAE between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"

    if not RGB:
        assert groundTruth.shape[2] == crf.shape[0], \
           "Spectral dimension mismatch between spectral images and " + \
           "camera response functions"
        groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
        recovered = np.clip(recovered.astype("float64"), 0, 1)
        specDim = crf.shape[0]  # spectral dimension

        # back projection + reshape the data into
        #   num_of_samples x spectral_dimensions
        groundTruthRGB = np.matmul(groundTruth.reshape(-1, specDim), crf)
        recoveredRGB = np.matmul(recovered.reshape(-1, specDim), crf)

        # plopt gt or reconstructed image
        rgbIm = np.dot(groundTruth, crf)
        rgbIm = np.true_divide(rgbIm, np.sum(crf[:, 1]))
        rgbIm = np.clip(rgbIm.astype("float64"), 0, 1)

        rgbIm = np.dot(recovered, crf)
        rgbIm = np.true_divide(rgbIm, np.sum(crf[:, 1]))
        rgbIm = np.clip(rgbIm.astype("float64"), 0, 1)
    else:
        groundTruthRGB = groundTruth
        recoveredRGB = recovered

    # calculate MRAE
    difference = np.abs(groundTruthRGB-recoveredRGB) / (groundTruthRGB + 1e-15)
    mrae = np.mean(difference)

    return mrae


def computePSNR(groundTruth, recovered):
    """
    Compute Peak Signal-to-Noise Ratio (PSNR) between the recovered and the
    corresponding ground-truth image

    :param groundTruth: ground truth reference image.
        numpy.ndarray (Height x Width x Spectral_Dimension)
    :param recovered: image under evaluation.
        numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        PSNR between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    psnr = 20 * np.log10(1 / np.sqrt(computeMSE(groundTruth, recovered) + \
                         1e-15))
    return psnr
