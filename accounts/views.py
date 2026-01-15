#ログインビューのクラスを継承するため
from django.contrib.auth.views import LoginView
#画面再表示・遷移に必要
from django.shortcuts import render, redirect
#ユーザーテーブル
from django.contrib.auth.models import User
#自動ログインに必要
from django.contrib.auth import authenticate, login

#ログイン画面
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


#アカウント登録画面
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        errors = {}

        if not username:
            errors.setdefault("username", []).append("ユーザー名を入力してください")
        else:
            if not (1 <= len(username) <= 20):
                errors.setdefault("username", []).append("ユーザー名は１文字～２０文字で入力してください")
            if User.objects.filter(username=username).exists():
                errors.setdefault("username", []).append("このユーザーは既に使われています")

        if not email:
            errors.setdefault("email", []).append("メールアドレスを入力してください")
        else:
            if User.objects.filter(email=email).exists():
                errors.setdefault("email", []).append("このメールアドレスは既に使われています")

        if not password1:
            errors.setdefault("password1", []).append("パスワードを入力してください")
        else:
            if len(password1) < 8:
                errors.setdefault("password1", []).append("パスワードは８文字以上に入力してください")
            has_letter = any(char.isalpha() for char in password1)
            has_number = any(char.isdigit() for char in password1)
            if not (has_letter and has_number):
                errors.setdefault("password1", []).append("パスワードは英字と数字の両方を含めてください")

        if not password2:
            errors.setdefault("password2", []).append("確認用パスワードを入力してください")
        else:
            if password1 and password1 != password2:
                errors.setdefault("password2", []).append("パスワードが一致しません")
        
        #エラー時に入力内容保持する（パスワード以外）
        if errors:
            return render(
                request,
                "accounts/register.html",
                {
                    "errors": errors,
                    "username": username,
                    "email": email,
                }
            )

        #ここでユーザーテーブルのカラムの中身を追加
        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        user = authenticate(username=username, password=password1)

        #エラー時に入力内容保持する（パスワード以外）
        if user is None:
            errors.append("ログイン処理に失敗しました もう一度お試しください")
            return render(
                request,
                "accounts/register.html",
                {
                    "errors": errors,
                    "username": username,
                    "email": email,
                }
            )
        login(request, user)

        return redirect("lists:list_index")
    return render(request, "accounts/register.html")