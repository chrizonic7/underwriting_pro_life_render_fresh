FROM odoo:16

LABEL maintainer="ERPBridge Technologies"

USER root
RUN pip3 install --upgrade pip
USER odoo

COPY ./custom-addons /mnt/extra-addons

ENV ADDONS_PATH=/mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons

CMD ["odoo", "-c", "/etc/odoo/odoo.conf", "--dev=all"]