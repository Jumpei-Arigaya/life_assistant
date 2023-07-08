import { User } from "../types/type";

export const useApi = () => {
  const SERVER_URL = process.env.NEXT_PUBLIC_SERVER_URL;

  /**
   * ログインAPIを呼び出す
   *
   * @param user フォームに入力されたユーザー情報
   * @returns
   */
  const loginApi = async (user: User) => {
    const url = `${SERVER_URL}/user/login/`;
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        user,
      }),
    });

    return response;
  };

  return { loginApi };
};
