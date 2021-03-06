import logging
from abc import (
    ABCMeta,
    abstractmethod,
    abstractproperty,
)
import six
from ..utils import get_plugins


__all__ = get_plugins(plugin_dir=__file__.rsplit('/', 1)[0])


logger = logging.getLogger(__name__)
SOURCES = {}


class ArtifactSourceMeta(ABCMeta):
    def __init__(cls, name, bases, attrs):
        ABCMeta.__init__(cls, name, bases, attrs)
        # Don't register this base class
        if name != 'ArtifactSource':
            SOURCES[name] = cls


@six.add_metaclass(ArtifactSourceMeta)
class ArtifactSource(object):
    def __init__(self, config, stores):
        self.config = config
        self.stores = stores

    @abstractproperty
    def DEFAULT_CONFIG(self):
        """
        Default configuration values for that store
        """
        pass

    @abstractproperty
    def CONFIG_SECTION(self):
        """
        Configuration section name for this store
        """
        pass

    @abstractmethod
    def expand(self, source_str):
        """
        Gets a source string and expands it to it's elements.
        """
        pass

    @abstractmethod
    def formats_list(self):
        """
        Returns a list of the supported string formats, used for documentation
        """
        pass


# Force the load of all the plugins
from . import *  # noqa
