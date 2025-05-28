import time


class Logger:
    LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

    def __init__(self, name='Samaia', level='INFO'):
        self.name = name
        self.level = level

    def _should_log(self, level):
        return self.LEVELS.index(level) >= self.LEVELS.index(self.level)

    def _format(self, level, msg):
        ts = time.ticks_ms()  # millisecond uptime
        return f"[{ts}ms][{self.name}][{level}] {msg}"

    def debug(self, msg):
        if self._should_log('DEBUG'):
            print(self._format('DEBUG', msg))

    def info(self, msg):
        if self._should_log('INFO'):
            print(self._format('INFO', msg))

    def warning(self, msg):
        if self._should_log('WARNING'):
            print(self._format('WARNING', msg))

    def error(self, msg):
        if self._should_log('ERROR'):
            print(self._format('ERROR', msg))
