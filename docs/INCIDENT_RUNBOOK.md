# App Factory: エラー・復旧・トークン運用

このFactoryはPublic。Issue本文、コメント、Actionsのログも公開される。非公開RepoのURL、トークン値、内部情報を追加しない。

## 安全な判断順

1. [Actions](https://github.com/moyashimisosoup/app-factory/actions)で対象のRun IDと結論を確認する。まず実行されているかと失敗したStepだけを確認する。
2. 失敗していても、**すぐに承認ラベルを外して付け直さない**。作成先の実在、申請された可視性、READMEの状態を、所有者の認証済みGitHubから先に確認する。
3. 生成済みなら再作成しない。同じ申請にひも付く既存Repoであり、Private/Publicが一致するか確認する。公開IssueにPrivate RepoのURLを貼らない。
4. 未生成と確認できたときだけ、障害を直した後に同じIssue・slug・可視性で再実行できるか検討する。**ラベル再付与は改めてユーザーの明示承認が必要**。
5. Issueのslug、可視性、採用内容を変える場合は、古いIssueを改変して再利用せず、新しい申請として扱う。古い承認記録に不一致が生じた場合は安全に停止する。
6. 接続アプリがRepoを取得できない場合、Repo不在とは即断しない。GitHub Appの対象Repoアクセス範囲を照合する。

## 症状別の対応

| 症状 | 確認すること | 復旧方針 |
| --- | --- | --- |
| ラベル付与後にRunが出ない | Issueの作成者・ラベル適用者がmoyashimisosoupか、名前がfactory-approvedか、Actionsが有効か | 条件を確認。勝手に再承認しない |
| CIだけが失敗 | Python構文・ユニットテスト・YAML検証の結果 | コードのPRで修正。作成用Secretを変更しない |
| APP_FACTORY_REPO_CREATOR secret is missing | Actions Secretsに名前が一致するか | 所有者が設定。トークン値をチャットへ送らない |
| Credential identity does not match | fine-grained PATのresource owner、発行者・期限 | 対象Ownerの専用PATでSecretを差し替え |
| HTTP 401/403 | PATの有効期限・Repository creation: Read and write、API制限 | 最小権限の再確認。広いAdministration権限は付けない |
| Repository name already exists | 同名Repoが別Issueや手動で作られたか | 上書きせず停止。別のslugは新Issueで承認 |
| Issue has a different approval lock | 承認後にIssue内容が変更されたか | 同一Issueを再承認しない。新Issueが必要 |
| 作成Step成功・最後のコメントStepだけ失敗 | 所有者のGitHubでRepoが実在し、可視性が正しいか | Repo作成済みとして検証。URLを書かず公開Issueの通知だけを再検討 |
| Actions成功なのにRepoが見えない | GitHubコネクタの対象リポジトリ権限 | 所有者のGitHub画面とRepo APIで照合 |

## トークンの期限とローテーション

- トークン名: app-factory-repo-creator、Secret名: APP_FACTORY_REPO_CREATOR。
- 値やスクリーンショットをこのPublic Repo、Issue、Actions出力、チャットに保存しない。
- PATの実際の有効期限は接続GitHubツールから確認できない。所有者が [fine-grained token管理](https://github.com/settings/personal-access-tokens)で確認する。
- 期限の**30日前**を目安に新しい専用トークンを作り、既存Secretの値を差し替える。更新後は秘密を表示しないドライランや**実アプリの次回正規申請**で検証する。無意味なテストRepoを作り続けない。
- 期限前通知が必要なら、期限日だけをユーザーから確認してリマインダーに登録する。公開Issueに有効期限を記録する必要はない。
- 漏洩の疑いがあればGitHub画面で速やかにPATを失効、Secretを差し替え、Actions履歴と新規Repoを監査する。作成ワークフローを一時無効化する判断を優先する。

## インシデントを記録するとき

記録: JST確認時刻、公開Run URL、Issue番号、エラー種別（一般名）、生成の有無・可視性検証、復旧策、次の1操作。非公開Repo URLやPAT値は公開記録から省く。

安全性評価: 申請・Repo作成・初期ファイルの配置・台帳登録・Pages公開は別マイルストーン。
