from converter import Converter
import sys

# Get the arguments
def get_param():
   cmdargs = sys.argv
   return cmdargs[1]




def convert():
   file = get_param()
   c = Converter()
   info = c.probe(file)

   conv = c.convert(file, '/tmp/output.mkv', {
        'format': 'mkv',
        'audio': {
            'codec': 'mp3',
            'samplerate': 11025,
            'channels': 2
        },
        'video': {
            'codec': 'h264',
            'width': 720,
            'height': 400,
            'fps': 15
        }})

   for timecode in conv:
      print("Converting (%f) ...\r" % timecode)
convert()
