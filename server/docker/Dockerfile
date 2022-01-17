# FROM nginx:stable

# COPY nginx.conf /etc/nginx/sites-available/nginx.conf
# COPY uwsgi_params /etc/nginx/uwsgi_params
# RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled

FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY uwsgi_params /etc/nginx/uwsgi_params

RUN ls /etc/nginx &&\
    cat /etc/nginx/nginx.conf &&\
    cat /etc/nginx/uwsgi_params

CMD ["/bin/bash"]