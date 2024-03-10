# Pydanticに関して

型初心者の自分が、Pydanticに関して勉強してみたメモを記載します。

## 前提知識として知っておいた方が良いこと

Pythonの型ヒントは簡単でも良いので知っておきましょう。

参考にした記事:https://qiita.com/terapyon/items/bd34763f78f2cb6f0131

## Pydanticとは

Pythonで動的に型づけを行うためのライブラリです。
Pythonの型ヒントはあくまで型ヒント（後で見返した時などに変数の型が何かの注釈を加えたもの）であり、実際に型をチェックすることはできません
mypyで実施していることもあくまで静的な型ヒントであって、型ヒントで指定した型でない場合はエラーを出すことができますが、実際の処理の中で型をチェックすることはできません。
Pydanticを使うことで処理実施時に型をチェックする動的な型チェックができます。これによりデータベースの書き込みなどの処理に入る前にエラーを出力できます。

## Pydanticの基本的な使い方

[main.py](https://github.com/yo5678/pra-Pydantic/blob/main/src/src/main.py)に記載中。

## 参考

- https://docs.pydantic.dev/latest/concepts/models/
- https://qiita.com/koralle/items/93b094ddb6d3af917702