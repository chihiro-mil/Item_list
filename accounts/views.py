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

        errors = []

        if not (1 <= len(username) <= 20):
            errors.append("ユーザー名は１文字～２０文字で入力してください")
        if not username:
            errors.append("ユーザー名を入力してください")
        if User.objects.filter(username=username).exists():
            errors.append("このユーザーは既に使われています")

        if not email:
            errors.append("メールアドレスを入力してください")
        if User.objects.filter(email=email).exists():
            errors.append("このメールアドレスは既に使われています")

        if not password1:
            errors.append("パスワードを入力してください")
        if len(password1) < 8:
            errors.append("パスワードは８文字以上に入力してください")
        has_letter = any(char.isalpha() for char in password1)
        has_number = any(char.isdigit() for char in password1)
        if not (has_letter and has_number):
            errors.append("パスワードは英字と数字の両方を含めてください")
        if not password2:
            errors.append("確認用パスワードを入力してください")
        if password1 != password2:
            errors.append("パスワードが一致しません")
        
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