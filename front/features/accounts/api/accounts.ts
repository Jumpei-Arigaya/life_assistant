import axios from "axios";

export const useAccounts = () => {
  const SERVER_URL = process.env.NEXT_PUBLIC_SERVER_URL;
  const login = async (username: string, password: string) => {
    axios
      .post(`${SERVER_URL}/user/login`, {
        username: username,
        password: password,
      })
      .then((response) => console.log(response))
      .catch((error) => console.log(error));
  };
  return { login };
};
