import pymel.core as pm

def fitToBoundingBox(fitType = None):
    objs = pm.ls(sl=True, fl=True)

    if len(objs) > 1:
        bboxfit = pm.exactWorldBoundingBox(objs[0:-1])
        lxfit = bboxfit[3] - bboxfit[0]
        cxfit = bboxfit[0] + lxfit / 2
        lyfit = bboxfit[4] - bboxfit[1]
        cyfit = bboxfit[1] + lyfit / 2
        lzfit = bboxfit[5] - bboxfit[2]
        czfit = bboxfit[2] + lzfit / 2

        bbox = pm.exactWorldBoundingBox(objs[-1])
        lx = bbox[3]-bbox[0]
        cx = bbox[0] + lx / 2
        ly = bbox[4]-bbox[1]
        cy = bbox[1] + ly / 2
        lz = bbox[5]-bbox[2]
        cz = bbox[2] + lz / 2

        scalex = lxfit/lx
        scaley = lyfit/ly
        scalez = lzfit/lz

        if fitType == 'min':
            scale = scalex if scalex < scaley else scaley
            scale = scale if scale < scalez else scalez
            scalex = scaley = scalez = scale
        elif fitType == 'max':
            scale = scalex if scalex > scaley else scaley
            scale = scale if scale > scalez else scalez
            scalex = scaley = scalez = scale

        pm.scale( objs[-1], scalex, scaley, scalez, p=(cx, cy, cz), r=True )
        pm.move( cxfit-cx, cyfit-cy, czfit-cz, objs[-1], r=True )

def fitToBoundingBoxMax():
    fitToBoundingBox(fitType = 'max')

def fitToBoundingBoxMin():
    fitToBoundingBox(fitType = 'min')
