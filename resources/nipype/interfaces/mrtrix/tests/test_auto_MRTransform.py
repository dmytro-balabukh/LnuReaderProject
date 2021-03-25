# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import MRTransform


def test_MRTransform_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        debug=dict(
            argstr="-debug",
            position=1,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        flip_x=dict(
            argstr="-flipx",
            position=1,
        ),
        in_files=dict(
            argstr="%s",
            mandatory=True,
            position=-2,
        ),
        invert=dict(
            argstr="-inverse",
            position=1,
        ),
        out_filename=dict(
            argstr="%s",
            extensions=None,
            genfile=True,
            position=-1,
        ),
        quiet=dict(
            argstr="-quiet",
            position=1,
        ),
        reference_image=dict(
            argstr="-reference %s",
            extensions=None,
            position=1,
        ),
        replace_transform=dict(
            argstr="-replace",
            position=1,
        ),
        template_image=dict(
            argstr="-template %s",
            extensions=None,
            position=1,
        ),
        transformation_file=dict(
            argstr="-transform %s",
            extensions=None,
            position=1,
        ),
    )
    inputs = MRTransform.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MRTransform_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = MRTransform.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
