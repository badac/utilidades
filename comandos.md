# Utilidades para línea de comandos

## Reescalar imagen con ImageMagick conservar proporción

Reescalar imagenes en ImageMagick, conservando la proporción.

```
convert original.png -resize 100x100^ new.png

```

## Reescalar y optimizar

```
convert feldroy-512x512-unoptimized.jpg \
-sampling-factor 4:2:0 \
-strip \
-quality 85 \
-interlace Plane \
-gaussian-blur 0.05 \
-colorspace RGB \
-resize '1920x1920^ \
original.jpg 
```

## Reescalar y optimizar en lote


```
mogrify \
-sampling-factor 4:2:0 \
-strip \
-quality 85 \
-interlace Plane \
-gaussian-blur 0.05 \
-colorspace RGB \
-resize '1920x1920^' \
-format jpg \
*.tif
```

## Referencias

https://dev.to/feldroy/til-strategies-for-compressing-jpg-files-with-imagemagick-5fn9

https://www.digitalocean.com/community/tutorials/workflow-resizing-images-with-imagemagick

https://www.smashingmagazine.com/2015/06/efficient-image-resizing-with-imagemagick/
