# NEWSUZ

## Installing

### Step 1: Install Nginx First, you'll need to install Nginx if it isn't already installed on your server.

`sudo apt update `

`sudo apt install nginx`

### Step 2: Configure Nginx for Your Flask Application
1. Create a New Nginx Server Block:
Create a new Nginx configuration file for your Flask project. This file will define how Nginx serves your application.

`sudo nano /etc/nginx/sites-available/ainews.conf`

2. Add the Nginx Configuration: 
In the new file, add the following configuration. This example assumes your Flask app is served by Gunicorn and listens on port 5000, as set up earlier.
    
    
    server {
    
        listen 80;
        server_name ainews.uz www.ainews.uz;
    
        location / {
            proxy_pass http://127.0.0.1:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    
        location /static {
            alias /var/www/another-projects/newsuz/static;
        }
    
        location /media {
            alias /var/www/another-projects/newsuz/media;
        }
    
        error_page 404 /404.html;
        location = /404.html {
            internal;
        }
    
        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
            internal;
        }
    }


* server_name: Replace ainews.uz with your actual domain name.
* proxy_pass: Directs traffic to the Gunicorn server running your Flask app.
* location /static and location /media: These directives tell Nginx where to find static and media files, if your app uses them.

3. Enable the Configuration: 
Create a symbolic link from this file to the sites-enabled directory to enable the configuration.

`sudo ln -s /etc/nginx/sites-available/ainews.uz /etc/nginx/sites-enabled/
`

4. Test the Nginx Configuration: 
Before restarting Nginx, test the configuration to make sure there are no syntax errors.

`sudo nginx -t`

5. Restart Nginx: 
Apply the new configuration by restarting Nginx.

`sudo systemctl restart nginx`

### Step 3: Update DNS Settings
Ensure that your domain ainews.uz points to your server's IP address. You can do this by updating the A record in your domain registrar’s DNS settings.

* A Record: Set the A record for ainews.uz and www.ainews.uz to point to your server's public IP address.

### Step 4: Install and Configure SSL (Optional but Recommended)
For security, it’s highly recommended to use SSL. You can use Let’s Encrypt to get a free SSL certificate.


