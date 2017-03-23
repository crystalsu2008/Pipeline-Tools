import pymel.core as pm

def muscleProducer(muscleData):
    locStart1 = muscleData['locStart1']
    locStart2 = muscleData['locStart2']
    locEnd1 = muscleData['locEnd1']
    locEnd2 = muscleData['locEnd2']

    baseName = muscleData['baseName']
    nMidControls = muscleData['nMidControls']
    nAround = muscleData['nAround']
    nAround = muscleData['nPrimaryAxis']
