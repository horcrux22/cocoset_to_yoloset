import os
import consts


def checking():
    if not os.path.exists(consts.LABELS):
        os.makedirs(consts.LABELS)

    if not os.path.exists(consts.IMAGES):
        os.makedirs(consts.IMAGES)
