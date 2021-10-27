class EngineNotStartedError(Exception):

    def __str__(self):
        return f'Engine not started!'
