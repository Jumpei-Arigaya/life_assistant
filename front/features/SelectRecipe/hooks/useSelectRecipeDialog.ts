import { login } from "../api/getRecipe";
import { User } from "../types/type";
import { useRouter } from "next/navigation";
import { useState } from "react";

export const useLoginForm = () => {
  const [user, setUser] = useState<User>({});
  const router = useRouter();

  /**
   * ログイン
   *
   * @param user フォームに入力されたユーザー情報
   */
  const userLogin = async (user: User) => {
    try {
      const response = await login(user);
      if (response.ok) {
        router.push("/");
      } else {
        alert(
          "ログインに失敗しました。ユーザー名かパスワードが間違っているか、アカウントが登録されていません。"
        );
      }
    } catch (error) {
      console.log(error);
      alert("ログイン処理中にエラーが発生しました。");
    }
  };

  /**
   * サインインボタン実行時にログイン処理を実行する
   *
   * @param event イベント
   */
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    userLogin(user);
  };

  /**
   * フォームの内容が変更されたらユーザー情報を更新する
   *
   * @param e フォームに入力されたユーザー情報
   */
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUser((prevUser) => ({
      ...prevUser,
      [event.target.name]: event.target.value,
    }));
  };

  return { handleSubmit, handleChange, user };
};
