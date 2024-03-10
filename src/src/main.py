from pydantic import BaseModel, ValidationError
from pydantic_settings import BaseSettings  # pip install pydantic-settingsが必要
import os

"""基本の使い方
参考:

BaseModelを継承したクラスで型の定義→クラスを呼び出す際に引数で値を指定.
user.model_dump()でdictに定義したものを出力可能である。
型を間違ったものを指定した場合、ValidationErrorが出力される（User(id="123")の場合はエラーが出力されないため、別途設定が必要）。
"""


class User(BaseModel):
    id: int
    name: str = "Jane Doe"  # デフォルト値を指定


user = User(id=123)
print(user)  # output)id=123 name='Jane Doe'
print(user.id)  # output) 123

print(user.model_dump())  # output) {'id': 123, 'name': 'Jane Doe'}
print(type(user.model_dump()))  # output) <class 'dict'>

# incorrect_user = User(id="test")
"""
Output)
pydantic_core._pydantic_core.ValidationError: 1 validation error for User id
Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='test', input_type=str]
"""

"""Note
[可変長引数](https://note.nkmk.me/python-args-kwargs-usage/)を使用しての指定もよく用いられる.

"""


class User2(BaseModel):
    id: int
    name: str
    age: int


item = {"id": 123, "name": "test", "age": 50}

user2 = User2(**item)


""" 環境変数の読み込み方法
参考:https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values
"""


os.environ["v0"] = "test"
os.environ["v1"] = "test2"


class EnvVar(BaseSettings):
    v0: str
    v1: str


try:
    env = EnvVar()
    print(env.v0)  # output) test
except ValidationError as e:
    print(e)
