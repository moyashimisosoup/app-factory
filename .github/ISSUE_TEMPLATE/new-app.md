---
name: 新アプリ採用申請（公開情報のみ）
about: GitHubに新規PRIVATEリポジトリを作る申請。ここに書いた内容は一般公開されます。
title: "APP FACTORY: "
labels: []
assignees: []
---

> ⚠️ **これは公開リポジトリのIssueです。誰でも読めます。**
> 非公開のアプリ構想、学校情報、個人情報、チャットURL、鍵、内部仕様を一切記載しないでください。
> 名前・説明・作成依頼の有無は公開されます。非公開で管理したい案件はここで申請しないでください。
> GitHubでの作成先リポジトリ自体はPrivateとして生成されます。

<!-- APP_FACTORY_REQUEST_V1 -->
~~~json
{
  "schema_version": 2,
  "repo_name": "replace-with-public-safe-slug",
  "app_name": "公開して差し支えない短い仮称",
  "description": "公開して差し支えない一般的なWebアプリ説明",
  "visibility": "private",
  "decision": "adopted",
  "public_intake_ack": true
}
~~~

## 作成前の確認

- [ ] このIssueの内容は、世界中から閲覧可能で問題ない
- [ ] Session Deckの全体台帳と既存GitHubリポジトリを照合し、重複しない
- [ ] アプリを開発対象として採用し、Privateリポジトリの作成を希望する
- [ ] 作成するリポジトリは当面Privateとし、公開は別途承認する

**Issueを開くだけでは作成されません。** `moyashimisosoup`本人が `factory-approved` ラベルを付けた時だけGitHub Actionsが実行されます。ChatGPTにラベル付与を依頼する場合は、対象Issueを明示して承認してください。

**重要:** 公開Issueには生成先のPrivateリポジトリURLを返信しません。作成後は所有者の認証済みGitHubで確認してください。
