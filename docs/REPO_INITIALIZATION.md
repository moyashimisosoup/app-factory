# App Factory: 新アプリRepo初期化の標準手順

**非ローカル・Web優先。** 新Repo生成の次に実施する半自動の手順。初期ファイルを自動投入する権限をApp Factoryの作成専用PATに追加しない。

## 初期化前の必須確認

- 既存Repoと全体台帳を照合。作成元Issue、Repo owner/slug、申請可視性、作成Run、実在するRepoのdefault branchを確認する。
- 新Repoに書込み可能な**GitHub接続**を確認。書込み不可ならセットアップを止め、接続権限の調整を依頼する。
- Publicで作成しても、秘密情報・学校情報・セッション固有情報を含むファイルは追加しない。
- 採用アプリのWeb試作が適切か判断し、Web以外ならindex.htmlを無理に用意せず個別の設計を優先する。

## 最小Webスターター

テンプレート正本は [templates/web-minimal](../templates/web-minimal/)。パスと責務:

| 配置先 | 内容 |
| --- | --- |
| README.md | アプリ名、目的、試作の状態、動作方法 |
| AGENTS.md | このRepoでの開発・安全・引継ぎルール |
| index.html | 依存なしのレスポンシブ静的Web試作 |
| docs/ROADMAP.md | 構想から検証までの小さな段階表 |

- 各テンプレートのプレースホルダーを実案件の公開可能な値で置換。HTMLはエスケープする。
- 既存READMEがGitHubで自動生成されているので、**読戻しと差分確認後に更新**する。初期化により説明を失うことを避ける。
- その他のファイルは必要になるまで追加しない。CI、Pages、PRフロー、APIの導入はアプリごとに判断する。
- GitHub上で作成・更新し、コミットSHAとファイルの読戻しを確認する。未検証のブラウザ挙動を「動作確認済み」と書かない。

補助スクリプト: scripts/render_starter.py は4ファイルを**新しい出力フォルダ**へ安全に生成する任意のオフライン補助。生成先Repoへ書き込まない。既存フォルダは上書きしない。ChatGPTのGitHubツールで作業する場合はテンプレートを直接参照すればよく、ローカルPythonのセットアップは不要。

## Session Deck連携

1. [Session Deck 全体台帳](https://github.com/moyashimisosoup/session-deck/blob/main/docs/APP_PORTFOLIO.md)の最新を取得し、ID重複、既存Repo・名称重複、公開可能な情報を照合。
2. APP-IDは**台帳へ正式登録した時に確定**。仮番号を創作しない。試験用Repoなら新規APP-IDを付けず、App Factoryの検証記録にとどめる。
3. Publicな台帳にはPublic RepoのURL、またはPrivate案件の場合は非機密の一般的概要と確認結果だけを記載。Private RepoのURL、Issueの非公開内容や秘密情報は掲載しない。
4. 確認日/JST、現在の段階、完了証拠（コミット・Actions）、未実施、次の1操作を書込み、**GitHub読戻し**する。
5. 各アプリのREADME、AGENTS.md、詳細仕様はそのRepoで管理。Session Deckに同じ仕様を重複複製しない。

## 完了報告の区別

- [ ] 作成Run成功
- [ ] リポジトリ存在と可視性の再確認
- [ ] 初期ファイルのcommitと読戻し
- [ ] 台帳登録と読戻し（正式な採用アプリのみ）
- [ ] CI（導入した場合）
- [ ] Web公開（別の明示承認）
- [ ] ブラウザ／スマホ実機検証（別途）

すべてを同時に完了扱いしない。
