import pkg_resources
pkg_resources.declare_namespace(__name__)

from armstrong.utils.backends import GenericBackend

from .youtube import YouTubeBackend
from .vimeo import VimeoBackend


backend = GenericBackend("ARMSTRONG_EXTERNAL_VIDEO_BACKEND")
get_backend = backend.get_backend
