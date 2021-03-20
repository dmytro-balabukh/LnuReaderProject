# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..developer import MedicAlgorithmSPECTRE2010


def test_MedicAlgorithmSPECTRE2010_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inApply=dict(
            argstr="--inApply %s",
        ),
        inAtlas=dict(
            argstr="--inAtlas %s",
            extensions=None,
        ),
        inBackground=dict(
            argstr="--inBackground %f",
        ),
        inCoarse=dict(
            argstr="--inCoarse %f",
        ),
        inCost=dict(
            argstr="--inCost %s",
        ),
        inDegrees=dict(
            argstr="--inDegrees %s",
        ),
        inFind=dict(
            argstr="--inFind %s",
        ),
        inFine=dict(
            argstr="--inFine %f",
        ),
        inImage=dict(
            argstr="--inImage %s",
        ),
        inInhomogeneity=dict(
            argstr="--inInhomogeneity %s",
        ),
        inInitial=dict(
            argstr="--inInitial %d",
        ),
        inInitial2=dict(
            argstr="--inInitial2 %f",
        ),
        inInput=dict(
            argstr="--inInput %s",
            extensions=None,
        ),
        inMMC=dict(
            argstr="--inMMC %d",
        ),
        inMMC2=dict(
            argstr="--inMMC2 %d",
        ),
        inMaximum=dict(
            argstr="--inMaximum %f",
        ),
        inMinimum=dict(
            argstr="--inMinimum %f",
        ),
        inMinimum2=dict(
            argstr="--inMinimum2 %f",
        ),
        inMultiple=dict(
            argstr="--inMultiple %d",
        ),
        inMultithreading=dict(
            argstr="--inMultithreading %s",
        ),
        inNumber=dict(
            argstr="--inNumber %d",
        ),
        inNumber2=dict(
            argstr="--inNumber2 %d",
        ),
        inOutput=dict(
            argstr="--inOutput %s",
        ),
        inOutput2=dict(
            argstr="--inOutput2 %s",
        ),
        inOutput3=dict(
            argstr="--inOutput3 %s",
        ),
        inOutput4=dict(
            argstr="--inOutput4 %s",
        ),
        inOutput5=dict(
            argstr="--inOutput5 %s",
        ),
        inRegistration=dict(
            argstr="--inRegistration %s",
        ),
        inResample=dict(
            argstr="--inResample %s",
        ),
        inRun=dict(
            argstr="--inRun %s",
        ),
        inSkip=dict(
            argstr="--inSkip %s",
        ),
        inSmoothing=dict(
            argstr="--inSmoothing %f",
        ),
        inSubsample=dict(
            argstr="--inSubsample %s",
        ),
        inUse=dict(
            argstr="--inUse %s",
        ),
        null=dict(
            argstr="--null %s",
        ),
        outFANTASM=dict(
            argstr="--outFANTASM %s",
            hash_files=False,
        ),
        outMask=dict(
            argstr="--outMask %s",
            hash_files=False,
        ),
        outMidsagittal=dict(
            argstr="--outMidsagittal %s",
            hash_files=False,
        ),
        outOriginal=dict(
            argstr="--outOriginal %s",
            hash_files=False,
        ),
        outPrior=dict(
            argstr="--outPrior %s",
            hash_files=False,
        ),
        outSegmentation=dict(
            argstr="--outSegmentation %s",
            hash_files=False,
        ),
        outSplitHalves=dict(
            argstr="--outSplitHalves %s",
            hash_files=False,
        ),
        outStripped=dict(
            argstr="--outStripped %s",
            hash_files=False,
        ),
        outd0=dict(
            argstr="--outd0 %s",
            hash_files=False,
        ),
        xDefaultMem=dict(
            argstr="-xDefaultMem %d",
        ),
        xMaxProcess=dict(
            argstr="-xMaxProcess %d",
            usedefault=True,
        ),
        xPrefExt=dict(
            argstr="--xPrefExt %s",
        ),
    )
    inputs = MedicAlgorithmSPECTRE2010.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_MedicAlgorithmSPECTRE2010_outputs():
    output_map = dict(
        outFANTASM=dict(
            extensions=None,
        ),
        outMask=dict(
            extensions=None,
        ),
        outMidsagittal=dict(
            extensions=None,
        ),
        outOriginal=dict(
            extensions=None,
        ),
        outPrior=dict(
            extensions=None,
        ),
        outSegmentation=dict(
            extensions=None,
        ),
        outSplitHalves=dict(
            extensions=None,
        ),
        outStripped=dict(
            extensions=None,
        ),
        outd0=dict(
            extensions=None,
        ),
    )
    outputs = MedicAlgorithmSPECTRE2010.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
