import json


def _execute_alert(window, function_name, *args):
    return window.evaluate_js(f'Alert.{function_name}({json.dumps(args)[1:-1]})')


def success(
    window,
    message,
    title='Sucesso',
):
    return _execute_alert(
        window,
        'success',
        message,
        title,
    )


def info(
    window,
    message,
    title='Info',
):
    return _execute_alert(
        window,
        'info',
        message,
        title,
    )


def error(
    window,
    message,
    title='Erro',
):
    return _execute_alert(
        window,
        'error',
        message,
        title,
    )


def warning(
    window,
    message,
    title='Aviso',
):
    return _execute_alert(
        window,
        'warning',
        message,
        title,
    )
