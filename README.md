# keycloak_sample
keycloakによるSAML対応サンプルアプリ


# 手順

## 1. 実行環境用意

` ./run.sh` を実行すると、keycloak/SAML使用サンプルサービスが実行されます。


## 2. Keycloakの基本設定

ここではIdPであるKeycloakの設定を行います。

- http://localhost:8080 にアクセスし、管理コンソール（admin / admin）を開きます。
- 左上メニューから Create Realm を開き、Nameを demo にして作成します。
- Users メニューからユーザー testuser を追加し、Credentials タブでパスワードを設定します。


## 3. サンプルアプリ登録

SAML対応サンプルアプリをKeycloakへ登録します。

- Realm「demo」内の Clients > Create client をクリックします。
- Client type に SAML、Client ID に my-python-sp と入力して進みます
- Valid redirect URIs に http://localhost:5001/saml/acs を設定して保存します。


## AuthnRequests signedをオフに

タブ : `Signature and Encryption` を確認し `Client signature required` をオフにする。


## 4. 動作確認








