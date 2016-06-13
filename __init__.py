from bpy.props import StringProperty
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper
import bpy
import os
import sys

bl_info = {
    'name': 'Link Text to VSE Text Strip',
    'author': 'gabriel@tibas.london',
    'version': (0, 0, 2),
    'blender': (2, 77, 0),
    'location': 'VSE',
    'description': 'Adds a "import subtitle file into vse" operator',
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
        scene = bpy.context.scene
        fps = scene.render.fps

        sys.path.append(os.path.dirname(__file__))
        from .pysrt import open as srtopen

        area = bpy.context.area
        old_type = area.type
        area.type = 'SEQUENCE_EDITOR'

        subtitles = srtopen(self.properties.filepath)

        for subtitle in subtitles:
            frame_start = round(subtitle.start.ordinal * fps / 1000)
            frame_end = round(subtitle.end.ordinal * fps / 1000)
            bpy.ops.sequencer.effect_strip_add(frame_start=frame_start,
                                               frame_end=frame_end, type='TEXT')
            scene.sequence_editor.active_strip.text = subtitle.text

        area.type = old_type
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ImportSubtitleFile)


def unregister():
    bpy.utils.unregister_class(ImportSubtitleFile)

if __name__ == '__main__':
    register()
