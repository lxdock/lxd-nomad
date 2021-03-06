class LXDockException(Exception):
    def __init__(self, msg=None):
        self.msg = msg


class ProjectError(LXDockException):
    """ An error occurred while executing some action at the project level. """


class ContainerOperationFailed(LXDockException):
    """ An operation on a specific container failed. """


class ProvisionFailed(LXDockException):
    """ A provisioning failed. """
