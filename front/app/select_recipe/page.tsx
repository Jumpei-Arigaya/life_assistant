import SelectRecipe from "@/features/SelectRecipe";

const Page: () => Promise<JSX.Element> = async () => {
  return (
    <>
      <header className="py-4"></header>
      <main>
        <SelectRecipe />
      </main>
    </>
  );
};

export default Page;
