# App Factory: main保護の運用設定

対象: moyashimisosoup/app-factory（Public）。本書は設定手順であり、GitHub Rulesetの適用済み証拠ではありません。

## 推奨: main用Ruleset

1. GitHubで app-factory → Settings → Rules → Rulesets → New ruleset → New branch ruleset を開く。
2. Name: protect-main-app-factory / Enforcement status: Active / Target branches: default branch（main）を指定する。
3. Require a pull request before merging: **有効**。一人で開発する現段階では Required approvals **0**。一人しか書込権限がない状態で1以上を要求すると自分でPRを承認できず、運用を止める可能性がある。
4. Require status checks to pass: **有効**。実際に成功しているCIジョブ（通常は App Factory CI / verify）を選ぶ。表示された名前を確認し、存在しないチェックを指定しない。追加する場合はCheckの発行元をGitHub Actionsに限定する。
5. Block force pushes: **有効**。Block deletions: **有効**。
6. Require linear history: 利用するmerge方式を先に確認。squash mergeのみなら有効化可能。最初は必須にしなくてもよい。
7. Restrict creations / Restrict updates: 今回は使わない。管理者まで意図せずロックすることを避ける。
8. ルールのbypassやadministratorへの適用はGitHub画面で明示確認。試験中は設定を有効にしても既存PRのマージを阻害しない構成とする。
9. Save changes後にRulesetがActiveでmainに適用されていることをGitHubで読戻し、PRのrequired check挙動を実際に確認する。

## 確認の境界

- 2026-10-18の初回点検ではGitHub API GET /repos/moyashimisosoup/app-factory/rulesets の応答が空配列であり、Rulesetは未設定。
- GitHub接続にRulesetを作成する操作がないため、ユーザーのGitHub画面での設定が必要。設定手順をコミットしただけでは保護は有効にならない。
- Rulesetの適用後、変更後のGET結果と必要に応じてPRのステータスを照合して「適用済み」と記録する。
- あとから共同開発者が増えた場合に1名以上のreviewを要求するか検討する。その場合、トークン保護のため作者以外のレビューを優先する。

## コード変更の原則

- create-repo.yml、preflight.yml、scripts/create_repo.py、Issueテンプレート、認証・可視性・承認条件の変更は安全上の重要変更。
- 重要変更は小さなPRで、ユニットテスト・YAML構文検証・公開情報境界を確認後にマージ。
- Actions Secret自体をコードやIssueやPRに出さない。作成専用トークンをContentsの書込みや設定変更に使い回さない。

参考: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
