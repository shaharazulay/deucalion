from copy import deepcopy


def collector(f):

	def _record(r):
		print(r)

	def wrapper(*args, **kwargs):
		_input_args = dict([(f'pos__{idx}', deepcopy(v)) for idx, v in enumerate(args)])
		_input_kwargs = dict([(f'named__{k}', deepcopy(v)) for k, v in kwargs.items()])
		_input_args.update(_input_kwargs)

		output = f(*args, **kwargs)

		_metadata = {
			'f_name': f.__name__,
			'input': _input_args,
			'output': output
		}

		_record(_metadata)

		return output
	return wrapper
