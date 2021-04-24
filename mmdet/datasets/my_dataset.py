from .coco import CocoDataset
from .registry import DATASETS
from .xml_style import XMLDataset
from .voc import VOCDataset
@DATASETS.register_module
class MyDataset(XMLDataset):

    #CLASSES =('Dent', 'Scratch_or_spot')#, 'Shatter', 'Tear')
    CLASSES = ('abyssinian',
 'american_bulldog',
 'american_pit_bull_terrier',
 'basset',
 'beagle',
 'bengal',
 'birman',
 'bombay',
 'boxer',
 'british_shorthair',
 'chihuahua',
 'egyptian',
 'english_cocker',
 'english_setter',
 'german_shorthaired',
 'great_pyrenees',
 'havanese',
 'japanese_chin',
 'keeshond',
 'leonberger',
 'maine_coon',
 'miniature_pinscher',
 'newfoundland',
 'persian',
 'pomeranian',
 'pug',
 'ragdoll',
 'russian_blue',
 'saint_bernard',
 'samoyed',
 'scottish_terrier',
 'shiba_inu',
 'siamese',
 'sphynx',
 'staffordshire',
 'wheaten_terrier',
 'yorkshire_terrier')