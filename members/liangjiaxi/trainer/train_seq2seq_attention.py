from allennlp.common import Params
from allennlp.common.util import import_submodules
# from members.liangjiaxi.mylibrary.modified.modified_import import import_submodules
from members.liangjiaxi.mylibrary.modified.modified_train import train_model
import shutil
import visdom

from allennlp.modules.text_field_embedders.basic_text_field_embedder import BasicTextFieldEmbedder
from allennlp.modules.token_embedders.embedding import Embedding
import warnings
warnings.filterwarnings('ignore')
#相对导入的技巧  https://blog.csdn.net/xie_0723/article/details/78004649
import_submodules('members.liangjiaxi.mylibrary')

params = Params.from_file('../experiment/decoder_baseline.json')

serialization_dir = '../../../tmp/model_weight/seq2seq_attn_model_4_12'

model = train_model(
                    params,
                    serialization_dir,
                    force=True,
                    )