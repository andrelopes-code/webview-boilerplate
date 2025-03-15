import json


def _execute(window, function_name, *args):
    args_str = json.dumps(args)[1:-1]
    result = window.evaluate_js(f'Alert.{function_name}({args_str})')
    return result


def success(
    window,
    message,
    title='Sucesso',
):
    return _execute(
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
    return _execute(
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
    return _execute(
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
    return _execute(
        window,
        'warning',
        message,
        title,
    )
