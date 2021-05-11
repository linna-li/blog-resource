FROM ubuntu:20.04
RUN apt-get update 
RUN apt-get -y install wget 
RUN mkdir download 
RUN cd download
RUN wget https://github.com/prometheus/prometheus/releases/download/v2.26.0/prometheus-2.26.0.linux-amd64.tar.gz 
RUN tar xvf prometheus-2.26.0.linux-amd64.tar.gz
RUN cp prometheus-2.26.0.linux-amd64/prometheus /usr/local/bin/
RUN cp prometheus-2.26.0.linux-amd64/promtool /usr/local/bin/
RUN chown root:root /usr/local/bin/prometheus
RUN chown root:root /usr/local/bin/promtool
RUN mkdir /etc/prometheus
RUN cp -r prometheus-2.26.0.linux-amd64/consoles /etc/prometheus/
RUN cp -r prometheus-2.26.0.linux-amd64/console_libraries /etc/prometheus/
RUN chown -R root:root /etc/prometheus/consoles
RUN chown -R root:root /etc/prometheus/console_libraries

COPY prometheus.yml /etc/prometheus/
ENTRYPOINT [ "/usr/local/bin/prometheus" ]

