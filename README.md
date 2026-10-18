# App Factory

**「新アプリ案」→採用→GitHubリポジトリ作成**の受付・自動化基盤です。標準Private、明示的に承認されたPublic申請にも対応します。

> **重要:** ここは公開リポジトリです。Issueのタイトル、本文、コメント、Actionsログは誰でも閲覧できます。非公開のアイデア、学校関係の情報、個人情報、アクセストークン、会話URLなどは**絶対に入力しないでください**。公開できない申請は、このIssueを使わずに非公開チャット内で検討してください。

## 初回本番疎通の結果（2026-10-17 JST）

**GitHub Actions経由でPrivateリポジトリ1件の生成に成功。** [承認済みIssue #4](https://github.com/moyashimisosoup/app-factory/issues/4) → [Actions実行 #39026244548：success](https://github.com/moyashimisosoup/app-factory/actions/runs/39026244548) → 認証されたGitHub接続から作成先の**実在・Visibility Private・main/README**を確認。公開Issueには作成先PrivateリポジトリのURLを投稿していない。

作成専用Secretが**この実行で使用できたこと**は検証済み。ただしGitHub Actions Secretの値・期限・設定画面は取得していない。異なる申請や改変後の再承認に対する本番多重実行は未検証で、衝突・冪等性はユニットテストで確認した段階。初期ファイル自動配置、APP-ID登録、Pages公開は未自動化。作成テストを目的なく繰り返さない。

## Public作成の追加条件

Public作成は既存のPrivate作成とは異なる明示オプトインです。公開IssueのJSONに `schema_version: 3`、`visibility: public`、`public_repo_ack: true` を記載し、本人が対象Issueと公開設定を確認した後に承認ラベルを付けてください。Privateのv2申請を自動的にPublicへ変更することはありません。GitHub Pagesによるアプリ公開は別工程です。

## 今できること

- GitHub Issueに、**公開して問題ない**アプリ名・短い説明・リポジトリ名を登録する。
- ユーザーがアプリを採用し、GitHub所有者が`factory-approved`ラベルを付けた場合だけ、GitHub Actionsから新規Repoを作成する。
- 標準は**Private**。Publicは `schema_version: 3`、`visibility: public`、`public_repo_ack: true` と所有者の明示承認がすべて揃う場合のみ許可。Private v2は従来どおり。
- 形式検査、認証アカウント確認、既存名衝突時の拒否、Issue番号＋slugの承認ロック、再実行時の二重作成防止を実装。
- **生成先RepoのURLを公開Issueや公開Actionsログには出さない。** 所有者がGitHub上で確認する。

## 新規アプリの初期化と運用保護（2026-10-18）

- [main保護設定](docs/BRANCH_PROTECTION.md)：PR必須・CI必須・強制pushと削除を禁止するRulesetの推奨値。**GitHub側のRulesetは未適用で、所有者による設定が必要**。
- [障害復旧・PAT期限管理](docs/INCIDENT_RUNBOOK.md)：承認ラベルをむやみに再付与しない、作成済みRepoと可視性を先に確認する。
- [初期ファイルと台帳引継ぎ](docs/REPO_INITIALIZATION.md)：作成後のREADME、AGENTS.md、index.html、ロードマップ、APP-IDの確認工程を分離。
- [最小Webスターター](templates/web-minimal/)：依存なしでスマートフォン対応を目指す静的HTMLの雛形。必要時のみ使う。
- [任意の安全なレンダラー](scripts/render_starter.py)：新規フォルダ内に4ファイルを生成し、既存フォルダへの上書きを拒否。生成先Repoへの自動書込みや秘密情報の取得は行わない。

作成専用トークンの権限を広げないため、**スターターのGitHubへの書込みは既存の認証済みGitHub接続で別途行う**。これらのファイルの追加で、Repo作成、APP-ID台帳登録、Web公開が自動完了するわけではありません。

## ChatGPT側での操作

| ChatGPTへの指示 | 処理 |
| --- | --- |
| 「新アプリ案：◯◯」 | 既存アプリ・Repoと照合し、**構想だけ整理**。Repoは作らない |
| 「この案を採用してApp Factoryに申請」 | 申請内容が公開可能か確かめ、`moyashimisosoup/app-factory`にIssueを登録。まだRepoは作らない |
| 「Issue #NNのRepo作成を承認」 | 内容・可視性と重複を再確認し、本人の明示承認がある場合にのみ`factory-approved`を付与 |
| Actions成功後 | GitHubの本人認証で新Repoを見つけ、申請された**Private/Public**を確認。初期ファイル作成とSession Deck登録は別工程 |

**各段階は別物です。** Issue登録、新Repo作成、初期ファイル保存、APP-ID台帳登録、公開サイト配信を混同しません。

## 最初の1回の設定

### 1. コードとCI

このRepoの`main`に以下が必要です。

- `scripts/create_repo.py`: 作成API、安全検査、冪等処理（v2 Private / v3 Public）
- `scripts/test_create_repo.py`: オフラインの回帰テスト
- `.github/workflows/ci.yml`: PRごとの安全検証
- `.github/workflows/preflight.yml`: `main`で自動実行する初期検証・承認用ラベル作成
- `.github/workflows/create-repo.yml`: **承認ラベルを付けた時だけ**実行する新Repo生成
- `.github/ISSUE_TEMPLATE/new-app.md`: 公開申請専用テンプレート

GitHub Actionsの **App Factory CI** と **App Factory offline readiness tests** の成功を確認し、`factory-approved`ラベルの存在を確認してください。権限不足やActions無効化なら実行は失敗します。その場合は稼働中と報告しません。

### 2. 専用の作成トークンを登録（所有者のGitHub画面で実施）

[GitHubのfine-grained PAT設定](https://github.com/settings/personal-access-tokens)で、GitHubユーザー `moyashimisosoup` 向けに期限付きの専用トークンを発行します。

- Permission: **Repository creation: Read and write** （API名`repository_creation:write`）。
- 可能な限り他のRepository権限・管理権限を付けず、既存Repoの削除・移管権限を付けない。
- `app-factory` → **Settings → Secrets and variables → Actions → New repository secret** に、名前 `APP_FACTORY_REPO_CREATOR` として登録。
- **トークンの値はチャット、Issue、コード、READMEへ絶対に貼らない。**
- GitHub Actions標準の`github.token`がIssueコメントを扱うため、`APP_FACTORY_ISSUE_TOKEN`を別途作る必要はありません。

公式情報：[GitHubの専用権限追加](https://github.blog/changelog/2026-10-13-github-app-improvements-for-least-privilege-and-management/)／[Repo作成API](https://docs.github.com/en/rest/repos/repos#create-a-repository-for-the-authenticated-user)。

### 3. 初めての動作確認（2026-10-17に1件成功。以下は次回以降も使う手順）

1. [Issue作成](https://github.com/moyashimisosoup/app-factory/issues/new/choose)から、一般公開して問題のない**採用済み**のアプリ申請を作る。テンプレートの`repo_name`等を確実に変更する。
2. **ラベルなし**ならリポジトリはできないことを確認する。
3. Repoが未使用名であることと可視性の承認を確かめてから、所有者が`factory-approved`を付ける。GitHub Actions `App Factory repository creation`が実行される。
4. Actionsが成功したら、**公開IssueにはRepoのURLが書かれない**ことを確認する。本人のGitHubリポジトリ一覧から生成先を開き、申請どおりの可視性を確認する。
5. GitHub接続に新Repoが見える場合、ChatGPTが`README.md`、`AGENTS.md`、`index.html`、`docs/ROADMAP.md`を整える。Session DeckのAPP-IDは全体台帳との照合後に登録する。
6. 同じIssueを編集して新しい名前に変更しても、承認済みslug以外の作成は拒否。作成済みの同じ申請は二重作成しない。

## ChatGPTプロジェクト指示への追記

- [ChatGPTプロジェクト用の短い追記文](docs/CHATGPT_PROJECT_ADDENDUM.md)に受付・本人承認・公開Issueの安全条件を記載しました。プロジェクト設定そのものはGitHubから変更できないため、ユーザーが一度手動で追加します。
- [AGENTS.md](AGENTS.md)にも同じ権限境界を記載しました。ChatGPT、Codex、Claude Codeの別作業者は先にこの短い正本を確認してください。

## 注意事項と限界

- 申請Issueに記載したslug/アプリ名/短い説明は**公開**される。Private Repoの中身自体はこのFactoryからは公開されない。一方、Public申請の作成先の内容は公開される。
- Issueの`public_intake_ack: true` は公開されることへの同意を示す。コードによる自動機密検出の保証ではない。
- 生成したRepoの初期ファイル配置、Session Deckの台帳登録、Web公開はまだ**自動化されていない**。ChatGPT GitHub操作で別途実施し、読戻し検証する。
- 現在接続されたChatGPT GitHubツールには「新Repo作成」の直接操作がないため、**GitHub Actionsで代理作成**する。専用Secretが未設定なら作成は失敗し、安全に停止する。
- GitHub Actionsが無効・利用枠制限・PAT権限不足・PAT期限切れの場合は未稼働とする。PATを無期限にしない。
- `moyashimisosoup`だけが申請・承認できる。所有者以外が公開Issueでラベルを付けても作成されない。
- 公開Factoryリポジトリに非公開Session Deckの内容を転載しない。

## 参考

- [App Factory起源と運用計画](https://github.com/moyashimisosoup/session-deck/blob/main/docs/APP_FACTORY_LAUNCH_PLAN.md)（この公開Repoへ移植する以前のPrivate受付案を含むため、**現在は本READMEの公開受付規則を優先**）
- [Session Deck全体台帳](https://github.com/moyashimisosoup/session-deck/blob/main/docs/APP_PORTFOLIO.md)
