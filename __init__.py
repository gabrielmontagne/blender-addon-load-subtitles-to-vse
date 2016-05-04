from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper
from pprint import pprint
import bpy
import os
import sys

bl_info = {
    'name': 'alegre brock',
    'author': 'gabriel@tibas.london',
    'version': (0,0,1),
    'blender': (2, 77, 0),
    'location': 'VSE',
    'description': 'aquel broc alegre',
    'wiki_url': 'http://www.tibas.london',
    'tracker_url': '',
    'category': 'Sequencer'
    }

class ImportSubtitleFile(Operator, ImportHelper):
    bl_idname = 'import_test.subtitle_file'
    bl_label = 'Import subtitle file into the Sequence Editor'
    filename_ext = '.srt'
    filter_glob = StringProperty(
        default='*.srt',
        options={'HIDDEN'},
        )

    def execute(self, context):
        sys.path.append(os.path.dirname(__file__))
        from .pysrt import open as srtopen
        subtitles = srtopen(self.properties.filepath)

        print('-' * 20)
        pprint(subtitles)

        area = bpy.context.area
        old_type = area.type
        area.type = 'SEQUENCE_EDITOR'
        bpy.ops.sequencer.effect_strip_add(frame_start=1, frame_end=20, type='TEXT')
        bpy.context.scene.sequence_editor.active_strip.text = self.properties.filepath
        area.type = old_type
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ImportSubtitleFile)

def unregister():
    bpy.utils.unregister_class(ImportSubtitleFile)

if __name__ == '__main__':
    register()
