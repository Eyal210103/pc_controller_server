from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Union, List


@dataclass_json
@dataclass
class Result:
    result_data: Union[str, int, List[Union[str, int]]]
