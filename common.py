def success_responce(data = None, message = 'Success', code = 200)->dict:
    return {
        'success' : True,
        'message' : message,
        'code' : code,
        'data' : data 
    }


def error_responce(message = 'An error occured', code = 400, erros = None)->dict:
    return {
        'success' : False,
        'message' : message,
        'code' : code,
        'errors' : erros
    }