import { User } from "../types/type";

/**
 * ログインAPIを呼び出す
 *
 * @param user フォームに入力されたユーザー情報
 * @returns
 */
export const login = async (user: User) => {
  const SERVER_URL = process.env.NEXT_PUBLIC_SERVER_URL;

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
