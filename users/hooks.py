

def custom_preprocessing_hook(endpoints):
    filtered_endpoints = ["/users/activation/", "/users/reset_phone_no_confirm/","/users/resend_activation/", "/users/reset_phone_no/"]

    endpoints = [
        (path, path_regex, method, callback)
        for (path, path_regex, method, callback) in endpoints
        if path not in filtered_endpoints
    ]

    return endpoints
