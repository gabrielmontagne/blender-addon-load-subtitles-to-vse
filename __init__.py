import bpy 
from bpy_extras.io_utils import ImportHelper 
from bpy.props import StringProperty, BoolProperty, EnumProperty 
from bpy.types import Operator 
from pprint import pprint
from . import loader 

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

class ImportSomeData(Operator, ImportHelper):
    bl_idname = 'import_test.some_data'
    bl_label = 'Import some data'
    filename_ext = '.srt'
    filter_glob = StringProperty( 
        default='*.srt', 
        options={'HIDDEN'}, 
        ) 
    def execute(self, context):
        print('execute')
        loader.load_srt(self.properties.filepath)
        pprint(self.properties.filepath)
        pprint(dir(self.properties))



        area = bpy.context.area
        old_type = area.type
        area.type = 'SEQUENCE_EDITOR'
        bpy.ops.sequencer.effect_strip_add(frame_start=1, frame_end=20, type='TEXT')
        bpy.context.scene.sequence_editor.active_strip.text = self.properties.filepath
        area.type = old_type
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(ImportSomeData)

    # from . import pysrt

    print('registered alegre broc')

def unregister():
    bpy.utils.unregister_class(ImportSomeData)
    print('un registered alegre brock')

if __name__ == '__main__':
    register()
