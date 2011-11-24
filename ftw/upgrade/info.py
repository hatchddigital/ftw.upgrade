from ftw.upgrade.interfaces import IUpgradeManager
from zope.interface import implements


class UpgradeInfo(object):
    """Provides information about an upgrade.
    """

    implements(IUpgradeManager)

    def __init__(self, upgrade_class):
        """Initializes a upgrade information object for the passed upgrade
        class.

        Arguments:
        `upgrade_class` -- the upgrade class.
        """
        self._upgrade_class = upgrade_class

    def get_title(self):
        """Returns the title, which is the dotted name of the class.
        """
        return self._title

    def get_description(self):
        """Returns the description, which is the docstring of the upgrade
        class.
        """
        return self._description

    def is_installed(self):
        """Returns `True` if the upgrade is already installed.
        """
        return self._installed

    def get_class(self):
        """Returns the class of the upgrade.
        """
        return self._upgrade_class