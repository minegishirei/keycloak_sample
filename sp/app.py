import os
from flask import Flask, request, render_template_string, redirect, session
from onelogin.saml2.auth import OneLogin_Saml2_Auth

app = Flask(__name__)
app.secret_key = 'python-saml-secret-key'

SAML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saml')

def init_saml_auth(req):
    auth = OneLogin_Saml2_Auth(req, custom_base_path=SAML_PATH)
    return auth

def prepare_flask_request(request):
    return {
        'https': 'on' if request.scheme == 'https' else 'off',
        'http_host': request.host,
        'script_name': request.path,
        'get_data': request.args.copy(),
        'post_data': request.form.copy()
    }

@app.route('/')
def index():
    attributes = session.get('samlUserdata', None)
    name_id = session.get('samlNameId', None)
    
    if name_id:
        html = """
        <h1>ログイン成功（Python SP保護エリア）</h1>
        <p><strong>NameID:</strong> {{ name_id }}</p>
        <pre>{{ attributes }}</pre>
        <a href="/logout">ログアウト</a>
        """
        return render_template_string(html, name_id=name_id, attributes=attributes)
    
    return '<h1>SAML認証デモ (Python SP)</h1><a href="/login">IdP（Keycloak）でログイン</a>'

# 1. HTTP Redirect BindingでIdPへリダイレクト
@app.route('/login')
def login():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    return redirect(auth.login())

# 2. HTTP POST BindingでSAML Assertion受取 (ACS: Assertion Consumer Service)
@app.route('/saml/acs', methods=['POST'])
def saml_acs():
    req = prepare_flask_request(request)
    auth = init_saml_auth(req)
    auth.process_response()
    errors = auth.get_errors()
    
    if not errors:
        session['samlUserdata'] = auth.get_attributes()
        session['samlNameId'] = auth.get_nameid()
        return redirect('/')
    else:
        return f"認証エラー: {', '.join(errors)}", 400

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)