# anvarbek

___

# Pip

```
python3 -m venv venv
source ./venv/bin/activate

python -m pip install -U pip
pip install -r requirements.txt
```

___

# Systemd service [anvarbek.service]

```
[Unit]
Description=Systemd service daemon for anvarbek.cmo
Before=nginx.service
After=network.target

[Service]
User=major
Group=major
WorkingDirectory=/home/major/anvarbek
ExecStart=/home/major/anvarbek/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/major/anvarbek/gunicorn.sock ANVARBEK.wsgi:application
Restart=always
SyslogIdentifier=gunicorn

[Install]
WantedBy=multi-user.target
```

___

# Nginx [anvarbek]

```
server {
    listen 80;
    server_name anvarbek.com www.anvarbek.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static {
        alias /home/major/anvarbek/static;
    }
    
    location /media  {
        alias /home/major/anvarbek/media;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/major/anvarbek/gunicorn.sock;
    }
}
```