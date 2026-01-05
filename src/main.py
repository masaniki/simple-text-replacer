import sys
from pathlib import Path
import argparse
import yaml
import json

VERSION="v0.1.0"

def mainCLI():
    """
    @Summ: CLIを処理する関数。
    """
    parser=argparse.ArgumentParser(prog="PROG")
    parser.add_argument("-v","--version", action="version", version=f"simple-text-replacer {VERSION}")
    parser.add_argument("replacer", type=str, default=None, help="Put in YAML file or JSON file that contains replace information.")
    parser.add_argument("textFile", type=str, default=None, help="Put in text file name or directory name.")
    parser.add_argument("-n","--new", default=None, help="Put in text file name or directory name.")
    args=parser.parse_args()
    replacerPath=Path(args.replacer)
    textPath=Path(args.textFile)
    #replacerのfileを開く。
    if(replacerPath.suffix==".json"):
        with open(replacerPath,mode="r",encoding="utf-8") as f:
            replacerDict=json.load(f)
    elif(replacerPath.suffix==".yaml" or replacerPath.suffix==".yml"):
        with open(replacerPath,mode="r",encoding="utf-8") as f:
            replacerDict=yaml.safe_load(f)
    else:
        raise ValueError(f'{args.replacer} should be JSON or YAML file.')
    # text fileを開く。
    directoryDFS(textPath,replacerDict,args.new)


def directoryDFS(startPath:Path,replacer:dict,newFile:str=None):
    """
    @Summ: directory構造を深さ優先探索する関数。

    @Desc: 再帰的に呼び出される。

    @Args:
      startDir:
        @Summ: 探索を開始するdirectory名。
        @Type: Path.
      replacer:
        @Summ: 置換用の文字列。
        @Desc: {置換前の文字列(str):置換後の文字列(str)}
        @Type: dict
      newFile:
        @Summ: 新規fileの名前。上書きの時はNoneにする。
        @Type: str|None
    """
    if(startPath.is_file()):
        with open(startPath,mode="r",encoding="utf-8") as f:
            text=f.read()
        for key in replacer.keys():
          value=replacer[key]
          text=text.replace(key,value)
        if(newFile):
            outputPath=newFile
        else:
            outputPath=startPath
        with open(outputPath,mode="w",encoding="utf-8") as f:
            f.write(text)
    else:
        for childPath in startPath.iterdir():
            directoryDFS(childPath,replacer)


if(__name__=="__main__"):
    mainCLI()