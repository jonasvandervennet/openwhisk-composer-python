__version__ = '0.1.0'

from .composer import Composer, ComposerError, parse_action_name

_composer = Composer()

def composition(name, task):
    return _composer.composition(name, task)

def seq(*arguments):
    return _composer.sequence(*arguments)

def sequence(*arguments):
    return _composer.sequence(*arguments)

def literal(value):
    return _composer.literal(value)

def action(name, action=None):
    return _composer.action(name, action)

def task(task):
    return _composer.task(task)

def function(value):
    return _composer.function(value)

def when(test, consequent, alternate=None):
    return _composer.when(test, consequent, alternate)

def when_nosave(test, consequent, alternate=None):
    return _composer.when_nosave(test, consequent, alternate)

def loop(test, body):
    return _composer.loop(test, body)

def loop_nosave(test, body):
    return _composer.loop_nosave(test, body)

def do(body, handler):
    return _composer._compose('try', (body, handler))

def doloop(body, test):
    return _composer.doloop(body, test)

def doloop_nosave(body, test):
    return _composer.doloop_nosave(body, test)

def ensure(body, finalizer):
    return _composer._compose('finally', (body, finalizer))

def let(declarations, *arguments):
    return _composer._compose('let', (declarations, *arguments))

def mask(*arguments):
    return _composer._compose('mask', arguments)

def retain(*arguments):
    return _composer._compose('retain', arguments)

def retain_catch(*arguments):
    return _composer.retain_catch(*arguments)

def repeat(count, *arguments):
    return _composer._compose('repeat', (count, *arguments))

def retry(count, *arguments):
    return _composer._compose('retry', (count, *arguments))

def openwhisk(options):
    return _composer.openwhisk(options)
