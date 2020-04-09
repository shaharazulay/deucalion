from copy import deepcopy
import logging
runtime_record = []

_logger = logging.getLogger()


def collector(f):
	def _record(r):
		runtime_record.append(r)
		_logger.debug(f"Recording {r}")

	def wrapper(*args, **kwargs):
		_input_args = dict([(f'pos__{idx}', deepcopy(v)) for idx, v in enumerate(args)])
		_input_kwargs = dict([(f'named__{k}', deepcopy(v)) for k, v in kwargs.items()])
		_input_args.update(_input_kwargs)

		_metadata = {
			'f_name': f.__name__,
			'input': deepcopy(_input_args),
			"original_args": deepcopy(args),
			"original_kwargs": deepcopy(kwargs)
		}
		_record(_metadata)

		output = f(*args, **kwargs)
		_metadata['output'] = deepcopy(output)
		return output
	return wrapper


def get_records():
	return deepcopy(runtime_record)
