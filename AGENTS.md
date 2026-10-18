# App Factory Agent Instructions

本リポジトリは **Public**。Issue、コメント、Actionsログ、PR差分は一般公開される。APIトークン、個人情報、学校の情報、チャットURL、非公開アプリの詳細、Private RepoのURLや内容を投稿しない。

## 受付と権限

- 「新アプリ案：」は構想相談のみ。勝手にIssue・Repoを作成しない。
- 「採用してApp Factoryへ申請」と本人が明示した場合だけ、**公開して問題のない一般的な情報**でIssueを作る。Private申請はpublic_intake_ack=true・schema_version=2・visibility=privateを必須とする。Public申請はschema_version=3・visibility=public・public_repo_ack=trueを追加し、明示的な公開承認がある場合のみ受理する。機密性があれば公開Issueに投稿せず非公開の代替管理を提案。
- GitHubに同種/同名RepoやSession Deck台帳登録がないか、申請前に現在情報を照合。
- **Repo作成には追加の本人承認**が必要。対象Issue番号を再確認し、承認を得た時のみfactory-approvedラベルを追加する。
- Issueに承認ラベルを付ける前に、必要なActions Secret APP_FACTORY_REPO_CREATORの登録があると決めつけない。未確認なら未確認と伝える。
- 生成先Repoの可視性はPrivateを初期値とする。Public作成はユーザーが対象RepoとPublic可視性を明示承認した場合だけ、v3申請を用いて許可する。削除・Archive、Pages公開、別オーナー作成は個別の明示承認なしに行わない。

## 完了基準

1. 公開Issueが作成できたことと、Private Repoが生成されたことを区別。
2. Actions成功、生成先の存在と申請されたPrivate/Public可視性の再確認が取れた場合のみ「Repo作成済み」と報告。
3. 初期ファイルのcommit/読戻し、APP-IDを台帳へ登録・読戻し、Pages公開、実機検収は**別々のマイルストーン**。
4. Secretの値はChatGPTへ送らせず、GitHub Actions Secretにのみ登録するよう案内。資格情報の存在を確認できない場合は未確認と記録。
5. 同一Issueの承認slugを変更・再作成しない。処理失敗時はGitHubの実行ログを確認し、非公開RepoのURLや秘密の漏洩を避けて原因を報告。
6. 本番用コードを変更するときは小さなPR＋CI検証＋main読戻しを優先する。

## 初期化と運用保護

- mainへの変更はPR・CI成功を原則とし、GitHubのブランチRuleset適用状況を別途確認する。設定案だけで「保護済み」と報告しない。[設定手順](docs/BRANCH_PROTECTION.md)。
- Actions失敗時は実Repoの有無・可視性を先に照合し、同一Issueのラベルを勝手に付け直さない。[復旧手順](docs/INCIDENT_RUNBOOK.md)。
- GitHub Actions Secretに保存するPATの実際の期限はGitHub画面で確認し、期限前更新は所有者が行う。Secretの値は取得・表示しない。
- Repo生成後のスターターは[初期化手順](docs/REPO_INITIALIZATION.md)に従い、テンプレートを必要な場合だけ使う。作成専用PATを既存Repoの内容編集に使わない。
- Session Deckの台帳は最新情報と公開可否を照合してから更新。試験用Repoを新アプリとして二重登録しない。

運用の正本は [README.md](README.md)。初期歴史資料は [Session Deck](https://github.com/moyashimisosoup/session-deck/blob/main/docs/APP_FACTORY_LAUNCH_PLAN.md)。
