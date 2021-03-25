# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import Registration


def test_Registration_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fixed_image=dict(
            argstr="-f %s",
            extensions=None,
            mandatory=True,
        ),
        fixed_mask=dict(
            argstr="-fMask %s",
            extensions=None,
        ),
        initial_transform=dict(
            argstr="-t0 %s",
            extensions=None,
        ),
        moving_image=dict(
            argstr="-m %s",
            extensions=None,
            mandatory=True,
        ),
        moving_mask=dict(
            argstr="-mMask %s",
            extensions=None,
        ),
        num_threads=dict(
            argstr="-threads %01d",
            nohash=True,
            usedefault=True,
        ),
        output_path=dict(
            argstr="-out %s",
            mandatory=True,
            usedefault=True,
        ),
        parameters=dict(
            argstr="-p %s...",
            mandatory=True,
        ),
    )
    inputs = Registration.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Registration_outputs():
    output_map = dict(
        transform=dict(),
        warped_file=dict(
            extensions=None,
        ),
        warped_files=dict(),
        warped_files_flags=dict(),
    )
    outputs = Registration.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value