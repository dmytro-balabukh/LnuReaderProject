# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import Normalize


def test_Normalize_inputs():
    input_map = dict(
        DCT_period_cutoff=dict(
            field="eoptions.cutoff",
        ),
        affine_regularization_type=dict(
            field="eoptions.regtype",
        ),
        apply_to_files=dict(
            copyfile=True,
            field="subj.resample",
        ),
        jobtype=dict(
            usedefault=True,
        ),
        matlab_cmd=dict(),
        mfile=dict(
            usedefault=True,
        ),
        nonlinear_iterations=dict(
            field="eoptions.nits",
        ),
        nonlinear_regularization=dict(
            field="eoptions.reg",
        ),
        out_prefix=dict(
            field="roptions.prefix",
            usedefault=True,
        ),
        parameter_file=dict(
            copyfile=False,
            extensions=None,
            field="subj.matname",
            mandatory=True,
            xor=["source", "template"],
        ),
        paths=dict(),
        source=dict(
            copyfile=True,
            field="subj.source",
            mandatory=True,
            xor=["parameter_file"],
        ),
        source_image_smoothing=dict(
            field="eoptions.smosrc",
        ),
        source_weight=dict(
            copyfile=False,
            extensions=None,
            field="subj.wtsrc",
        ),
        template=dict(
            copyfile=False,
            extensions=None,
            field="eoptions.template",
            mandatory=True,
            xor=["parameter_file"],
        ),
        template_image_smoothing=dict(
            field="eoptions.smoref",
        ),
        template_weight=dict(
            copyfile=False,
            extensions=None,
            field="eoptions.weight",
        ),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver="8",
            usedefault=True,
        ),
        write_bounding_box=dict(
            field="roptions.bb",
        ),
        write_interp=dict(
            field="roptions.interp",
        ),
        write_preserve=dict(
            field="roptions.preserve",
        ),
        write_voxel_sizes=dict(
            field="roptions.vox",
        ),
        write_wrap=dict(
            field="roptions.wrap",
        ),
    )
    inputs = Normalize.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Normalize_outputs():
    output_map = dict(
        normalization_parameters=dict(),
        normalized_files=dict(),
        normalized_source=dict(),
    )
    outputs = Normalize.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
