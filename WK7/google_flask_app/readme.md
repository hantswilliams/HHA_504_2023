## Setting up API for Signin:

Link: https://console.cloud.google.com/apis/credentials

## Setting up API for Signin:
- First need to create a project (you should have one already)
- Then need to create a generic oauth consent screen
    - call it whatever you want
    - need to have support email
    - can add in a logo or photo if you want
    - authorized domains: 
        - `cloudshell.dev`
- Then can go into credentials -> create credentials 
    - should create - 'oAuth client' --> 'for Web Server/Application'
    - add javascript origins: 
        - `https://5000-cs-213132341638-default.cs-us-east1-pkhd.cloudshell.dev`
    - add redirect URIs: 
        - need to make sure that the redirect has `/google/auth/` to match the route in the app.py file
        - be sure to include the final `/` in there
        - `https://[yousertroutegeneratedhere].cloudshell.dev/google/auth/`