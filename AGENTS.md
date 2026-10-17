# App Factory Agent Instructions

本リポジトリは **Public**。Issue、コメント、Actionsログ、PR差分は一般公開される。APIトークン、個人情報、学校の情報、チャットURL、非公開アプリの詳細、Private RepoのURLや内容を投稿しない。

## 受付と権限

- 「新アプリ案：」は構想相談のみ。勝手にIssue・Repoを作成しない。
- 「採用してApp Factoryへ申請」と本人が明示した場合だけ、**公開して問題のない一般的な情報**でIssueを作る。public_intake_ack=true、schema_version=2、visibility=privateを必須とする。機密性があれば公開Issueに投稿せず非公開の代替管理を提案。
- GitHubに同種/同名RepoやSession Deck台帳登録がないか、申請前に現在情報を照合。
- **Repo作成には追加の本人承認**が必要。対象Issue番号を再確認し、承認を得た時のみfactory-approvedラベルを追加する。
- Issueに承認ラベルを付ける前に、必要なActions Secret APP_FACTORY_REPO_CREATORの登録があると決めつけない。未確認なら未確認と伝える。
- 生成先Repoの可視性は Private 固定。Public Repo生成、削除・Archive、Pages公開、別オーナー作成は追加の明示承認なしに行わない。

## 完了基準

1. 公開Issueが作成できたことと、Private Repoが生成されたことを区別。
2. Actions成功、生成先の存在とPrivate状態の再確認が取れた場合のみ「Repo作成済み」と報告。
3. 初期ファイルのcommit/読戻し、APP-IDを台帳へ登録・読戻し、Pages公開、実機検収は**別々のマイルストーン**。
4. Secretの値はChatGPTへ送らせず、GitHub Actions Secretにのみ登録するよう案内。資格情報の存在を確認できない場合は未確認と記録。
5. 同一Issueの承認slugを変更・再作成しない。処理失敗時はGitHubの実行ログを確認し、非公開RepoのURLや秘密の漏洩を避けて原因を報告。
6. 本番用コードを変更するときは小さなPR＋CI検証＋main読戻しを優先する。

運用の正本は [README.md](README.md)。初期歴史資料は [Session Deck](https://github.com/moyashimisosoup/session-deck/blob/main/docs/APP_FACTORY_LAUNCH_PLAN.md)。
