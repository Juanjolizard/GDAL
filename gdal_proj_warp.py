#####se va a convertir /reproyectar el raster desde un crs a otro, desde 25830 a 4326, si el crs ya fuera 4326 no sería necesaria tal reproyección, para ello se va a emplear gdal.Warp(dst_file, src_file, **kwargs)

import gdal
import os
import logging

logfmt = '[%(levelname)s][%(asctime)s] %(message)s'
dtfmt = '%Y-%m-%d %I:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=logfmt, datefmt=dtfmt)

ds_source = 'C:/raster_input/local.tif'

ds_target = 'C:/raster_output/local_warped_4326.tif'

raster = gdal.Open(ds_source) #### ya tenemos la posibilidad de manipular el raster

src_dst = 'EPSG:4326'
cols = raster.RasterXSize ###width
rows = raster.RasterYSize ###height


proj = raster.GetProjection()
proj[:80] ####80 primeros caracteres de la proyección, en formato librería proj4
if '4326' in proj[:80]:
    logging.info(f'=>Not needed warping {os.path.basename(ds_source)}')
else:
    try:
        gdal.Warp(ds_target, ds_source, dstSRS=src_dst, width=cols, height=rows, resampleAlg='near', polynomialOrder=1, options=['COMPRESS=LZW'])
        logging.info(f'=>Warping image {os.path.basename(ds_source)}')
    except Exception as err:
        logging.error(err)
