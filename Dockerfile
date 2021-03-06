FROM ubuntu:16.04
LABEL MAINTAINER=ElasticRun

USER root
# Generate locale C.UTF-8 for mariadb and general locale dataopenjpeg
ENV LANG C.UTF-8

# Install all pre-requisites
# Add Node JS PPA.
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common dirmngr curl sudo wget apt-utils \
  && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8 \
  && add-apt-repository 'deb [arch=amd64] https://mirrors.ukfast.co.uk/sites/mariadb/repo/10.3/ubuntu xenial main' \
  && wget -qO - https://packages.confluent.io/deb/5.3/archive.key | sudo apt-key add - \
  && add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/5.3 stable main" \
  && add-apt-repository "deb https://nginx.org/packages/ubuntu/ xenial nginx" \
  && curl -fsSL https://nginx.org/keys/nginx_signing.key | sudo apt-key add - \
  && apt-get update && apt-get -y install --no-install-recommends libssl-dev fonts-indic libssl-dev virtualenv \
    libjpeg-dev zlib1g-dev libxml2-dev libxslt-dev libfontconfig1 libxrender1 lib32z1-dev nodejs \
    supervisor nginx git libblas3 liblapack3 liblapack-dev libblas-dev gfortran build-essential checkinstall \
    libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev \
    mariadb-client lzma-dev liblzma-dev \
  && wget -O /tmp/Python-3.7.5.tgz https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz \
  && cd /tmp && tar xzf Python-3.7.5.tgz && cd Python-3.7.5 \
  && ./configure --enable-optimizations && sudo make altinstall \
  && npm install -g yarn \
  && pip3.7 install setuptools pip --upgrade --force-reinstall \
  && ln -s `which python3.7` /usr/local/bin/python \
  && git clone --branch v1.2.2 https://github.com/edenhill/librdkafka.git && cd librdkafka \
  && ./configure --prefix /usr && make && make install \
  && apt-get install -y --no-install-recommends fontconfig xfonts-75dpi xfonts-base xtail jq \
  && wget -O /tmp/wkhtmltox_0.12.5-1.xenial_amd64.deb https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.xenial_amd64.deb \
  && dpkg -i /tmp/wkhtmltox_0.12.5-1.xenial_amd64.deb && apt --fix-broken install && rm -f /tmp/wkhtmltox_0.12.5-1.xenial_amd64.deb \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/*

ARG BENCH_AUTH_USER
ARG BENCH_AUTH_PASSWORD
ARG BENCH_BRANCH
ARG FRAPPE_AUTH_USER
ARG FRAPPE_AUTH_PASSWORD
ARG FRAPPE_BRANCH=master
ARG GIT_BENCH_URL=github.com/frappe/bench.git
ARG GIT_FRAPPE_URL=github.com/frappe/frappe.git
ARG KAFKA_CONFIG='{}'
ENV KAFKA_CONFIG=${KAFKA_CONFIG}

ENV BENCH_URL=git+https://${BENCH_AUTH_USER}${BENCH_AUTH_PASSWORD:+:}${BENCH_AUTH_PASSWORD}${BENCH_AUTH_USER:+@}${GIT_BENCH_URL}@${BENCH_BRANCH}
ENV FRAPPE_URL=https://${FRAPPE_AUTH_USER}${FRAPPE_AUTH_PASSWORD:+:}${FRAPPE_AUTH_PASSWORD}${FRAPPE_AUTH_USER:+@}${GIT_FRAPPE_URL}

ENV DB_HOST=mariadb
ENV BENCH_NAME=docker-bench

# OS User Setup
RUN addgroup --system --gid 1001 frappe && adduser --system --uid 1001 --ingroup frappe frappe  \
  && printf '# User rules for frappe\nfrappe ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
  && pip install -U pip-tools && pip install ${BENCH_URL}

# Create bench instance + cleanup
USER frappe
RUN sudo chown -R frappe:frappe /home/frappe && cd /home/frappe \
  && bench init ${BENCH_NAME} --ignore-exist \
      --skip-redis-config-generation --no-procfile --no-backups --frappe-branch ${FRAPPE_BRANCH:-master} \
      --verbose --frappe-path ${FRAPPE_URL} --python /usr/local/bin/python && cd /home/frappe/${BENCH_NAME} \
  && ./env/bin/pip install --upgrade werkzeug==0.16 && ./env/bin/pip install gevent watchgod \
  && mkdir -p /home/frappe/${BENCH_NAME}/entrypoints && chown -R frappe:frappe /home/frappe/${BENCH_NAME}/config \
  && mkdir -p /home/frappe/${BENCH_NAME}/config/env && rm -r /home/frappe/.cache \
  && sudo rm -rf /tmp/* && sudo rm -r /root/.cache \
  && rm -rf /home/frappe/${BENCH_NAME}/apps/frappe/.git* \
  && npm cache clean --force && sudo rm -rf /tmp/pip-install* \
  && rm -rf /home/frappe/${BENCH_NAME}/env/src/pdfkit/.git

USER root
COPY --chown=frappe:frappe ./common_site_config_docker.json /home/frappe/docker-bench/common_site_config_docker.json
COPY --chown=frappe:frappe ./entrypoints/*.sh /home/frappe/${BENCH_NAME}/entrypoints/
COPY --chown=frappe:frappe ./boot_scripts/*.sh /home/frappe/${BENCH_NAME}/boot_scripts/
COPY --chown=frappe:frappe ./postboot_scripts/*.sh /home/frappe/${BENCH_NAME}/postboot_scripts/
COPY --chown=frappe:frappe ./entrypoint.sh /home/frappe/${BENCH_NAME}/entrypoint.sh
COPY --chown=frappe:frappe ./error.sh /home/frappe/${BENCH_NAME}/error.sh
COPY --chown=frappe:frappe ./start-nginx.sh /home/frappe/${BENCH_NAME}/start-nginx.sh
COPY --chown=frappe:frappe ./start-web.sh /home/frappe/${BENCH_NAME}/start-web.sh
COPY --chown=frappe:frappe ./start-kafka-worker.sh /home/frappe/${BENCH_NAME}/start-kafka-worker.sh
COPY --chown=frappe:frappe ./run.sh /home/frappe/${BENCH_NAME}/run.sh
COPY --chown=frappe:frappe ./migrate.sh /home/frappe/${BENCH_NAME}/migrate.sh
COPY --chown=frappe:frappe ./checkjobhealth.sh /home/frappe/${BENCH_NAME}/checkjobhealth.sh
COPY --chown=frappe:frappe ./setenv.sh /home/frappe/${BENCH_NAME}/setenv.sh
COPY --chown=frappe:frappe ./bench.default.env /home/frappe/${BENCH_NAME}/bench.default.env
COPY --chown=frappe:frappe ./supervisord.conf /etc/supervisord.conf
COPY --chown=frappe:frappe ./supervisor-docker.conf /home/frappe/${BENCH_NAME}/config/supervisor.conf
COPY --chown=frappe:frappe ./nginx-docker.conf /home/frappe/${BENCH_NAME}/config/nginx.conf
COPY --chown=frappe:frappe ./nginx-startup.conf /home/frappe/${BENCH_NAME}/config/nginx-startup.conf
COPY --chown=frappe:frappe ./site_config_docker.json /home/frappe/${BENCH_NAME}/site_config_docker.json
# Files setup
RUN chmod u+x /home/frappe/${BENCH_NAME}/entrypoints/*.sh \
  && chmod u+x /home/frappe/${BENCH_NAME}/*.sh \
  && chmod u+x /home/frappe/${BENCH_NAME}/bench.default.env \
  && chmod u+x /home/frappe/${BENCH_NAME}/boot_scripts/*.sh \
  && chmod u+x /home/frappe/${BENCH_NAME}/postboot_scripts/*.sh \
  && ln -s /home/frappe/${BENCH_NAME}/config/nginx.conf /etc/nginx/conf.d/nginx.conf && mkdir -p /run/nginx \
  && mkdir -p /etc/supervisor.d && mkdir -p /var/run && mkdir -p /var/log/supervisor \
  && ln -s /home/frappe/${BENCH_NAME}/config/supervisor.conf /etc/supervisor.d/frappe.conf
  

# Uncomment next 2 lines if you want all child images to mandatorily provide an entrypoint script 
# under entrypoints directory
#ONBUILD COPY --chown=frappe:frappe ./entrypoints/*.sh /home/frappe/${BENCH_NAME}/entrypoints/
#ONBUILD RUN sudo chmod u+x /home/frappe/${BENCH_NAME}/*.sh && sudo chmod u+x /home/frappe/${BENCH_NAME}/entrypoints/*.sh

# Execute Startup script
USER frappe
WORKDIR /home/frappe/${BENCH_NAME}
CMD [ "/bin/sh", "-c", "./entrypoint.sh" ]
