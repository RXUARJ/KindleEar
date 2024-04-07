# gunicorn.conf.py
pythonpath = "/home/ubuntu/.local/lib/python3.10/site-packages"
bind = "127.0.0.1:8000"
workers = 1
threads = 3
accesslog = "/var/log/gunicorn/error.log"
errorlog = "/var/log/gunicorn/access.log"
capture_output = True
enable_stdio_inheritance = True
loglevel = "info"
#preload_app = True
#certfile = 'cert.pem'
#keyfile = 'key.pem'