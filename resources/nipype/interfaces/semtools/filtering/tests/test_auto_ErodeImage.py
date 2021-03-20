# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..featuredetection import ErodeImage


def test_ErodeImage_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputMaskVolume=dict(
            argstr="--inputMaskVolume %s",
            extensions=None,
        ),
        inputRadius=dict(
            argstr="--inputRadius %d",
        ),
        inputVolume=dict(
            argstr="--inputVolume %s",
            extensions=None,
        ),
        outputVolume=dict(
            argstr="--outputVolume %s",
            hash_files=False,
        ),
    )
    inputs = ErodeImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ErodeImage_outputs():
    output_map = dict(
        outputVolume=dict(
            extensions=None,
        ),
    )
    outputs = ErodeImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
