// import { login } from "../api/getRecipe";
// import { User } from "../types/type";
// import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { getRecipe } from "../api/getRecipe";

export const useSelectRecipeDialog = () => {
  const [recipe, setRecipe] = useState<any[]>([]);

  useEffect(() => {
    setRecipeList();
  }, []);

  /**
   * レシピリストをセットする
   */
  const setRecipeList = async () => {
    try {
      const response = await getRecipe();
      if (response.ok) {
        const data = await response.json();
        setRecipe(data);
      }
    } catch (error) {
      setRecipe([]);
      console.log(error);
    }
  };

  return { recipe };
};
