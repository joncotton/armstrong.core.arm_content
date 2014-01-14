from django import template
import fudge

from ..templatetags import content_helpers
from ._utils import ArmContentTestCase


class ThumbnailTestCase(ArmContentTestCase):
    def test_thumbnail_filter(self):
        thumb_url = "http://example.com/thumbnail_url.jpg"
        obj = {'image': "image"}
        t = template.Template("{% load content_helpers %}{{ obj.image|thumbnail:'thumb_size' }}")

        thumbnail_result = fudge.Fake()
        thumbnail_result.has_attr(url=thumb_url)

        get_preset_thumbnail = fudge.Fake()
        get_preset_thumbnail.expects_call().\
                with_args("image", u'thumb_size').\
                returns(thumbnail_result)
        with fudge.patcher.patched_context(content_helpers,
                    'get_preset_thumbnail',
                    get_preset_thumbnail):
            result = t.render(template.Context({'obj': obj}))
        self.assertEqual(result, thumb_url)
        fudge.verify()
