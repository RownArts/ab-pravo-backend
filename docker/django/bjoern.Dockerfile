FROM python:3.8.3-alpine
COPY requirements.txt run.sh ./
RUN apk add --no-cache libwebp-dev mariadb-dev libev gcc libc-dev python3-dev libev-dev jpeg-dev zlib-dev libtiffxx freetype lcms2 libwebp tcl-dev openjpeg nginx; pip install --no-cache-dir -r requirements.txt; mkdir /run/nginx
EXPOSE 8000/tcp 80/tcp 443/tcp
ENTRYPOINT ["sh","./run.sh"]