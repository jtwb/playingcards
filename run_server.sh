docker run \
    --name playingcard0 \
    -d \
    -p 8888:8888 \
    -v /Users/jason/src/play/playingcard-collision/notebooks:/notebooks \
    -e "PASSWORD=mugwumpjismsyn2" \
    jtwb/playingcard-ipynb
