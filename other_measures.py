import numpy as np


def computeMSID(groundTruth, recovered):
    """
    Compute Mean Spectral Information Divergence (MSID) between
    the recovered and the corresponding ground-truth image

    Args:
        :param groundTruth: ground truth reference image.
            numpy.ndarray (Height x Width x Spectral_Dimension)
        :param recovered: image under evaluation.
            numpy.ndarray (Height x Width x Spectral_Dimension)

    Returns:
        MSID between `recovered` and `groundTruth`
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)

    H = groundTruth.shape[0]
    W = groundTruth.shape[1]
    err = np.zeros(H * W)
    i = 0
    for h in range(H):
        for w in range(W):
            sumRC = np.sum(recovered[h, w, :])
            sumGT = np.sum(groundTruth[h, w, :])

            logRC = np.log((recovered[h, w, :] / sumRC + 1e-15) /
                           (groundTruth[h, w, :] / sumGT + 1e-15))

            logGT = np.log((groundTruth[h, w, :] / sumGT + 1e-15) /
                           (recovered[h, w, :] / sumRC + 1e-15))

            err[i] = abs(np.sum(recovered[h, w, :] * logRC) +
                         np.sum(groundTruth[h, w, :] * logGT))
            i += 1
    return err.mean()
