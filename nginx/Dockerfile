# ----------------------------------------------------------------------------------------------------------------------
# Static collectiong
# ----------------------------------------------------------------------------------------------------------------------
FROM algol2302/options-and-pushes AS collection-static
CMD /bin/bash -c "python ./manage.py collectstatic --noinput"


# ----------------------------------------------------------------------------------------------------------------------
# Prepare nginx
# ----------------------------------------------------------------------------------------------------------------------
FROM nginx:1.19-alpine
COPY ./conf/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=collection-static /app/static_files /var/www/static
EXPOSE 80
