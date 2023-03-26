from flask import escape

def greetings_http(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'TomandJerry'
    return '<html><head></head>\
        <body style="background-color:#060C59;"><div style="height:100%;background-repeat:no-repeat;background-position:center;\
        background-image:url(https://raw.githubusercontent.com/vikramvlb/kcs-serverless-gcp/master/sitev1/serverless-qtree-1/img/tom-and-jerry.webp);">\
        <h1 style="padding-top:100px;font-size:48px;color:white;text-align:center;">Hello we are Qtree {}!</h1>\
        </div></body></html>'.format(escape(name))
