# soukai-issue-creator

イシュートラッカー向け総会文書の Issue 作成ツール

## 準備

1. 依存ソフトウェアをインストール
   - **Python** - Poetry が要求しているバージョン
   - **Poetry** - インストール方法は [Poetry 公式ドキュメント](https://python-poetry.org/docs/) を参照
1. このリポジトリを clone
1. `poetry install` で依存 Python パッケージをインストール
1. `.env.sample` を書き換えて `.env` というファイル名で保存
   - `ACCESS_TOKEN` GitHub 個人アクセストークン
     - [個人アクセストークンを使用する \- GitHub Docs](https://docs.github.com/ja/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) を参照
     - **repo** 権限を付与すること
     - この個人アクセストークンを使うと第三者がリポジトリを操作することが可能なため、扱いに気をつける
       - 自分以外の人に見せないようにする
       - 実行が終わったら revoke (削除) する
   - `REPO` リポジトリ名
   - `TAG_NAME` リリースのタグ名 (パーマリンクを取得するために必要)
1. 以下の Issue に必要な情報を `issues.csv` ファイルに追記する
   - `PAGE` - ページ数
   - `SECTION` - 章名
   - `MODIFICATION` - 編集内容 (「誤字」、「脱字」、「内容」、「LaTeX」、「表記」) など
   - `AUTHOR` - 文責 GitHub アカウント
   - `BEFORE` - 修正前の文言
   - `AFTER` - 修正後の文言
   - `URL` - ソースコードの URL

## 実行

```sh
poetry run python src/soukai-issue-creator.py
```

## 開発

### フォーマット

```
poetry run black src
```

### Lint

```
poetry run flake8 src
```

### 型チェック

```
poetry run mypy src
```
