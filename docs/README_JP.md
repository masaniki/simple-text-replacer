# 概要

JSONファイルやYAMLファイルによる文字列置換機能を提供するCLI applicationです。

正規表現には対応していません。

# インストール方法

`pip install simple-text-replacer`

## パッケージ依存性

以下のpackageをインストールしないと正しく機能しない場合があります。

- [PyYAML](https://pypi.org/project/PyYAML/): 最も人気なPyhton用のYAMLパーサーです。


# 使用例

my_pet.txt:

```
I have one dog and one cat.
```

replacer.json:

```
{"dog":"wolf", "cat":"lion"}
```

```
> simrep replacer.json my_pet.txt
> cat my_pet.txt
I have one wolf and one lion.
```

## 構文

`simrep <replacer> <text_file>`

`replacer`はJSONもしくはYAML形式です。

`replacer`で指定するJSONもしくはYAMLは、`{置換前の単語: 置換後の単語}`というkey value systemで記述する必要があります。

`text_file`はdirectoryでも指定できますが、その場合はそのdirectoryの子孫要素のファイルを全て置き換えるので注意が必要です。

`text_file`の上書きを嫌う場合は、`-n`オプションで新規ファイルまたは新規directoryに出力することができます。


## Options

`[-h|--help]`

helpを表示する。

`[-v|--version]`

versionを表示する。

`[-n|--new]　<new file or new directory>`

置換後のテキストファイルを新規ファイルとして出力する。

## 詳細仕様

key-valueによる置換は上から順番に実行される。


