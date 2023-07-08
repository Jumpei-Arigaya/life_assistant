import { useApi } from "../api/api";
import { User } from "../types/type";
import { useRouter } from "next/navigation";

export const useAccounts = () => {
  const { loginApi } = useApi();
  const router = useRouter();

  /**
   * ログイン
   *
   * @param user フォームに入力されたユーザー情報
   */
  const login = async (user: User) => {
    try {
      const response = await loginApi(user);
      if (response.ok) {
        console.log(await response.json());
        router.push("/");
      } else {
        alert("ログインに失敗しました。ユーザー名かパスワードが誤っています。");
      }
    } catch (error) {
      console.log(error);
      alert("ログイン処理中にエラーが発生しました。");
    }
  };
  return { login };
};
