from pathlib import Path
import utils


def abs_path(relative_path: str):
    return str(Path(utils.__file__).parent.joinpath(relative_path).absolute())
