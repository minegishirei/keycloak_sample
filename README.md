# keycloak_sample
keycloakによるSAML対応サンプルアプリ


# 手順

ソースコードは以下から取得します。

```bash
git clone https://github.com/minegishirei/keycloak_sample.git
```


## 1. 実行環境用意

` ./run.sh` を実行すると、keycloak/SAML使用サンプルサービスが実行されます。


## 2. Keycloakの基本設定

ここではIdPであるKeycloakの設定を行います。

- http://localhost:8080 にアクセスし、管理コンソール（admin / admin）を開きます。

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image.png?raw=true" />

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%202.png?raw=true" />

- 左上メニューから Create Realm を開き、Nameを demo にして作成します。

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%203.png?raw=true" />

- Users メニューからユーザー testuser を追加し、Credentials タブでパスワードを設定します。


<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%204.png?raw=true" />

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%205.png?raw=true" />




## 3. サンプルアプリ登録

SAML対応サンプルアプリをKeycloakへ登録します。

- Realm「demo」内の Clients > Create client をクリックします。

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%206.png?raw=true" />


- Client type に SAML、Client ID に my-python-sp と入力して進みます

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%207.png?raw=true" />

- Valid redirect URIs に http://localhost:5001/saml/acs を設定して保存します。


<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%208.png?raw=true" />


## AuthnRequests signedをオフに

タブ : `Signature and Encryption` を確認し `Client signature required` をオフにする。

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%209.png?raw=true" />

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%2010.png?raw=true" />



## 4. 動作確認

<img src="https://github.com/minegishirei/keycloak_sample/blob/67756879bd160d5ed418af92b06c5ad444e49849/docs/image%20copy%2011.png?raw=true" />









