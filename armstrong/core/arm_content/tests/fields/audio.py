# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

from ..arm_content_support.models import AudioModel
from ..arm_content_support.models import AudioModelForm
from ..arm_content_support.models import SimpleProfile
from .._utils import *

from ...fields import AudioField
from ...widgets.audio import AudioFileWidget 

class AudioFieldMetadataTestCase(TestCase):
    def setUp(self):
        self.audiofile = load_audio_file(self.audio_metadata['filename'])
        
    def test_format_handling(self):
        """
        figure out which audio format a file is or return false

        """
        self.assertEqual(self.audiofile.format, self.audio_metadata['format'])

    def test_audiofield_default_widget(self):
        """
        test that the correct widget is displayed in 
        a model form 
        """
        form=AudioModelForm()
        self.assertEqual(form.audio_file.widget, AudioFileWidget)
   
    def test_audiofield_metadata(self):
        """
        confirm that the extracted metadata matches the expected values 
        """
        for key in self.audio_metadata.keys():
            self.assertEqual(self.audio_metadata[key], self.audiofile.metadata[key])


class Mp3Test(AudioFieldMetadataTestCase):
    """
    tests the audio fiels support for mp3's
    """
    audio_metadata=dict(
        filename = 'test.mp3',
        audio_format = 'mp3',
        artist='nodus',
        playtime='0:10')

