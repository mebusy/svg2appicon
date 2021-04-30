# svg2appicon

python3 script to convert SVG to iOS AppIcon.appiconset

## Requirement

1. python3.6+
2. [CairoSVG](https://cairosvg.org/documentation/)
    ```bash
    pip3 install cairosvg --user
    ```

## Usage

```bash
usage: python3 svg2appicon.py <path-2-svg> [outpath]

@ outpath:  `.` by default
```

Example:

```bash
$ python3 ./svg2appicon.py test_arrow_circle_down.svg
```

I will generate such files...

```bash
AppIcon.appiconset
├── Contents.json
├── icon_ios-marketing_1024x1024_1x.png
├── icon_ipad_20x20_1x.png
├── icon_ipad_20x20_2x.png
├── icon_ipad_29x29_1x.png
├── icon_ipad_29x29_2x.png
├── icon_ipad_40x40_1x.png
├── icon_ipad_40x40_2x.png
├── icon_ipad_76x76_1x.png
├── icon_ipad_76x76_2x.png
├── icon_ipad_83.5x83.5_2x.png
├── icon_iphone_20x20_2x.png
├── icon_iphone_20x20_3x.png
├── icon_iphone_29x29_2x.png
├── icon_iphone_29x29_3x.png
├── icon_iphone_40x40_2x.png
├── icon_iphone_40x40_3x.png
├── icon_iphone_60x60_2x.png
└── icon_iphone_60x60_3x.png
```


## Docker 

Or just using the prebuilt docker image 

```bash
$ docker run --rm -v `pwd`:/opt/svg2appicon/ mebusy/svg2appicon  test_arrow_circle_down.svg
```




