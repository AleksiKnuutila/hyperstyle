from configs import transforms_config
from configs.paths_config import dataset_paths


DATASETS = {
	'streetview': {
		'transforms': transforms_config.EncodeTransforms,
		'train_source_root': dataset_paths['train_data'],
		'train_target_root': dataset_paths['train_data'],
		'test_source_root': dataset_paths['test_data'],
		'test_target_root': dataset_paths['test_data'],
	},
	'ffhq_hypernet_pre_extract': {
		'transforms': transforms_config.NoFlipTransforms,
		'train_source_root': dataset_paths['train_data'],
		'train_target_root': dataset_paths['train_data'],
		'train_latents_path': dataset_paths['train_latents'],
		'test_source_root': dataset_paths['test_data'],
		'test_target_root': dataset_paths['test_data'],
		'test_latents_path': dataset_paths['test_latents']
	},

}
