import numpy as np


def computeAPPSA(groundTruth, recovered):
    """
    Compute Average Per-Pixel Spectral Angle (APPA) between the recovered and
    the corresponding ground-truth image

    :param groundTruth: ground truth reference image.
    (Height x Width x Spectral_Dimension)

    :param recovered: image under evaluation.
    (Height x Width x Spectral_Dimension)
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    nom = np.sum(groundTruth * recovered, axis=2)
    denom = np.linalg.norm(groundTruth, axis=2) * \
        np.linalg.norm(recovered, axis=2)

    cos = np.where((nom / (denom + 1e-15)) > 1, 1, (nom / (denom + 1e-15)))
    appsa = np.arccos(cos)

    return np.sum(appsa) / (groundTruth.shape[1] * groundTruth.shape[0])


def computeMAngE(groundTruth, recovered):
    """
    Compute Mean Angular Error (MangE) between the recovered and
    the corresponding ground-truth image

    :param groundTruth: ground truth reference image.
    (Height x Width x Spectral_Dimension)

    :param recovered: image under evaluation.
    (Height x Width x Spectral_Dimension)
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)

    inner_product = np.sum(groundTruth * recovered, axis=2)   # DIM_DATA,
    normalized_inner_product = inner_product /
    (np.linalg.norm(groundTruth, axis=2) + 1e-15) /
    (np.linalg.norm(recovered, axis=2) + 1e-15)

    mangE = np.arccos(normalized_inner_product) * 180 / np.pi
    mangE *= np.sqrt(np.mean(groundTruth, axis=2))

    return mangE


def computeSAM(groundTruth, recovered):
    """
    Compute Spectral Angle Mapper (SAM) between the recovered and
    the corresponding ground-truth image

    :param groundTruth: ground truth reference image.
    (Height x Width x Spectral_Dimension)

    :param recovered: image under evaluation.
    (Height x Width x Spectral_Dimension)
    """
    assert groundTruth.shape == recovered.shape, \
        "Size not match for groundtruth and recovered spectral images"
    groundTruth = np.clip(groundTruth.astype("float64"), 0, 1)
    recovered = np.clip(recovered.astype("float64"), 0, 1)
    H = groundTruth.shape[0]
    W = groundTruth.shape[1]
    C = groundTruth.shape[2]

    nom = np.sum(np.multiply(groundTruth, recovered), axis=2)
    denom1 = np.sqrt(np.sum(np.power(groundTruth, 2), axis=2))
    denom2 = np.sqrt(np.sum(np.power(recovered, 2), axis=2))
    sam = np.arccos(np.divide(nom, np.multiply(denom1, denom2)))
    sam = np.multiply(np.divide(sam, np.pi), 180)
    sam = np.divide(np.sum(sam), H*W)
    return sam
