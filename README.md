# Dockerized Environment for deploying Django Projects

### Have you ever struggled with setting up a new environment for publishing your Django projects to the web? Do you want a Docker solution that you can use across projects? Look no more, this repo is a template that will get you started immediately! 


__Features :__

- An extensible template, that can be used for any kind of Django framework (including Django Rest Framework)
- Serve static files with Nginx, the way it's supposed to be served!
- A seamless connection between Nginx and UWSGI. 

__Steps :__

1. Copy repository, and look at settings. 
2. Set up ENV in docker/RUN_SECRETS.env.
- Alternatively, if you are using Github Actions or Secrets - write the variables to this file. 
3. Change the server name based on your requirement in docker/nginx.conf

If you need any help with setting it up, or you need any new features - feel free to create an issue/shoot me an email! 


