#!/usr/local/bin/python3

import cairosvg
import sys
import os
import shutil
import json


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print( "usage: python3 svg2appicon.py <path-2-svg> [outpath]" )
        sys.exit(1)

    path_svg = sys.argv[1]
    outpath = '.'
    if len(sys.argv) >= 3:
        outpath = sys.argv[2]
    
    print( "convert {} to .appicon".format(path_svg) )

    fpath, fname = os.path.split( path_svg )
    fbasename, fext = os.path.splitext(fname)

    imageset_path = os.path.join( outpath, "AppIcon.appiconset"  )
    if os.path.exists( imageset_path ):
        shutil.rmtree( imageset_path )
    os.makedirs( imageset_path )

    # print(cairosvg.svg2png.__doc__)
    path_tpl_content = "template_Contents.json"
    if not os.path.exists( path_tpl_content ):
        # for docker
        path_tpl_content = os.path.join( "/opt/res", path_tpl_content )
    with open( path_tpl_content ) as fp:
        contentsInfo = json.load(fp)

    # print(contentsInfo)
    for imageinfo in contentsInfo["images"]:
        iconsize = float(imageinfo["size"].split('x')[0])
        scale = int(imageinfo["scale"].split('x')[0])
        actual_size = int(iconsize * scale)
        # {'idiom': 'iphone', 'size': '20x20', 'scale': '2x'}
        fname_icon = "icon_{idiom}_{size}_{scale}.png".format( **imageinfo )
        # add filename info
        imageinfo['filename'] = fname_icon
        # create icon
        path_png = os.path.join( imageset_path , fname_icon )
        cairosvg.svg2png(
            url=path_svg, write_to=path_png, output_width=actual_size )


    # create Contents.json
    with open( os.path.join(imageset_path, "Contents.json" ), "w") as fp:
        fp.write( json.dumps( contentsInfo, indent=4 ) ) 

    print('done')



