# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..wrappers import Function


def test_Function_inputs():
    input_map = dict(
        function_str=dict(
            mandatory=True,
        ),
    )
    inputs = Function.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Function_outputs():
    output_map = dict()
    outputs = Function.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value