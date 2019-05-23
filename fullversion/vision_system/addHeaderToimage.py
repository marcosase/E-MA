'''
Created on May 10, 2019

@author: rodrigo.guercio
'''
import tifffile
import numpy as np
import exifread
from typing import ByteString

def printtags(filename1):
    f = open(filename1, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)

    # Print the tag/ value pairs
    print(filename1)
    for tag in tags.keys():
        #print(tag)
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print ("Key: %s, value %s" % (tag, tags[tag]))

def numpyAndTags(addr):
    with tifffile.TiffFile(addr) as image:
        image_matrix = np.uint16(image.asarray()) #Now, it is numpy 
        tag = image.pages[0]
        alltags = []
        nametags = []
        for name,addr in tag.tags.items():
            tags_list =  [(tag.tags[name].code, tag.tags[name].dtype, tag.tags[name].count,tag.tags[name].value),False]
            alltags.append(tags_list)
            nametags.append(name)
        return image_matrix,tag,nametags,alltags

def findTag(addr,name = 'StripOffsets'):
    with tifffile.TiffFile(addr) as image:
        tag = image.pages[0]
        allStripOffsets = [(tag.tags[name].code, tag.tags[name].dtype, tag.tags[name].count,tag.tags[name].value, False)]
        allStripOffsets =  [(tag.tags[name].code, 'I', tag.tags[name].count,tag.tags[name].value[0], False)]
    return allStripOffsets

def writeimage(addr, matrix, tags, specialTag):
    with tifffile.TiffWriter(file = addr) as newimage:
        newimage.save(data=matrix,
                      photometric=tags.tags['PhotometricInterpretation'].value,
                      planarconfig=None,
                      extrasamples=None,
                      tile=None,
                      contiguous=True,
                      align=16,
                      truncate=False, 
                      compress=0,
                      rowsperstrip=tags.tags['RowsPerStrip'].value, 
                      predictor=False, 
                      colormap=None,
                      description=None,
                      datetime=None,
                      resolution=(tags.tags['XResolution'].value[0]/tags.tags['XResolution'].value[1],tags.tags['YResolution'].value[0]/tags.tags['YResolution'].value[1],'CENTIMETER'),
                      subfiletype=0,
                      software='tifffile.py', 
                      metadata={}, 
                      ijmetadata=None,
                      extratags=[(273, 'I', 1, 1, False)] )
    print('Ok')
    
    
def compare(i_addr,f_addr):
    '''Print tags'''
    printtags(i_addr)
    
    '''Any variable to do any operation'''
    accumulate_xds = 0 # This will be a numpy
    
    name_tag = 'StripOffsets'
    
    ''' Reading the file 1''' 
    [image_matrix_xds,tag_xds, nametags_xds, alltags_xds] = numpyAndTags(addr = i_addr)
    allStripOffsets_xds = findTag(addr = image_addr_xds, name = name_tag)
    print(alltags_xds)
    print(allStripOffsets_xds)
    'Operating with image - numpy'
    accumulate_xds = image_matrix_xds + accumulate_xds #it is numpy
    
    'Now, it is time to write the new image'
    writeimage(addr=f_addr, matrix=accumulate_xds, tags=tag_xds, specialTag=allStripOffsets_xds)
    
    '''Print tags'''
    printtags(f_addr)
    
    print('Ok')
if __name__ == '__main__':
    'Input'
    PATH_xds = '/home/ABTLUS/rodrigo.guercio/Downloads/bittar/'
    filename_xds  = 'Ca00_phi1n_11K_5min_n026' + '.tiff'
    PATH_xrd1 = '/home/ABTLUS/rodrigo.guercio/Pictures/FileMarrcds/'
    filename_xrd1  = '_1_c_20s_4m_4c_n000.tiff'
    image_addr_xds = PATH_xds + filename_xds # This is a string (address of image)
    image_addr_xrd1 = PATH_xrd1 + filename_xrd1 # This is a string (address of image)
    ''' Output '''
    '''Define an address to new image'''
    pathFileAcclt_xds = PATH_xds + 'nameC' + '.tiff'
    pathFileAcclt_xrd1 = PATH_xrd1  + 'nameC' + '.tiff'
    ''' compare'''
    compare(i_addr=image_addr_xds, f_addr=pathFileAcclt_xds)
    compare(i_addr=image_addr_xrd1, f_addr=pathFileAcclt_xrd1)
    
   
    
  
    
   
    print("resolution=tag.tags['XResolution'].value")