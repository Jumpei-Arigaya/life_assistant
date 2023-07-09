/**
 * レシピ取得APIを呼び出す
 */
export const getRecipe = async () => {
  const SERVER_URL = process.env.NEXT_PUBLIC_SERVER_URL;

  const url = `${SERVER_URL}/recipe/recipe_list/`;
  const response = await fetch(url, {
    method: "GET",
  });

  return response;
};
